from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
import os
import cv2
from PIL import ImageGrab
import numpy as np
import matplotlib.pyplot as plt

model = load_model('./E_D/handwritten-digit-recognition-main/handwriting_CNN.h5')


def predict_digit(img):
    """function to predict the digit.
    Argument of function is PIL Image"""
    img.save('test.png')
    img = cv2.imread('test.png')
    # cv2.imshow('image', img)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray_image', gray_image)
    img = cv2.resize(gray_image, (28, 28))
    img = np.invert(np.array([img]))
    img = np.squeeze(img)

    #draw a digit
    plt.imshow(img)
    plt.colorbar()
    plt.show()

    # reshape
    img = img/255.0
    img = img.reshape(1, 28, 28, 1)

    #predicting the digit
    result = model.predict([img])[0]
    os.remove('test.png')
    return np.argmax(result), max(result)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        # Creating elements
        self.config(bg="#360f47")
        self.canvas = tk.Canvas(self, width=300, height=300, bg="white", cursor="cross")
        self.title("Digit recognition program")
        self.label = tk.Label(self, text="Draw digit",
                              font=("Bookman Old Style", 42),
                              fg="black",
                              bg="#360f47")
        self.classify_btn = tk.Button(self, width=40, text="Recognise",
                                      relief=RAISED,
                                      bd=4,
                                      command=self.classify_handwriting)
        self.button_clear = tk.Button(self, width=40, text="Clear",
                                      relief=RAISED,
                                      bd=4,
                                      command=self.clear_all)
        self.button_close = tk.Button(self, width=40, text="Close",
                                      relief=RAISED,
                                      bd=4,
                                      command=self.close_window)
        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        self.button_close.grid(row=2, column=0, pady=2)
        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
    def close_window(self):
        self.destroy()
    def clear_all(self):
        self.canvas.delete("all")
    def classify_handwriting(self):
        HWND = self.canvas.winfo_id() # get the handle of the canvas
        rect = win32gui.GetWindowRect(HWND) # get the coordinate of the canvas
        x1, y1, x2, y2 = rect
        # print(x1,x2, y1,y2)
        im = ImageGrab.grab((x1+40, y1+40, x2+100, y2+100))
        digit, acc = predict_digit(im)
        # print(digit)
        self.label.configure(text=str(digit)+', '+str(int(acc*100))+'%')
    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r=10
        self.canvas.create_oval(self.x-r, self.y-r, self.x + r, self.y + r, fill='black')

app = App()

# place window on computer screen, listen to events
mainloop()