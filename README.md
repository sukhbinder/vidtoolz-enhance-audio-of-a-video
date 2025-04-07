# vidtoolz-enhance-audio-of-a-video

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-enhance-audio-of-a-video.svg)](https://pypi.org/project/vidtoolz-enhance-audio-of-a-video/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-enhance-audio-of-a-video?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-enhance-audio-of-a-video/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-enhance-audio-of-a-video/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-enhance-audio-of-a-video/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-enhance-audio-of-a-video/blob/main/LICENSE)

Enhance audio of a video using ffmpeg

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-enhance-audio-of-a-video
```
## Usage

type ``vid enhance --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-enhance-audio-of-a-video
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
