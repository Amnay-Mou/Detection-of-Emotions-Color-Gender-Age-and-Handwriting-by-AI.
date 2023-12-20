# from tkinter import *
# from tkinter import filedialog
# print("Hello in get path: ")
# filepath = filedialog.askopenfilename()
# print(filepath)
# Import the required library
# from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox

# Create an instance of tkinter frame
# from pptx import Presentation
# f = open('manual/test.ppsx')
# prs = Presentation(f)
# f.close()
#import tkinter as tk


#class RoundedButton(tk.Canvas):

#    def __init__(self, master=None, text: str = "", radius=25, btnforeground="#000000", btnbackground="#ffffff",
#                 clicked=None, *args, **kwargs):
#        super(RoundedButton, self).__init__(master, *args, **kwargs)
#        self.config(bg=self.master["bg"])
#        self.btnbackground = btnbackground
#        self.clicked = clicked

#        self.radius = radius

#        self.rect = self.round_rectangle(0, 0, 0, 0, tags="button", radius=radius, fill=btnbackground)
#        self.text = self.create_text(0, 0, text=text, tags="button", fill=btnforeground, font=("Times", 30),
#                                     justify="center")

#        self.tag_bind("button", "<ButtonPress>", self.border)
#        self.tag_bind("button", "<ButtonRelease>", self.border)
#        self.bind("<Configure>", self.resize)

#        text_rect = self.bbox(self.text)
#        if int(self["width"]) < text_rect[2] - text_rect[0]:
#            self["width"] = (text_rect[2] - text_rect[0]) + 10

#        if int(self["height"]) < text_rect[3] - text_rect[1]:
#            self["height"] = (text_rect[3] - text_rect[1]) + 10

#    def round_rectangle(self, x1, y1, x2, y2, radius=25, update=False,
#                        **kwargs):  # if update is False a new rounded rectangle's id will be returned else updates existing rounded rect.
        # source: https://stackoverflow.com/a/44100075/15993687
#        points = [x1 + radius, y1,
#                  x1 + radius, y1,
#                  x2 - radius, y1,
#                  x2 - radius, y1,
#                  x2, y1,
#                  x2, y1 + radius,
#                  x2, y1 + radius,
#                  x2, y2 - radius,
#                  x2, y2 - radius,
#                  x2, y2,
#                  x2 - radius, y2,
#                  x2 - radius, y2,
#                  x1 + radius, y2,
#                  x1 + radius, y2,
#                  x1, y2,
#                  x1, y2 - radius,
#                  x1, y2 - radius,
#                  x1, y1 + radius,
#                  x1, y1 + radius,
#                  x1, y1]

#        if not update:
#            return self.create_polygon(points, **kwargs, smooth=True)

#        else:
#            self.coords(self.rect, points)

#    def resize(self, event):
#        text_bbox = self.bbox(self.text)

#        if self.radius > event.width or self.radius > event.height:
#            radius = min((event.width, event.height))

#        else:
#            radius = self.radius

#        width, height = event.width, event.height

#        if event.width < text_bbox[2] - text_bbox[0]:
#            width = text_bbox[2] - text_bbox[0] + 30

#        if event.height < text_bbox[3] - text_bbox[1]:
#            height = text_bbox[3] - text_bbox[1] + 30

#        self.round_rectangle(5, 5, width - 5, height - 5, radius, update=True)

#        bbox = self.bbox(self.rect)

#        x = ((bbox[2] - bbox[0]) / 2) - ((text_bbox[2] - text_bbox[0]) / 2)
#        y = ((bbox[3] - bbox[1]) / 2) - ((text_bbox[3] - text_bbox[1]) / 2)

 #       self.moveto(self.text, x, y)

#    def border(self, event):
#        if event.type == "4":
#            self.itemconfig(self.rect, fill="#d2d6d3")
#            if self.clicked is not None:
#                self.clicked()

 #       else:
 #           self.itemconfig(self.rect, fill=self.btnbackground)


#def func():
#    print("Button pressed")


#root = tk.Tk()
#fill = PhotoImage(file="C:/Users/amnay/PycharmProjects/project SE/Pic/ff3ywn-2.png")
#btn = RoundedButton(text="This is a \n rounded button", radius=100, btnbackground="#0078ff", btnforeground="#ffffff",
#                    clicked=func)
#btn.pack(expand=True, fill="both")
#root.mainloop()
# import tkinter as tk
# from tkVideoPlayer import TkinterVideo

# root = tk.Tk()

# videoplayer = TkinterVideo(master=root, scaled=True)
# videoplayer.load(r"C:/Users/amnay/PycharmProjects/project SE/Pic/Vid1.mp4")
# videoplayer.pack(expand=True, fill="both")

# videoplayer.play()  # play the video

# root.mainloop()
#from tkinter import *
#win = Tk()
#win.geometry("700x350")
#win.wm_attributes('-transparentcolor', '#ab23ff')
#Label(win, text= "Hello World!", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 50, ipady=50, padx= 20)
#win.mainloop()
from tkinter import *
import time
root = Tk()
root.geometry('600x300')
root.wm_attributes('-alpha',0.3)
Exit_butt = Button(root, text=" Go back ", command=root.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
Exit_butt.place(x=100, y=150)
l = Label(root,bg='white',text='Text',width=50,height=20)
l.pack()

root.mainloop()

