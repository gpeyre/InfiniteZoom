import numpy as np
from PIL import Image
from toolbox.znum2str import num2str
# Parameter to be changed if needed.

# Number of frames to be processed
Nb = 6
# Number of images to interpolate between frames
K = 100
# Define input and output directories
rep_in = 'output' # directory where input images are located
out_dir = 'animation' # directory where output images will be saved
# flag to determine whether to write output images to file
write_mode = True

f=[]
for i in range(1,Nb+1):
    image = Image.open(f'{rep_in}\im{i}.eps')
    f.append(image)
f.reverse()
# Determine the size of each frame
n = np.size(f[0])[1]

# Scaling factors - Note: the second assignment overrides the first one
rho = 2 #Final scaling factor for zoom

# Generate zoom levels between half-size and full-size
zl = rho**np.linspace(-1, 0, K+1)
np.delete(zl,-1)

# Counter for output images
k = 0

#Loop over each frame
for it in range(1,Nb+1):
    # Loop over each zoom level
    for i in range(1,K+1):
        # Current zoom level
        z = zl[i-1]
        # Calculate the size of the resized image
        q = round(z * n * rho)
        # Resize the current frame according to the zoom level
        F = f[it-1].resize((q,q), Image.LANCZOS)
        # Select the central part of the resized frame to keep the original frame size
        if q%2 == 0:
            sel1,sel2 = q/2 - n/2 -1, q/2 + n/2 
        else:
            sel1,sel2 = (q - 1)/2 - n/2 -1, (q - 1)/2 + n/2
        
        F = F.crop((sel1+1,sel1+1,sel2,sel2))
        # Increment the counter and save the image if write_mode is true
        k += 1
        if write_mode :
            F.save(f'{out_dir}\img{num2str(k, 4)}.eps')
