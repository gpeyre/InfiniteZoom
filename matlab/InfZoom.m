
%% Parameter to be changed if needed
% Define input and output directories
rep_in = 'output'; % directory where input images are located
out_dir = 'animation'; % directory where output images will be saved
write_mode = 1; % flag to determine whether to write output images to file
% Number of frames to be processed
Nb = 50;

% Add the "toolbox" directory to the path to use its functions and scripts
addpath("toolbox/")

% Initialize cell array to store frames
f = {};
% Read and process each frame in reverse order
for i = 1:Nb
    j = Nb - i + 1;
    % Read image and convert to grayscale by averaging color channels
    f{j} = imread([rep_in '/im' num2str(i) '.png']);
    f{j} = mean(f{j}, 3) / 255;
end
% Determine the size of each frame
n = size(f{1}, 1);

% Scaling factors - Note: the second assignment overrides the first one
rho = 2; % Final scaling factor for zoom

% Number of images to interpolate between frames
K = 20;
% Generate zoom levels between half-size and full-size
zl = rho.^linspace(-1, 0, K + 1); 
zl(end) = []; % Remove the last element to have exactly K zoom levels

% Counter for output images
k = 0;
% Loop over each frame
for it = 1:Nb
    % Loop over each zoom level
    for i = 1:K
        % Current zoom level
        z = zl(i);
        
        % Calculate the size of the resized image
        q = round(z * n * rho);
        % Resize the current frame according to the zoom level
        F = imresize(f{it}, [q q]);
        % Select the central part of the resized frame to keep the original frame size
        if mod(q, 2) == 0
            sel1 = q/2 - n/2 + 1 : q/2 + n/2;
        else
            sel1 = (q - 1)/2 - n/2 + 1 : (q - 1)/2 + n/2;
        end
        F = F(sel1, sel1);

        % Ensure pixel values are within [0,1]
        F(F < 0) = 0;
        F(F > 1) = 1;
        % Display the image without axes and in grayscale
        clf; imagesc(F); axis image; axis off;
        colormap gray;
        drawnow;
        % Increment the counter and save the image if write_mode is true
        k = k + 1;
        if write_mode
            imwrite(F, [out_dir '/anim-' num2str(k, '%04d') '.png']);
        end
    end
end
