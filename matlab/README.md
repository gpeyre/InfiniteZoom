# Infinite Zoom Toolbox

This toolbox contains a set of MATLAB scripts and directories for interactive drawing and infinite zoom animation creation. The main scripts included are `DrawingInteractive.m` for interactive image manipulation and `InfZoom.m` for generating zoom animations from a series of images.

## Directory Structure

- `animation/`: This directory is used to store the generated animation frames.
- `output/`: This directory contains the output images processed by the scripts.
- `toolbox/`: Contains additional MATLAB functions and scripts that are utilized by the main scripts.

### Workflow
Here's the corrected markdown text with appropriate formatting and minor grammatical corrections:

- Run `DrawingInteractive(0)` and draw the initial image. Press the `escape` key to exit. Ensure that some curves of your drawing touch the boundary of the drawing area.
- Run `DrawingInteractive(1)`, `DrawingInteractive(2)`, etc., to iteratively draw the subsequent images, by continuing the curve from each previous image, generating curves that touch the new boundaries.
- Once finished, edit `InfZoom.m` to set `Nb` to the number of images you have generated. You can change the value of `K` if you want more intermediate images.
- Run `InfZoom` to generate the interpolation.
- Install [ImageMagick]([link-to-imagemagick](https://imagemagick.org/)).
- Launch a terminal in the `animation/` folder and run:

  ```sh
  convert *.png anim.mp4
  ```



## Content

- `DrawingInteractive.m`: This script allows for interactive image drawing and manipulation. To run the script, simply execute it in the MATLAB environment. The interactive mode will be initiated, allowing you to perform various drawing tasks on the loaded image.
- `InfZoom.m` is used to create infinite zoom animations from a series of images. Before running the script, ensure that your images are placed in the `output/` directory. The script will process these images and save the animation frames to the `animation/` directory.

## License

This project is licensed under the MIT License.