from PIL import Image
import numpy as np
from tkinter import Tk, Toplevel, Label, Button
import sys
# end of imports

"""
Nonlinear Digital Imaging  - NDI Graphics library
v1.0

GPL license (c) Aaha3 2024
"""

class Render():
    def __init__(self, imGL):  # visualiser init
            self.imGL = np.load(imGL)  # Load image as NumPy array (assuming a saved .npy file)
    def visualizer(self):
        im_R = self.imGL.copy()
        im_R[:, :, (1, 2)] = 0
        im_G = self.imGL.copy()
        im_G[:, :, (0, 2)] = 0
        im_B = self.imGL.copy()
        im_B[:, :, (0, 1)] = 0
        self.im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)

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
        