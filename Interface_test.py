import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from tkVideoPlayer import TkinterVideo
import cv2


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


def Detect_Age_Gender_with_vid():
    exec(open('./E_D/Detect age & gender/Age & Gender detector vid.py').read())


def Detect_Age_Gender_with_cam():
    exec(open('./E_D/Detect age & gender/Age & Gender detector cam.py').read())


def start_ED_H_W():
    from E_D.gui import predict_digit


def pressExit(_):
    exit_button2.config(image=pi7)


def pressEmo(_):
    AI_com1.config(image=PicEmo2)


def pressHw(_):
    AI_com2.config(image=PicHw2)


def pressCol(_):
    AI_com3.config(image=PicCol2)


def pressAg(_):
    AI_com4.config(image=PicAg2)


def pressBy(_):
    canvas4.config(bg="yellow")


def pressBack(_):
    canvas4.destroy()


def RunPpt1():
    VidPlyer = Toplevel()
    VidPlyer.geometry("1000x750")
    videoplayer = TkinterVideo(master=VidPlyer, scaled=True)
    videoplayer.load(r"Vid Help/Detection of Emotions.mp4")
    videoplayer.pack(expand=True, fill="both")
    Exit_butt = tk.Button(VidPlyer, text=" Go back ", command=VidPlyer.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
    Exit_butt.place(x=30, y=670)
    videoplayer.play()


def RunPpt2():
    VidPlyer = Toplevel()
    VidPlyer.geometry("1000x750")
    videoplayer = TkinterVideo(master=VidPlyer, scaled=True)
    videoplayer.load(r"Vid Help/Detaction Colors.mp4")
    videoplayer.pack(expand=True, fill="both")
    Exit_butt = tk.Button(VidPlyer, text=" Go back ", command=VidPlyer.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
    Exit_butt.place(x=30, y=670)
    videoplayer.play()


def RunPpt3():
    VidPlyer = Toplevel()
    VidPlyer.geometry("1000x750")
    videoplayer = TkinterVideo(master=VidPlyer, scaled=True)
    videoplayer.load(r"Vid Help/Handwriting.mp4")
    videoplayer.pack(expand=True, fill="both")
    Exit_butt = tk.Button(VidPlyer, text=" Go back ", command=VidPlyer.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
    Exit_butt.place(x=30, y=670)
    videoplayer.play()


def RunPpt4():
    VidPlyer = Toplevel()
    VidPlyer.geometry("1000x750")
    videoplayer = TkinterVideo(master=VidPlyer, scaled=True)
    videoplayer.load(r"Vid Help/Detection of age & gender.mp4")
    videoplayer.pack(expand=True, fill="both")
    Exit_butt = tk.Button(VidPlyer, text=" Go back ", command=VidPlyer.destroy, fg="blue", font="SimSun 10 bold",
                          bg="#8B7D6B", cursor='hand2')
    Exit_butt.place(x=30, y=670)
    videoplayer.play()


#               ----------------------------------CREATE A NEW WINDOW----------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ------------------------------------------------CHILD1----------------------------------------------------------------
def create_emotions_detect():
    child1 = Toplevel()
    child1.geometry("700x550")
    child1.title("AI Detection Emotion")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/AI.png")
    bg_label = Label(child1, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------------------------------------
    can0 = tk.Canvas(child1, width=690, height=90, bg="#66CDAA")
    can0.create_text(350, 50, text="This AI Project help you in Detect Emotions using Camera or Video", fill="black",
                     font='Blanch 15 bold')
    can0.place(x=5, y=10)

    # ------------------------------- 2 Win
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
    def pressdisap(_):
        can2.destroy()
    child1_1 = Toplevel()
    child1_1.geometry("700x550")
    child1_1.title("AI Detection Emotion in Video")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/Emo.png")
    bg_label = Label(child1_1, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    can = tk.Canvas(child1_1, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="HELLO in Detection of Emotion in Video", fill="#F5F5F5", font='Helvetica 15 bold')
    can.place(x=5, y=10)

    Star_button2 = tk.Button(child1_1, text="Run Veo", command=start_ED_Vid, fg="Blue", cursor='hand2', bg='#00CD66')
    Star_button2.place(x=200, y=450)
    Star_button2.config(height=5, width=7)

    Exit_ch1_1 = tk.Button(child1_1, text="Exit", command=child1_1.destroy, fg="brown", cursor='hand2', bg='#00CD66')
    Exit_ch1_1.place(x=300, y=450)
    Exit_ch1_1.config(height=5, width=7)
    # -------------------------------- disappeared text
    can2 = tk.Canvas(child1_1, width=290, height=50, bg="Black")
    can2.create_text(150, 20, text="To stop Detection press 'x' ", fill="White",
                     font='Helvetica 15 bold')
    can2.place(x=400, y=490)
    can2.bind('<Leave>', pressdisap)


#       ------------------------------------------CHILD2----------------------------------------------------------------
def create_SecondAI():
    child2 = tk.Toplevel()
    child2.geometry("700x550")
    child2.title("AI Handwriting")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/hWtting.png")
    bg_label = Label(child2, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    exit_button1 = tk.Button(child2, text="Exit", fg="red", command=child2.destroy, cursor='hand2', bg='#CAE1FF')
    exit_button1.place(x=350, y=450)
    exit_button1.config(height=5, width=7)
    start_butt = tk.Button(child2, text="Start", fg="red", command=start_ED_H_W, cursor='hand2', bg='#CAE1FF')
    start_butt.place(x=250, y=450)
    start_butt.config(height=5, width=7)
    # -----------------------------------
    can = tk.Canvas(child2, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="HandWriting ", fill="black", font='Helvetica 15 bold')
    can.place(x=5, y=10)


def create_Second_DC_AI():
    child3 = Toplevel()
    child3.geometry("700x550")
    child3.title("AI Detection Color")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/PicColor.png")  # 1.png
    bg_label = Label(child3, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    can = tk.Canvas(child3, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="This AI project help you to Detect colors from image ", fill="black",
                    font='Helvetica 15 bold')
    can.place(x=5, y=10)

    exit_button1 = tk.Button(child3, text="Start D.C", fg="black", command=start_ED_Check_Color, cursor='hand2',
                             bg='yellow')
    exit_button1.place(x=280, y=270)
    exit_button1.config(height=5, width=15)

    Str_button1 = tk.Button(child3, text="Back", fg="gray", command=child3.destroy, cursor='hand2')
    Str_button1.place(x=300, y=460)
    Str_button1.config(height=5, width=10)


def create_Second_D_Ag():
    child4 = Toplevel()
    child4.geometry("700x550")
    child4.title("AI Detection Age & Gender")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/AgeGender.png")  # 1.png
    bg_label = Label(child4, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    can = tk.Canvas(child4, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="This AI project help you to Detect Age and Gender from video ", fill="black",
                    font='Helvetica 15 bold')
    can.place(x=5, y=10)
    # Detect_Age_Gender_with_vid
    Str_button1 = tk.Button(child4, text="Start\nage & gender", fg="black", command=cam_or_vid, cursor='hand2')

    Str_button1.place(x=220, y=460)
    Str_button1.config(height=5, width=10)

    exit_button1 = tk.Button(child4, text="Back", fg="gray", command=child4.destroy, cursor='hand2')
    exit_button1.place(x=350, y=460)
    exit_button1.config(height=5, width=10)


def cam_or_vid():
    def pressdisap2(_):
        can6.destroy()
    child5 = Toplevel()
    child5.geometry("700x550")
    child5.title("AI Detection Age & Gender")
    # ------------------------------- img
    filename = PhotoImage(file="Pic/AgeGender2.png")  # 1.png
    bg_label = Label(child5, image=filename)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename
    # -----------------------------------
    can = tk.Canvas(child5, width=690, height=90, bg="gray")
    can.create_text(350, 50, text="This AI project help you to Detect Age and Gender from video ", fill="black",
                    font='Helvetica 15 bold')
    can.place(x=5, y=10)

    Str_button1 = tk.Button(child5, text="Start Detector\nwith Vid", fg="black", command=Detect_Age_Gender_with_vid,
                            cursor='hand2')  # Detect_Age_Gender_with_vid
    Str_button1.place(x=250, y=260)
    Str_button1.config(height=5, width=15)

    Str_button2 = tk.Button(child5, text="Start Detector\nwith Cam", fg="black", command=Detect_Age_Gender_with_cam,
                            cursor='hand2')  # Detect_Age_Gender_with_vid
    Str_button2.place(x=370, y=260)
    Str_button2.config(height=5, width=15)

    exit_button1 = tk.Button(child5, text="Back", fg="gray", command=child5.destroy, cursor='hand2')
    exit_button1.place(x=300, y=460)
    exit_button1.config(height=5, width=10)
    # -------------------------------- Disappeared text
    can6 = tk.Canvas(child5, width=230, height=70, bg="Black")
    can6.create_text(110, 30, text="To stop Detection\n       press 'x' ", fill="white", font='Helvetica 15 bold')
    can6.place(x=440, y=470)
    can6.bind('<Leave>', pressdisap2)


#               ----------------------------------CREATE A Helper----------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def Create_helper0():
    Help_0 = Toplevel()
    Help_0.geometry("900x850")
    Help_0.title("manual")
    # ---------- 4 butt in inter to helper
    # ---------- Pic
    filename2 = PhotoImage(file="Pic/HelpPic.png")
    bg_label = Label(Help_0, image=filename2)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename2
    # ---------- Back
    exit_button1 = tk.Button(Help_0, text="Back", fg="gray", command=Help_0.destroy, cursor='plus')
    exit_button1.place(x=370, y=750)
    exit_button1.config(height=5, width=20)
    # ---------- DM
    DM_button1 = tk.Button(Help_0, text="Detect\nEmotion", fg="white", bg="blue", command=Create_helper_DE,
                           font='Helvetica 11 bold', cursor='hand2')
    DM_button1.place(x=260, y=160)
    DM_button1.config(height=5, width=50)
    # ---------- DC
    DC_button1 = tk.Button(Help_0, text="Detect\nColor", fg="white", bg="orange", command=Create_helper_DC,
                           font='Helvetica 11 bold', cursor='hand2')
    DC_button1.place(x=260, y=270)
    DC_button1.config(height=5, width=50)
    # ---------- HW
    HW_button1 = tk.Button(Help_0, text="Handwriting", fg="white", bg="green", command=Create_helper_HW,
                           font='Helvetica 11 bold', cursor='hand2')
    HW_button1.place(x=260, y=380)
    HW_button1.config(height=5, width=50)
    # ---------- A&G
    HW_button1 = tk.Button(Help_0, text="Age & Gender", fg="white", bg="#EE5C42", command=Create_helper_Ag,
                           font='Helvetica 11 bold', cursor='hand2')
    HW_button1.place(x=260, y=490)
    HW_button1.config(height=5, width=50)


def Create_helper_DE():
    Help_1 = Toplevel()
    Help_1.title("Manual of Detection Emotions")
    Help_1.geometry("900x850")
    # --------------------------------------- img
    filename3 = PhotoImage(file="Pic/Help1Pic.png")
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
    RunFile1 = tk.Button(Help_1, text="get Help", command=RunPpt1, fg="red", cursor='hand2')
    RunFile1.config(height=7, width=10)
    RunFile1.place(x=370, y=560)


def Create_helper_DC():
    Help_2 = Toplevel()
    Help_2.title("Manual of Detection Color")
    Help_2.geometry("900x850")
    # --------------------------------------- img
    filename4 = PhotoImage(file="Pic/Help2Pic.png")
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
    # -------------------------------- Run Vid
    RunFile2 = tk.Button(Help_2, text="get Help", command=RunPpt2, fg="red", cursor='hand2')
    RunFile2.config(height=7, width=10)
    RunFile2.place(x=370, y=560)


def Create_helper_HW():
    Help_3 = Toplevel()
    Help_3.title("Manual of Handwriting")
    Help_3.geometry("900x850")
    # --------------------------------------- img
    filename5 = PhotoImage(file="Pic/Help3Pic.png")
    bg_label = Label(Help_3, image=filename5)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename5
    # ------------------------------------------
    txt3 = tk.Canvas(Help_3, width=540, height=90, bg="green")
    txt3.create_text(150, 50, text="\t\tAI_Project H_W", fill="black", font='Helvetica 15 bold')
    txt3.place(x=5, y=120)
    txt3.config(border='0')
    Exit_ch3 = tk.Button(Help_3, text="Exit", command=Help_3.destroy, fg="red", cursor='hand2', border='0')
    Exit_ch3.place(x=380, y=760)
    Exit_ch3.config(height=5, width=9)
    # -------------------------------- Run Vid
    RunFile2 = tk.Button(Help_3, text="get Help", command=RunPpt3, fg="red", cursor='hand2')
    RunFile2.config(height=7, width=10)
    RunFile2.place(x=370, y=560)


def Create_helper_Ag():
    Help_3 = Toplevel()
    Help_3.title("Manual of age & gender")
    Help_3.geometry("900x850")
    # --------------------------------------- img
    filename5 = PhotoImage(file="Pic/HelpPic4.png")
    bg_label = Label(Help_3, image=filename5)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = filename5
    # ---------------------------------------
    txt3 = tk.Canvas(Help_3, width=540, height=90, bg="green")
    txt3.create_text(150, 50, text="\t\tAI_Project A_&_G", fill="black", font='Helvetica 15 bold')
    txt3.place(x=5, y=120)
    txt3.config(border='0')
    Exit_ch3 = tk.Button(Help_3, text="Exit", command=Help_3.destroy, fg="red", cursor='hand2', border='0')
    Exit_ch3.place(x=380, y=760)
    Exit_ch3.config(height=5, width=9)
    # -------------------------------- Run Vid
    RunFile2 = tk.Button(Help_3, text="get Help", command=RunPpt4, fg="red", cursor='hand2')
    RunFile2.config(height=7, width=10)
    RunFile2.place(x=370, y=560)


# ---------------------------------- Father
parent = tk.Tk()
parent.geometry("1000x850")
parent.title("AI")

img = ImageTk.PhotoImage(Image.open("Pic/ff3ywn-4.png"))
label = Label(parent, image=img)

text_disp = tk.Button(parent, text="Manual\nCheck", command=Create_helper0, bg="#63B8FF", font="Corbel 13 bold",
                      cursor='hand2')
text_disp.place(x=30, y=765)
text_disp.config(height=3, width=8)
label.pack()  # , relief=SUNKEN

#       ---------------------------------- PARENT ---------------------------------------------------------------------
pic = PhotoImage(file="Pic/Exitpic.png")
pi7 = PhotoImage(file="Pic/ByePic.png")
exit_button2 = tk.Button(parent, image=pic, cursor='clock', border=0, command=parent.destroy)
exit_button2.place(x=400, y=750)
exit_button2.config(height=90, width=120)
exit_button2.bind('<ButtonPress>', pressExit)

#       ---------------------------------- BUTT AI 1                                                          # emotions
PicEmo = PhotoImage(file="Pic/PicEmo.png")
PicEmo2 = PhotoImage(file="Pic/Emo2.png")
AI_com1 = tk.Button(parent, command=create_emotions_detect, border='0', image=PicEmo, cursor='heart')
AI_com1.place(x=735, y=210)
AI_com1.config(height=70, width=90)
AI_com1.bind('<ButtonPress>', pressEmo)

#       ---------------------------------- BUTT AI 2                                                        # no get yet
PicHw = PhotoImage(file="Pic/PicHw.png")
PicHw2 = PhotoImage(file="Pic/hw2.png")
AI_com2 = tk.Button(parent, image=PicHw, border='0', command=create_SecondAI,  cursor='spraycan')
AI_com2.place(x=735, y=340)
AI_com2.config(height=70, width=90)
AI_com2.bind('<ButtonPress>', pressHw)

#       ---------------------------------- BUTT AI 3                                                       # Check_Color
PicCol = PhotoImage(file="Pic/PicCol.png")
PicCol2 = PhotoImage(file="Pic/PicCol2.png")
AI_com3 = tk.Button(parent, text="AI_D.C", command=create_Second_DC_AI, image=PicCol, cursor='exchange', border='0')
AI_com3.place(x=735, y=460)
AI_com3.config(height=70, width=90)
AI_com3.bind('<ButtonPress>', pressCol)

#       ---------------------------------- BUTT AI 4                                                         # Check_A&G
PicAg = PhotoImage(file="Pic/AgePic.png")
PicAg2 = PhotoImage(file="Pic/GenderPic.png")
AI_com4 = tk.Button(parent, text="AI_D.Ag", command=create_Second_D_Ag, image=PicAg, cursor='exchange', border='0')
AI_com4.place(x=735, y=580)
AI_com4.config(height=70, width=90)
AI_com4.bind('<ButtonPress>', pressAg)

#       ---------------------------------- TEXT INTRO

canvas5 = tk.Canvas(parent, width=690, height=100, bg="#3D59AB")
canvas5.create_text(350, 50, text="  HELLO DEAR USER\nWelcome in AI World", fill="#40E0D0", font='Tahoma 25 bold')
canvas5.place(x=155, y=10)  # 5
# canvas.attributes('-alpha',0.5)

#       ---------------------------------- TEXT AI1

canvas1 = tk.Canvas(parent, width=540, height=90, bg="blue")
canvas1.create_text(150, 50, text="\t\tAI_Project Detection emotions", fill="#FFFFE0", font='Helvetica 15 bold')
canvas1.place(x=180, y=200)

#       ---------------------------------- TEXT AI2

canvas2 = tk.Canvas(parent, width=540, height=90, bg="green")
canvas2.create_text(150, 50, text="\t\tAI_Project Handwriting", fill="#FFFFE0", font='Helvetica 15 bold')
canvas2.place(x=180, y=330)

#       ---------------------------------- TEXT AI3
canvas3 = tk.Canvas(parent, width=540, height=90, bg="orange")
canvas3.create_text(155, 50, text="\t\tAI_Project Detection Color", fill="#FFFFE0", font='Helvetica 15 bold')
canvas3.place(x=180, y=450)

#       ---------------------------------- TEXT AI4
canvas5 = tk.Canvas(parent, width=540, height=90, bg="#EE5C42")
canvas5.create_text(155, 50, text="\t\tAI_Project Detection Gender & Age", fill="#FFFFE0", font='Helvetica 15 bold')
canvas5.place(x=180, y=570)

#       ---------------------------------- TEXT AI3
canvas4 = tk.Canvas(parent, width=120, height=50, bg='black', border='0')
canvas4.create_text(5, 27, text="\t\tBy: Amnay Mou", fill="red", font='Helvetica 10 bold')  #
canvas4.place(x=850, y=780)
parent.wm_attributes('-alpha', 0.9)
canvas4.bind('<ButtonRelease>', pressBy)
canvas4.bind('<Leave>', pressBack)

#       ----------------------------------

parent.mainloop()
# ---------------

# color " https://www.webucator.com/article/python-color-constants-module/ "
# justify='center'
