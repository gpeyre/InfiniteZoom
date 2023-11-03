function DrawingInteractive(num)

    % DrawingInteractive creates an interactive drawing environment where the user can draw with their mouse.
    % The drawing canvas is displayed as an overlay on top of a specified image.
    %
    % Parameters:
    %   num (integer): The iteration number of the drawing session. This number is used to load a specific 
    %   image file ('imX.png' where X is the iteration number) as the background for the drawing canvas.
    %   It also determines the filename of the output image which will be saved at the end of the drawing session.
    %
    % Output:
    %   There is no return value. However, this function produces a figure window where the user can interactively
    %   draw. Upon pressing the 'escape' key, the content of the figure is saved as 'output/imX.png', where X is
    %   num + 1, and the figure window is closed.
    %
    % Typical Use Case:
    %   The function is meant to be called in a sequence, starting with DrawingInteractive(0), which would load 'im0.png'
    %   as the background. The user can then draw on this canvas. When the user is finished and exits the application
    %   (by pressing the 'escape' key), the drawing is saved as 'output/im1.png'. The next iteration can be started
    %   by calling DrawingInteractive(1), which would now load 'im1.png' as the background, allowing the user to either
    %   continue drawing or start with a new background. This process can be repeated iteratively with increasing values
    %   of num to continue the interactive drawing sessions.
    %
    % Note: This function sets up several callback functions to handle mouse interactions for drawing and a keyboard
    % interaction to handle the save and exit operation. The drawing size dynamically changes based on the cursor's
    % distance from the center, providing a unique drawing experience. It is assumed that the necessary image files 
    % exist in the working directory. If an image cannot be loaded, the function silently fails to display the image 
    % but still allows for drawing on a blank canvas.
    %
    % Example:
    %   DrawingInteractive(0); % Start the first drawing session with 'im0.png' as the background.
    %   % After exiting, 'output/im1.png' will be saved.
    %   DrawingInteractive(1); % Continue with the next session using 'im1.png' as the background.
    %   % This can be repeated with DrawingInteractive(2), DrawingInteractive(3), etc.


    rho = 0.2; 
    rho = 0.5; 
    % Initialize the figure and axis
    fig = figure('Name', 'Drawing Interactive', 'NumberTitle', 'off');
    set(fig,'position',[200,200,1000,1000])
    ax = axes('Parent', fig, 'Position', [0 0 1 1]);
    axis([0 100 0 100]);
    axis square;
    hold on;
    set(ax, 'XTick', [], 'YTick', [], 'XTickLabel', [], 'YTickLabel', []);

    % Load and flip the image vertically
    imageName = sprintf('im%d.png', num);
    try
        img = imread(imageName);
        img = img(end:-1:1,:,:); % Flip vertically
        img = img(3:end-2,3:end-2,:); % remove black edge
        % Calculate the size to display the image
        drawingAreaWidth = diff(get(ax, 'XLim'));
        imageSize = drawingAreaWidth * rho;
        aspectRatio = size(img, 1) / size(img, 2);
        scaledHeight = imageSize * aspectRatio;
        scaledWidth = imageSize;
        % Display the image
        imagesc('XData', [50-scaledWidth/2, 50+scaledWidth/2], 'YData', [50-scaledHeight/2, 50+scaledHeight/2], 'CData', img);
        set(ax, 'YDir', 'normal'); % Ensure the image isn't flipped vertically
    catch
        % disp(['Error loading image: ' imageName]);
    end

    % Set up mouse button callbacks
    set(fig, 'WindowButtonDownFcn', @mouse_down);
    set(fig, 'WindowButtonUpFcn', @mouse_up);
    set(fig, 'WindowButtonMotionFcn', @mouse_move);
    set(fig, 'KeyPressFcn', @key_press);

    % Drawing state
    isDrawing = false;
    lastPoint = [];

    function mouse_down(~, ~)
        clickType = get(fig, 'SelectionType');
        if strcmp(clickType, 'normal')
            isDrawing = true;
            lastPoint = get(ax, 'CurrentPoint');
            lastPoint = lastPoint(1, 1:2);
        end
    end

    function mouse_up(~, ~)
        isDrawing = false;
        lastPoint = [];
    end

    function mouse_move(~, ~)
        if isDrawing
            currentPoint = get(ax, 'CurrentPoint');
            currentPoint = currentPoint(1, 1:2);

            if ~isempty(lastPoint)
                % Interpolate points between last point and current point for smoother drawing
                t = linspace(0, 1, ceil(norm(currentPoint - lastPoint))*5);
                x = (1 - t) * lastPoint(1) + t * currentPoint(1);
                y = (1 - t) * lastPoint(2) + t * currentPoint(2);

                % Calculate dot size based on position
                dotSize = 2 + (42 * sqrt((x - 50).^2 + (y - 50).^2) / 50);

                % Draw the line segments
                for i = 1:length(x)
                    plot(x(i), y(i), 'k.', 'MarkerSize', dotSize(i));
                end
            end

            lastPoint = currentPoint;
        end
    end

    function key_press(~, event)
        % Use the escape key to exit
        if strcmp(event.Key, 'escape')
            save_and_exit();
        end
    end

    function save_and_exit()
        % Save the content of the figure as an image
        frame = getframe(ax);
        im = frame2im(frame);
        % im = flip(im, 2); % Re-flip the image horizontally
        im = imresize(im, [512 512]*4, 'bilinear'); % Resize to 512x512 pixels
        nextImageName = sprintf('output/im%d.png', num+1);
        imwrite(im, nextImageName); % Save the image

        % Close the figure
        close(fig);
    end
end