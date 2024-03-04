"""
Nonlinear Digital Imaging  - NDI Graphics library API
=====

Driver i2342

NDI is a Simple Open-Source Graphics library used for rendering 2D Images with a rage of formats.

Commands:
-----

- NDI.Render('image.png')
- render = NDI.Render # <- recommended for easy 2D Rendering
- NDI.Render.visualiser() # <- make sure to set as a variable*
- NDI.Render.init_window(title,name,x,y,w,h) # <- work in progress, set as variable*

"""


from PIL import Image
import numpy as np
from numpy import asarray
from tkinter import Tk, Toplevel, Label, Button
import sys
# end of imports


class Render():
    global imGL
    def __init__(self, imGL):  # visualiser init
            try:
                self.imGL = asarray(imGL)
            except Exception as e:
                print(f"NDI: [!] Error loading image: {e}")
                self.imGL = None  # Handle the error gracefully

    def visualizer(imGL,self):
        
        
        if len(self.imGL.shape) == 2:  # Grayscale image
            self.im_RGB = np.zeros_like(self.imGL)  # Create empty 3-channel array
            im_R = np.stack((self.imGL, np.zeros_like(self.imGL), np.zeros_like(self.imGL)), axis=-1)
            im_G = np.stack((np.zeros_like(self.imGL), self.imGL, np.zeros_like(self.imGL)), axis=-1)
            im_B = np.stack((np.zeros_like(self.imGL), np.zeros_like(self.imGL), self.imGL), axis=-1)
        elif len(self.imGL.shape) == 3:
            im_R = self.imGL.copy()
            im_R[:, :, (1, 2)] = 0
            im_G = self.imGL.copy()
            im_G[:, :, (0, 2)] = 0
            im_B = self.imGL.copy()
            im_B[:, :, (0, 1)] = 0
            self.im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
        else:
            print(f"NDI: [!] image Render failed. image RGB value not found. RGB value: {imGL}")
            exit(1)

        pil_img = Image.fromarray(self.im_RGB)
        pil_img.save(self.imGL + ".png")
    
    def displ(self,title,name,x,y,w,h):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
        self.title = title
    
        # Create a new top-level window (popup)
        popup = Toplevel()
        popup.title(title)

        # This line makes the popup window modal (user can't interact with the main window until closing the popup)
        popup.grab_set()

        # Start the popup window's event loop
        popup.mainloop()

        
    def init_window(name,w,h,x,y):
        # Create the main window
        root = Tk()
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.title(name)

        # Create a button to trigger the popup window

        # Start the main window's event loop
        root.mainloop()
        

if __name__ == "__main__":  # package info (using sys.argv)
    arg = sys.argv[1] # set sys.argv list as variable

    if arg == "-d":
        print("driver version: i2342")
    if arg == "-de":
        print("driver editions: i2342")
    if arg == "-h":
        print("-d          - Current NDI driver")
        print("-dh         - NDI driver editions (history)")
        
        
