# Infinite Zoom Toolbox

This toolbox contains a set of MATLAB scripts and directories for interactive drawing and infinite zoom animation creation. The main scripts included are `DrawingInteractive.m` for interactive image manipulation and `InfZoom.m` for generating zoom animations from a series of images.

## Directory Structure

- `animation/`: This directory is used to store the generated animation frames.
- `output/`: This directory contains the output images processed by the scripts.
- `toolbox/`: Contains additional MATLAB functions and scripts that are utilized by the main scripts.

## Getting Started

To use this toolbox, clone or download this repository to your local machine and add it to your MATLAB path with the following command:

```matlab
addpath(genpath('path_to_toolbox'));
```

Replace `path_to_toolbox` with the actual path to the toolbox directory.

### Prerequisites

Ensure that you have MATLAB installed on your computer to run the scripts included in this toolbox.

## Usage

### DrawingInteractive.m

This script allows for interactive image drawing and manipulation. To run the script, simply execute it in the MATLAB environment. The interactive mode will be initiated, allowing you to perform various drawing tasks on the loaded image.

### InfZoom.m

`InfZoom.m` is used to create infinite zoom animations from a series of images. Before running the script, ensure that your images are placed in the `output/` directory. The script will process these images and save the animation frames to the `animation/` directory.

## License

This project is licensed under the MIT License.