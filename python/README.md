# Infinite Zoom Toolbox

This toolbox contains a set of Python scripts and directories for interactive drawing and infinite zoom animation creation. The main scripts included are `DrawingInteractive.py` for interactive image manipulation and `InfZoom.py` for generating zoom animations from a series of images.

## Requirements

You need to install the following programs :

- Install [ImageMagick]([link-to-imagemagick](https://imagemagick.org/)).
- Install [Ghostscript]([link-to-ghostscript](https://ghostscript.com/releases/gsdnld.html))

## Directory Structure

- `animation/`: This directory is used to store the generated animation frames.
- `output/`: This directory contains the output images processed by the scripts.
- `toolbox/`: Contains additional Python functions and scripts that are utilized by the main scripts.

### Workflow
Here's the corrected markdown text with appropriate formatting and minor grammatical corrections:

- Run `DrawingInteractive.py` and draw the initial image. Ensure that some curves of your drawing touch the boundary of the drawing area.
- Press the `Next` button to iteratively draw the subsequent images, by continuing the curve from each previous image, generating curves that touch the new boundaries.
- Once finished, press the 'End' button.
- Edit `InfZoom.py` to set `Nb` to the number of images you have generated. You can change the value of `K` if you want more intermediate images.
- Run `InfZoom.py` to generate the interpolation.
- Launch a terminal in the `animation/` folder and run:

  ```sh
  magick convert *.eps anim.mp4
  ```



## Content

- `DrawingInteractive.py`: This script allows for interactive image drawing and manipulation. To run the script, simply execute it in a python environment. The interactive mode will be initiated, allowing you to perform various drawing tasks on the loaded image.
- `InfZoom.py` is used to create infinite zoom animations from a series of images. Before running the script, ensure that your images are placed in the `output/` directory. The script will process these images and save the animation frames to the `animation/` directory.

## License

This project is licensed under the MIT License.