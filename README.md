# manim-linuxMobject

This is a small library to do what's in the image below:

  1. Display a line of text (like a command line prompt or result)
  2. Fade out all other text and start at beginning
  3. Fade in descriptions for each area

![manim gif](https://raw.githubusercontent.com/sorrell/sorrell.github.com/master/images/cli_prompt_example.gif)

Review the `cli_prompt_example.py` file for usage.

If you clone this repo, you will need to make sure the `manim` repository is in your `PYTHONPATH` (maybe put in bash/zsh profile):

`export PYTHONPATH=/my/path/to/manim`

Finally, to build the video:

`python3 -m manim cli_prompt_example.py cli_prompt_example`

