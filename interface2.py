import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


def write_text():
    print("Tkinter is easy to create GUI!")


def get_Path():
    filepath = filedialog.askopenfilename()
    print(filepath)


def start_ED_Vid():
    exec(open('./E_D/TestEmotionDetector 2.py').read())


def start_ED_Cam():
    exec(open('./E_D/TestEmotionDetector.py').read())


def start_ED_Check_Color():
    exec(open('./E_D/check Color.py').read())


def pressExit(_):
    exit_button2.config(image=pi7)


def pressEmo(_):
    AI_com1.config(image=PicEmo2)


def pressHw(_):
    AI_com2.config(image=PicHw2)


def pressCol(_):
    AI_com3.config(image=PicCol2)


def pressBy(_):
    canvas4.config(bg="yellow")


def pressBack(_):
    canvas4.destroy()


def presstt(_):
    AI_com4.config(image=PicCol8)


#               ----------------------------------CREATE A NEW WINDOW----------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ------------------------------------------------CHILD1----------------------------------------------------------------
def create_emotions_detect():
    child1 = Toplevel()
    child1.geometry("700x550")
    child1.title("AI Detection Emotion")
    # -------------------------------img
    filename = PhotoImage(file="Pic/AI.png")
    bg_label = Label(child1, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------------------------------------
    can0 = tk.Canvas(child1, width=690, height=90, bg="#66CDAA")
    can0.create_text(350, 50, text="This AI Project help you in Detect Emotions using Camera or Video", fill="black",
                     font='Blanch 15 bold')
    can0.place(x=5, y=10)

    # -------------------------------2 Win
    Star_button = tk.Button(child1, text=" With Cam ", command=start_ED_Cam, fg="#FF6103", font="SimSun 10 bold",
                            bg="#CDB79E", cursor='hand2')
    Star_button.place(x=300, y=450)
    Star_button1 = tk.Button(child1, text=" With Veo ", command=create_emotect_video, fg="red", font="SimSun 10 bold",
                             bg="#EED5B7", cursor='hand2')
    Star_button1.place(x=200, y=450)
    Exit_butt = tk.Button(child1, text=" Go back ", command=child1.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
    Exit_butt.place(x=400, y=450)
    # -----------------------------------------------------------------------------
    Star_button1.config(height=5, width=10)
    Star_button.config(height=5, width=10)
    Exit_butt.config(height=5, width=10)


#       ------------------------------------------CHILD1_1----------------------------------------------------------------
def create_emotect_video():
    child1_1 = Toplevel()
    child1_1.geometry("700x550")
    child1_1.title("AI Detection Emotion in Video")
    # -------------------------------img
    filename = PhotoImage(file="Pic/Emo.png")
    bg_label = Label(child1_1, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -------------------------------img
    # filename1 = PhotoImage(file="Pic/emotions pic.png")
    # bg_label1 = Label(child1_1, image=filename1)
    # bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
    # bg_label1.image = filename1
    # -----------------------------------------------------------------
    can = tk.Canvas(child1_1, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="HELLO in Detection of Emotion in Video", fill="yellow", font='Helvetica 15 bold')
    can.place(x=5, y=10)

    Star_button2 = tk.Button(child1_1, text="Run Veo", command=start_ED_Vid, fg="Blue", cursor='hand2')
    Star_button2.place(x=200, y=450)
    Star_button2.config(height=5, width=7)

    # Browse = tk.Button(child1_1, text="Browse", command=get_Path, fg="red")
    # Browse.place(x=100, y=450)
    Exit_ch1_1 = tk.Button(child1_1, text="Exit", command=child1_1.destroy, fg="brown", cursor='hand2')
    Exit_ch1_1.place(x=300, y=450)
    Exit_ch1_1.config(height=5, width=7)


#       ------------------------------------------CHILD2----------------------------------------------------------------
def create_SecondAI():
    child2 = tk.Toplevel()
    child2.geometry("700x550")
    child2.title("AI Handwriting")
    # -------------------------------img
    filename = PhotoImage(file="Pic/hWtting.png")
    bg_label = Label(child2, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    exit_button1 = tk.Button(child2, text="Exit", fg="red", command=child2.destroy, cursor='hand2')
    exit_button1.place(x=350, y=450)
    exit_button1.config(height=5, width=7)
    start_butt = tk.Button(child2, text="Start", fg="red", command=child2.destroy, cursor='hand2')
    start_butt.place(x=250, y=450)
    start_butt.config(height=5, width=7)
    # -----------------------------------
    can = tk.Canvas(child2, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="HandWirring ", fill="black", font='Helvetica 15 bold')
    can.place(x=5, y=10)


def create_Second_DC_AI():
    child3 = Toplevel()
    child3.geometry("700x550")
    child3.title("AI Detection Color")
    # -------------------------------img
    filename = PhotoImage(file="Pic/PicColor.png")  # 1.png
    bg_label = Label(child3, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    can = tk.Canvas(child3, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="This AI project help you to Detect colors from image ", fill="black",
                    font='Helvetica 15 bold')
    can.place(x=5, y=10)

    exit_button1 = tk.Button(child3, text="Start D.C", fg="black", command=start_ED_Check_Color, cursor='hand2')
    exit_button1.place(x=220, y=460)
    exit_button1.config(height=5, width=10)

    Str_button1 = tk.Button(child3, text="Back", fg="gray", command=child3.destroy, cursor='hand2')
    Str_button1.place(x=350, y=460)
    Str_button1.config(height=5, width=10)

#               ----------------------------------CREATE A Helper----------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def Create_helper0():
    Help_0 = Toplevel()
    Help_0.geometry("900x850")
    Help_0.title("manual")
    # ----------4 butt in inter to helper
    # ----------Pic
    filename2 = PhotoImage(file="Pic/HelpPic.png")
    bg_label = Label(Help_0, image=filename2)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename2
    # ----------Back
    exit_button1 = tk.Button(Help_0, text="Back", fg="gray", command=Help_0.destroy, cursor='plus')
    exit_button1.place(x=370, y=750)
    exit_button1.config(height=5, width=20)
    # ----------DM
    DM_button1 = tk.Button(Help_0, text="Detect\nEmotion", fg="white", bg="blue", command=Create_helper_DE,
                           font='Helvetica 11 bold', cursor='hand2')
    DM_button1.place(x=260, y=160)
    DM_button1.config(height=5, width=50)
    # ----------DC
    DC_button1 = tk.Button(Help_0, text="Detect\nColor", fg="white", bg="orange", command=Create_helper_DC,
                           font='Helvetica 11 bold', cursor='hand2')
    DC_button1.place(x=260, y=270)
    DC_button1.config(height=5, width=50)
    # ----------HW
    HW_button1 = tk.Button(Help_0, text="Handwriting", fg="white", bg="green", command=Create_helper_HW,
                           font='Helvetica 11 bold', cursor='hand2')
    HW_button1.place(x=260, y=380)
    HW_button1.config(height=5, width=50)


def Create_helper_DE():
    Help_1 = Toplevel()
    Help_1.title("Manual of Detection Emotions")
    Help_1.geometry("900x850")
    # ---------------------------------------img
    filename3 = PhotoImage(file="Pic/Help2Pic.png")
    bg_label = Label(Help_1, image=filename3)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename3
    # ------------------------------------------
    txt1 = tk.Canvas(Help_1, width=540, height=90, bg="blue")
    txt1.create_text(150, 50, text="\t\tAI_Project D_E", fill="black", font='Helvetica 15 bold')
    txt1.place(x=5, y=120)
    Exit_ch1 = tk.Button(Help_1, text="Exit", command=Help_1.destroy, fg="red", cursor='hand2')
    Exit_ch1.place(x=370, y=760)
    Exit_ch1.config(height=5, width=9)


def Create_helper_DC():
    Help_2 = Toplevel()
    Help_2.title("Manual of Detection Color")
    Help_2.geometry("900x850")
    # ---------------------------------------img
    filename4 = PhotoImage(file="Pic/1715114.png")
    bg_label = Label(Help_2, image=filename4)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename4
    # ------------------------------------------
    txt2 = tk.Canvas(Help_2, width=540, height=90, bg="orange")
    txt2.create_text(150, 50, text="\t\tAI_Project D_C", fill="black", font='Helvetica 15 bold')
    txt2.place(x=5, y=120)
    Exit_ch2 = tk.Button(Help_2, text="Exit", command=Help_2.destroy, fg="red", cursor='hand2')
    Exit_ch2.place(x=370, y=760)
    Exit_ch2.config(height=5, width=9)


def Create_helper_HW():
    Help_3 = Toplevel()
    Help_3.title("Manual of Handwriting")
    Help_3.geometry("900x850")
    # ---------------------------------------img
    filename5 = PhotoImage(file="Pic/Help4Pic.png")
    bg_label = Label(Help_3, image=filename5)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename5
    # ------------------------------------------
    txt3 = tk.Canvas(Help_3, width=540, height=90, bg="green")
    txt3.create_text(150, 50, text="\t\tAI_Project H_W", fill="black", font='Helvetica 15 bold')
    txt3.place(x=5, y=120)
    Exit_ch3 = tk.Button(Help_3, text="Exit", command=Help_3.destroy, fg="red", cursor='hand2')
    Exit_ch3.place(x=380, y=760)
    Exit_ch3.config(height=5, width=9)


# ----------------------------------Father
parent = tk.Tk()
parent.geometry("1100x880")
parent.title("AI")

img1 = ImageTk.PhotoImage(Image.open('Pic/ff3ywn-3.png'))
label = Label(parent, image=img1)

text_disp = tk.Button(parent, text="Manual\nCheck", command=Create_helper0, bg="#63B8FF", font="Corbel 13 bold",
                      cursor='hand2')
text_disp.place(x=200, y=790)
text_disp.config(height=2, width=7)
label.pack()  # , relief=SUNKEN

#       ----------------------------------PARENT-----------------------------------------------------------------------
pic = PhotoImage(file="Pic/Exit pic.png")
pi7 = PhotoImage(file="Pic/by.png")
exit_button2 = tk.Button(parent, image=pic, cursor='clock', border=0, command=parent.destroy)
# text="Exit", fg="#000080", command=parent.destroy, bg="#CD4F39", font="Corbel 13 bold"
exit_button2.place(x=400, y=790)
exit_button2.config(height=60, width=100)
exit_button2.bind('<ButtonPress>', pressExit)

#       ----------------------------------BUTT AI 1                                                           # emotions
PicEmo = PhotoImage(file="Pic/PicEmo.png")
PicEmo2 = PhotoImage(file="Pic/Emo2.png")
AI_com1 = tk.Button(parent, command=create_emotions_detect, border='0', image=PicEmo, cursor='heart')
AI_com1.place(x=725, y=230)
AI_com1.config(height=70, width=90)
AI_com1.bind('<ButtonPress>', pressEmo)

#       ----------------------------------BUTT AI 2                                                         # no get yet
PicHw = PhotoImage(file="Pic/PicHw.png")
PicHw2 = PhotoImage(file="Pic/hw2.png")
AI_com2 = tk.Button(parent, image=PicHw, border='0', command=create_SecondAI,  cursor='spraycan')
AI_com2.place(x=725, y=345)
AI_com2.config(height=70, width=90)
AI_com2.bind('<ButtonPress>', pressHw)

#       ----------------------------------BUTT AI 3                                                        # Check_Color
PicCol = PhotoImage(file="Pic/PicCol.png")
PicCol2 = PhotoImage(file="Pic/PicCol2.png")
AI_com3 = tk.Button(parent, text="AI_D.C", command=create_Second_DC_AI, image=PicCol, cursor='exchange', border='0')
AI_com3.place(x=725, y=460)
AI_com3.config(height=70, width=90)
AI_com3.bind('<ButtonPress>', pressCol)

#       ----------------------------------BUTT AI 4                                                        # Check_Color
PicCol9 = PhotoImage(file="Pic/PicCol.png")
PicCol8 = PhotoImage(file="Pic/PicCol2.png")
AI_com4 = tk.Button(parent, text="AI_D.C", command=create_Second_DC_AI, image=PicCol, cursor='exchange', border='0')
AI_com4.place(x=725, y=575)
AI_com4.config(height=70, width=90)
AI_com4.bind('<ButtonPress>', presstt)

#       ----------------------------------TEXT INTRO

canvas = tk.Canvas(parent, width=690, height=100, bg="#3D59AB")
canvas.create_text(350, 50, text="  HELLO DEAR USER\nWelcome in AI World", fill="#40E0D0", font='Tahoma 25 bold')
canvas.place(x=200, y=10)
# canvas.attributes('-alpha',0.5)

#       ----------------------------------TEXT AI1

canvas1 = tk.Canvas(parent, width=540, height=90, bg="blue")
canvas1.create_text(150, 50, text="\t\tAI_Project Detection emotions", fill="#FFFFE0", font='Helvetica 15 bold')
canvas1.place(x=170, y=220)

#       ----------------------------------TEXT AI2

canvas2 = tk.Canvas(parent, width=540, height=90, bg="green")
canvas2.create_text(150, 50, text="\t\tAI_Project Handwriting", fill="#FFFFE0", font='Helvetica 15 bold')
canvas2.place(x=170, y=330)

#       ----------------------------------TEXT AI3
canvas3 = tk.Canvas(parent, width=540, height=90, bg="orange")
canvas3.create_text(150, 50, text="\t\tAI_Project Detection Color", fill="#FFFFE0", font='Helvetica 15 bold')
canvas3.place(x=170, y=450)

#       ----------------------------------TEXT AI4
canvas5 = tk.Canvas(parent, width=540, height=90, bg="black")
canvas5.create_text(150, 50, text="\t\tAI_Project .........", fill="#FFFFE0", font='Helvetica 15 bold')
canvas5.place(x=170, y=570)

#       ----------------------------------TEXT AI BY
canvas4 = tk.Canvas(parent, width=120, height=50, bg='black', border='0')
canvas4.create_text(5, 27, text="\t\tBy: Amnay Mou", fill="red", font='Helvetica 10 bold')  #
canvas4.place(x=970, y=820)
parent.wm_attributes('-alpha', 0.9)
canvas4.bind('<ButtonRelease>', pressBy)
canvas4.bind('<Leave>', pressBack)

#       ----------------------------------


parent.mainloop()
# ---------------

# color " https://www.webucator.com/article/python-color-constants-module/ "
# justify='center'
