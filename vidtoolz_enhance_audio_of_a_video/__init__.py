import vidtoolz
import subprocess
import os

def determine_output_path(input_file, output_file):
    input_dir, input_filename = os.path.split(input_file)
    name, _ = os.path.splitext(input_filename)

    if output_file:
        output_dir, output_filename = os.path.split(output_file)
        if not output_dir:  # If no directory is specified, use input file's directory
            return os.path.join(input_dir, output_filename)
        return output_file
    else:
        return os.path.join(input_dir, f"{name}_enhance.mp4")
    
def build_filter_chain(mode, volume):
    if mode == "voice":
        return (
            f"highpass=f=100,"
            f"equalizer=f=3000:t=q:w=1:g=5,"
            f"compand=attacks=0:decays=0:points=-90/-900|-70/-70|-20/-20|20/20,"
            f"volume={volume}"
        )
    elif mode == "music":
        return (
            f"equalizer=f=100:t=q:w=1:g=5,"  # Boost bass
            f"equalizer=f=1000:t=q:w=1:g=-3,"  # Slight dip in mids
            f"equalizer=f=8000:t=q:w=1:g=4,"  # Boost treble
            f"compand=attacks=0:decays=0:points=-90/-900|-70/-70|-20/-20|20/20,"
            f"volume={volume}"
        )
    else:
        raise ValueError(f"Unknown mode: {mode}")


def enhance_audio(input_file, output_file, mode="voice", volume=1.5):
    filter_chain = build_filter_chain(mode, volume)

    cmd = ["ffmpeg", "-i", input_file, "-af", filter_chain, "-c:v", "copy", output_file]

    print("Running command:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def create_parser(subparser):
    parser = subparser.add_parser(
        "enhance", description="Enhance audio of a video using ffmpeg"
    )
    # Add subprser arguments here.
    parser.add_argument("input", help="Input video file (e.g., input.mp4)")
    parser.add_argument("-o","--output", default=None, help="Output video file (e.g., input_enhance.mp4)")
    parser.add_argument(
        "-m",
        "--mode",
        choices=["voice", "music"],
        default="voice",
        help="Enhancement mode: 'voice' or 'music' (default: voice)",
    )
    parser.add_argument(
        "-v",
        "--volume",
        type=float,
        default=1.5,
        help="Volume multiplier (default: 1.5)",
    )
    return parser


class ViztoolzPlugin:
    """Enhance audio of a video using ffmpeg"""

    __name__ = "enhance"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)

    def run(self, args):
        output = determine_output_path(args.input, args.output)
        enhance_audio(args.input, output, args.mode, args.volume)

    def hello(self, args):
        # this routine will be called when "vidtoolz "enhance is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


enhance_plugin = ViztoolzPlugin()
