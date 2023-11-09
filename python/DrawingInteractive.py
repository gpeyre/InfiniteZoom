"""

DrawingInteractive creates an interactive drawing environment where the user can draw with their mouse.

	Output:
    There is no return value. However, this function produces a figure window where the user can interactively
    draw. Clicking on the 'Next' button saves the contents of the figure as 'output/imX.png',
    where X is the number of the current image, and produces a new canva on which to draw, with the X image resized in the center.
    Clicking on the "End" button saves the contents of the figure as "output/imX.png",
    where X is the number of the current image, and closes the figure window.
    
    Typical Use Case:
    All you need to do is run the program once.
    You can stop image generation at any time.
    You can also change pencil size and color, and erase traces.
    
    Note : Drawing size does not change dynamically according to the
    cursor's distance from the center, in contrast to the matlab version.
    On the other hand, you can select different sizes and colors, and erase your strokes.

"""

import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk


w,h = 1024, 1024 # width and height of the figure
wm,hm = 100,100 # corresponding marges
c = 0 #image counter

# Initialize the figure
app = tk.Tk()
app.title(f"Drawing Interactive") # Title of the current figure
app.geometry(f'{w+100}x{h}') # Default size, can be changed above

# Default color & size of pencil
stroke_color = tk.StringVar()
stroke_color.set("black")

stroke_size = tk.IntVar()
stroke_size.set(3)


#Frame 0 - SideMenu
frame0 = tk.Frame(app,width=100,height=h)
frame0.grid(row=0,column=0,sticky='NW')

#Frame T - Tools
frame_t = tk.Frame(frame0,width=100,height=300)
frame_t.grid(row=0,column=0,sticky='NW')

#Tools Frame
toolsFrame = tk.Frame(frame_t,width=100,height=100)
toolsFrame.grid(row=0,column=0)

def usePencil():
    stroke_color.set("black")
    canvas["cursor"] = "arrow"
    
def useEraser():
    stroke_color.set("white")
    canvas["cursor"] = tk.DOTBOX

pencilButton = tk.Button(toolsFrame, text='Pencil',width=10,command=usePencil)
pencilButton.grid(row=2,column=0)

EraserButton = tk.Button(toolsFrame, text='Eraser',width=10,command=useEraser)
EraserButton.grid(row=1,column=0)

ToolsLabel = tk.Label(toolsFrame, text='Tools',width=10)
ToolsLabel.grid(row=0,column=0)

# Frame s - Size
frame_s = tk.Frame(frame0,width=100,height=300)
frame_s.grid(row=1,column=0)

#Size & Color Frame
sizeFrame = tk.Frame(frame_s,width=100,height=100)
sizeFrame.grid(row=0,column=1)

def selectColor():
    selectedColor = tk.colorchooser.askcolor(title="Select Color")
    if selectedColor[1] == None:
        stroke_color.set("black")
    else:
        stroke_color.set(selectedColor[1])

colorBoxButton = tk.Button(sizeFrame, text='Color',width=10,command=selectColor)
colorBoxButton.grid(row=0,column=0)

options = [1,2,3,5,10,30]

emptySizeLabel = tk.Label(sizeFrame, text='',width=10)
emptySizeLabel.grid(row=1,column=0)

sizeLabel = tk.Label(sizeFrame, text='Size',width=10)
sizeLabel.grid(row=2,column=0)

sizeList = tk.OptionMenu(sizeFrame, stroke_size, *options)
sizeList.grid(row=3,column=0)



#Frame E - End
frame_e = tk.Frame(frame0,width=100,height=300)
frame_e.grid(row=2,column=0,sticky='NW')

#Save and Exit Frame
infiniteZoomFrame = tk.Frame(frame_e,width=100,height=100)
infiniteZoomFrame.grid(row=2,column=0)


def nextImage():
    global c
    c+=1
    
    canvas.postscript(file=f'output\im{c}.eps') # save canvas as encapsulated postscript
    
    image = Image.open(f'output\im{c}.eps')
    image = image.resize((w//2,h//2), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    canvas.delete('all')
    app.image = image
    canvas.create_image(w//2,h//2, image=image, anchor='center')


def endImage():
    global c
    c+=1
    canvas.postscript(file=f'output\im{c}.eps') # save canvas as encapsulated postscript
    app.destroy()


emptyLabel = tk.Label(infiniteZoomFrame, text='',width=10)
emptyLabel.grid(row=0,column=0)

infiniteLabel = tk.Label(infiniteZoomFrame, text='Frames',width=10)
infiniteLabel.grid(row=1,column=0)

nextButton = tk.Button(infiniteZoomFrame, text='Next',width=10,command=nextImage)
nextButton.grid(row=2,column=0)

endButton = tk.Button(infiniteZoomFrame, text='End',width=10,command=endImage)
endButton.grid(row=3,column=0)

#Frame C - Canvas
frame_c = tk.Frame(app,width=w,height=h,bg='white')
frame_c.grid(row=0,column=1,sticky='NW')



canvas = tk.Canvas(frame_c, width=w, height=h, bg='white')
canvas.grid(row=1,column=0)


# Variables for the Pencil / Eraser
prevPoint = [0,0]
currentPoint = [0,0]

def paint(event):
    global prevPoint, currentPoint
    x = event.x
    y = event.y
    currentPoint = [x,y]
    
    if prevPoint != [0,0]:
        #No interpolation here, unlike the Matlab version. We simply trace a line by drawing successive ovals of the same size.
        canvas.create_oval(prevPoint[0],prevPoint[1],currentPoint[0],
                           currentPoint[1],fill=stroke_color.get(),outline=stroke_color.get(),width=stroke_size.get())
    
    prevPoint = currentPoint
    
    if event.type == "5":
        prevPoint = [0,0]


canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)

app.mainloop()