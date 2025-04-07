import pytest
import vidtoolz_enhance_audio_of_a_video as w

from argparse import ArgumentParser

# Replace 'your_module_name' with the actual Python filename (without .py)


def test_build_filter_chain_voice():
    volume = 1.5
    expected = (
        "highpass=f=100,"
        "equalizer=f=3000:t=q:w=1:g=5,"
        "compand=attacks=0:decays=0:points=-90/-900|-70/-70|-20/-20|20/20,"
        f"volume={volume}"
    )
    result = w.build_filter_chain("voice", volume)
    assert result == expected


def test_build_filter_chain_music():
    volume = 2.0
    expected = (
        "equalizer=f=100:t=q:w=1:g=5,"
        "equalizer=f=1000:t=q:w=1:g=-3,"
        "equalizer=f=8000:t=q:w=1:g=4,"
        "compand=attacks=0:decays=0:points=-90/-900|-70/-70|-20/-20|20/20,"
        f"volume={volume}"
    )
    result = w.build_filter_chain("music", volume)
    assert result == expected


def test_build_filter_chain_invalid_mode():
    with pytest.raises(ValueError, match="Unknown mode: podcast"):
        w.build_filter_chain("podcast", 1.0)


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    args = parser.parse_args(["in.mp4", "-o","out.mp4", "-m", "voice", "--volume", "1.2"])
    assert args.input == "in.mp4"
    assert args.output == "out.mp4"
    assert args.mode == "voice"
    assert args.volume == 1.2


def test_plugin(capsys):
    w.enhance_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out
