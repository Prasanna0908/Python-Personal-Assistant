from email.message import EmailMessage
import smtplib
import re
import phonenumbers
from math import e
from PIL import Image  # pip install pillow
from tkinter import messagebox
import mysql.connector
from captcha.image import ImageCaptcha

import string
from tkinter import Tk
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
import PIL.Image
import threading
import time,pyautogui,pyjokes,PyPDF2

import random, subprocess
import wolframalpha
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import urllib
import io





# # Main_funcn
# def main():
#     win = Tk()
#     app = Login_Window(win)
#     win.mainloop()

#class Login
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1536x864+225+50")


        self.compText = StringVar()

    #background

        framenew=Frame(self.root,bg="black")
        framenew.place(x=0,y=0,relwidth=1,relheight=1)

        imgnew = Image.open(r"JARVIS IMAGES\Login_Window_Figma2.png")
        imgnew = imgnew.resize((1536, 864), Image.ANTIALIAS)
        self.PhotoImagenew = ImageTk.PhotoImage(imgnew)
        lblimg6 = Label(framenew,image=self.PhotoImagenew, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)



        #Username_Entry
        self.txtname=Entry(font=("arial",13),relief="flat")
        self.txtname.place(x=660,y=320,width=245,height=30)

        #Password_Entry
        self.txtpass=Entry(font=("arial",13),show="*",relief="flat")
        self.txtpass.place(x=660,y=446,width=245,height=30)

        #Signinbutton_Image
        img2 = Image.open(r"JARVIS IMAGES\Signin_Button_Figma.jpg")
        img2 = img2.resize((120, 47), Image.ANTIALIAS)
        self.PhotoImage1 = ImageTk.PhotoImage(img2)
        b1 = Button(image=self.PhotoImage1,command=lambda: threading.Thread(target=self.Signin,daemon=True).start(),bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b1.place(x=709, y=517, width=120, height=47)

        #Forgot_Password_button_Image
        img3 = Image.open(r"JARVIS IMAGES\Forgot_Password_Figma.jpg")
        img3 = img3.resize((220, 22), Image.ANTIALIAS)
        self.PhotoImage3 = ImageTk.PhotoImage(img3)
        b2 = Button(command=self.Forgot_Password_User_1,image=self.PhotoImage3,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=660, y=592, width=220, height=22)

        #Signupbutton_Image
        img4 = Image.open(r"JARVIS IMAGES\Signup_Button_Figma.jpg")
        img4 = img4.resize((120, 46), Image.ANTIALIAS)
        self.PhotoImage4 = ImageTk.PhotoImage(img4)
        b3 = Button(command=self.Signup_user,image=self.PhotoImage4,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b3.place(x=815, y=648, width=120, height=46)

# Funcn Signup
    def Signup_user(self):
        self.new_win = Toplevel(self.root)
        self.app = Signup(self.new_win)

    # Funcn Signup
    def Forgot_Password_User_1(self):
        self.new_win = Toplevel(self.root)
        self.app = Forgot_Password_1(self.new_win)

    # Funcn Signin
    def Signin(self):
        try:
            if self.txtname.get() == "" or self.txtpass.get() == "":
                messagebox.showerror("Error", "All fields are required")
            else:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="inarr42712", database="jarvis_final", )
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from users where Name=%s and Password=%s",
                                (self.txtname.get(), self.txtpass.get()))
                row = my_cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Username and Password")
                else:
                    messagebox.showinfo("Successful Signed up","Welcome to jarvis AI Bot")
                    self.new_win = Toplevel(self.root)
                    self.app = Jarvis(self.new_win)
                conn.commit()
                conn.close()
        except:
                messagebox.showerror("Error", "Invalid Username")
#class Signup
class Signup:
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    def __init__(self,root):
        self.root=root
        self.root.title("Signup")
        self.root.geometry("1536x864+225+50")

        # variables

        self.var_Email = StringVar()
        self.var_Pass = StringVar()
        self.var_ConfirmPass = StringVar()
        self.var_Phone = StringVar()
        self.var_Name = StringVar()
        self.var_Check = IntVar()

    #background

        frame2=Frame(self.root,bg="black")
        frame2.place(x=0,y=0, width=1536, height=864)

        imgb = Image.open(r"JARVIS IMAGES\Signup_Window_Figma.png")
        imgb = imgb.resize((1536, 864), Image.ANTIALIAS)
        self.PhotoImageb = ImageTk.PhotoImage(imgb)
        lblimg6 = Label(frame2,image=self.PhotoImageb, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)


#Frmae
        Signupframe=Frame(self.root,bg="black")
        Signupframe.place(x=525,y=152, width=450, height=567)

    # AI_image
        img1 = Image.open(r"JARVIS IMAGES\Signup_Frame_Figma.png")
        img1 = img1.resize((450, 567), Image.ANTIALIAS)
        self.PhotoImage1 = ImageTk.PhotoImage(img1)
        lblimg6 = Label(Signupframe,image=self.PhotoImage1, borderwidth=0)
        lblimg6.place(x=0, y=0, relwidth=1, relheight=1)


        # #Email_Entry
        # self.txtname=Entry(Signupframe,font=("arial",12,),textvariable=self.var_Name,relief="flat")
        # self.txtname.place(x=27,y=118,width=250,height=20)

        #Email_Entry
        self.txtname=Entry(Signupframe,font=("arial",12,),textvariable=self.var_Name,relief="flat")
        self.txtname.place(x=27,y=198,width=270,height=25)

        #Password_Entry
        self.txtmail=Entry(Signupframe,font=("arial",12),textvariable=self.var_Email,relief="flat")
        self.txtmail.place(x=27,y=280,width=270,height=25)

        #ConfirmPassword_Entry
        self.txtpass=Entry(Signupframe,font=("arial",12),textvariable=self.var_Pass,relief="flat",show="*")
        self.txtpass.place(x=27,y=363,width=270,height=25)

        #Phone_Entry
        self.txtCnfm_pass=Entry(Signupframe,font=("arial",12),textvariable=self.var_ConfirmPass,relief="flat",show="*")
        self.txtCnfm_pass.place(x=27,y=445,width=270,height=25)



        #CheckButton
        self.CheckBtn=Checkbutton(Signupframe,variable=self.var_Check,font=("arial",9),relief="flat",text="By Clicking This I Agree To Terms And Conditions",onvalue=1,offvalue=0,fg="black",bg="white")
        self.CheckBtn.place(x=30,y=516,width=370,height=15)

        #Signupbutton_Image
        img4 = Image.open(r"JARVIS IMAGES\Signup_Button_Figma2.jpg")
        img4 = img4.resize((120, 47), Image.ANTIALIAS)
        self.PhotoImage4 = ImageTk.PhotoImage(img4)
        b4 = Button(Signupframe,image=self.PhotoImage4,command=self.SignUp_Data,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b4.place(x=314, y=97, width=120, height=47)

        #Backupbutton_Image
        img5 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img5 = img5.resize((70, 43), Image.ANTIALIAS)
        self.PhotoImage5 = ImageTk.PhotoImage(img5)
        b5 = Button(Signupframe,image=self.PhotoImage5,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Signup)
        b5.place(x=20, y=100, width=70, height=43)

    def SignUp_Data(self):
        self.Check_email()
        
        try:
            if self.var_Email.get() == "" or self.var_Pass.get() == "" or self.var_ConfirmPass.get() == "" or self.var_Name.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            elif self.var_Pass.get() != self.var_ConfirmPass.get():
                messagebox.showerror("Error", "Password and Confirm Password must be same")
            elif self.var_Check.get() == 0:
                messagebox.showerror("Error", "Please Click on the Checkbox")
            else:
                conn = mysql.connector.connect(
                host="localhost", user="root", password="inarr42712", database="jarvis_final",)
                my_cursor = conn.cursor()
                query = ("Select * from users where Email=%s")
                value = (self.var_Email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Email Address is already taken, please try with another Email Address")
                else:
                    my_cursor.execute("insert into users values(%s,%s,%s,%s)", (0,self.var_Name.get(),self.var_Email.get(), self.var_Pass.get(),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Successful Signed up","Welcome to jarvis AI Bot")
        except:
                messagebox.showerror("Error", " Username is already taken, please try another Username")


    # Funcn Signup
    def Signup_user(self):
        self.new_win = Toplevel(self.root)
        self.app = Signup(self.new_win)

    def Destroy_Signup(self):
        self.root.destroy()
    
    # Checking email validation
    def Check_email(self):
        if(re.search(Signup.regex, self.var_Email.get())):
            return
        else:
            messagebox.showerror("Error","Please enter a valid email",parent=self.root)

    

otp="100"
#Forgot_Password_Class
class Forgot_Password_1:
    Email="a"
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot_Password")
        self.root.geometry("1536x864+225+50")

        self.var_Email = StringVar()

        frame3=Frame(self.root,bg="black")
        frame3.place(x=0,y=0, relwidth=1, relheight=1)

    #background
        imgc = Image.open(r"JARVIS IMAGES\Forgot_Password_Figma1.png")
        imgc = imgc.resize((1536, 864), Image.ANTIALIAS)
        self.PhotoImagec = ImageTk.PhotoImage(imgc)
        lblimg6 = Label(frame3,image=self.PhotoImagec, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)


        Forgotframe=Frame(self.root,bg="black")
        Forgotframe.place(x=543,y=162, width=450, height=535)

        img7 = Image.open(r"JARVIS IMAGES\Forgot_Password_Frame_Figma1mod2.png")
        img7 = img7.resize((450, 535), Image.ANTIALIAS)
        self.PhotoImage7 = ImageTk.PhotoImage(img7)
        lblimg7 = Label(Forgotframe,image=self.PhotoImage7, borderwidth=0)
        lblimg7.place(x=0, y=0, width=450, height=535)

        #Email_Entry
        self.txtmail = Entry(Forgotframe, font=("ariel 13"), relief="flat",bd=2,textvariable=self.var_Email)
        self.txtmail.place(x=93,y=410,width=265,height=25)



        #Backupbutton_Image
        img5 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img5 = img5.resize((66, 43), Image.ANTIALIAS)
        self.PhotoImage5 = ImageTk.PhotoImage(img5)
        b2 = Button(Forgotframe,image=self.PhotoImage5,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Forgot_1)
        b2.place(x=22, y=100, width=66, height=43)

        img8 = Image.open(r"JARVIS IMAGES\SendOTP_Button_Figma.png")
        img8 = img8.resize((160, 42), Image.ANTIALIAS)
        self.PhotoImage8 = ImageTk.PhotoImage(img8)
        b2 = Button(Forgotframe,command=self.send,image=self.PhotoImage8,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=142, y=462, width=162, height=44)

    # Funcn Signup
    def Forgot_Password_User_2(self):
        self.new_win = Toplevel(self.root)
        self.app = Forgot_Password_2(self.new_win)





    def send(self):
        global otp
        try:
            # s = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is a port number
            # s.starttls()
            # s.login("jarvis.ai.bot2022@gmail.com", "jarvis@123")

            otp = random.randint(100000, 999999)
            otp = str(otp)
            conn = mysql.connector.connect(
            host="localhost", user="root", password="inarr42712", database="jarvis_final")
            my_cursor = conn.cursor()
            query = ("Select * from users where Email=%s")
            value = (self.var_Email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This Email doesn't exists",parent=self.root)
            else:

                conn.commit()
                conn.close()


                EMAIL_ADDRESS = "jarvis.ai.bot2022@gmail.com"
                EMAIL_PASSWORD = "jarvis@123"
                with open("my-new-message.html", "r", encoding='utf-8') as f:
                    text= f.read()
                msg = EmailMessage()
                text = text.replace("xxxxxx",otp)
                msg['Subject'] = 'Welcome to JARVIS'
                msg['From'] = "jarvis.ai.bot2022@gmail.com"
                msg['To'] = self.txtmail.get()

                msg.set_content('This is a plain text email')

                msg.add_alternative(text, subtype='html')


                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
                messagebox.showinfo("Send OTP via Email", f"OTP sent to {self.txtmail.get()}")
                self.new_win = Toplevel(self.root)
                self.app = Forgot_Password_2(self.new_win)
                #select Username,Password from Users where email = self.E.get()
                Forgot_Password_1.Email=self.txtmail.get()

        except Exception as e:
            print(e)
            messagebox.showerror("Send OTP via Email","Please enter the valid email address OR check an internet connection")

    def Destroy_Forgot_1(self):
        self.root.destroy()



#class Forgot_Password_Window2
class Forgot_Password_2:
    def __init__(self,root):
        self.root=root
        self.root.title("Forgot_Password")
        self.root.geometry("1536x864+225+50")
        self.image_captcha = ''

        self.ans = StringVar()
        self.ans1 = StringVar()
        self.generate_first_image()

        frame4=Frame(self.root,bg="black")
        frame4.place(x=0,y=0,relwidth=1,relheight=1)

    #background
        imgd = Image.open(r"JARVIS IMAGES\Forgot_Password_Figma2.png")
        imgd = imgd.resize((1536, 864), Image.ANTIALIAS)
        self.PhotoImaged = ImageTk.PhotoImage(imgd)
        lblimg6 = Label(frame4,image=self.PhotoImaged, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)


        Forgot2frame=Frame(self.root,bg="black")
        Forgot2frame.place(x=548,y=98, width=454, height=652)

        img7 = Image.open(r"JARVIS IMAGES\Forgot_Password_Frame_Figma2.png")
        img7 = img7.resize((454, 652), Image.ANTIALIAS)
        self.PhotoImage7 = ImageTk.PhotoImage(img7)
        lblimg7 = Label(Forgot2frame,image=self.PhotoImage7, borderwidth=0)
        lblimg7.place(x=0, y=0, width=454, height=652)

        #Captcha_Entry
        self.txtcap=Entry(Forgot2frame,textvariable=self.ans1,font=("arial",15),relief="flat")
        self.txtcap.place(x=134,y=326,width=180,height=30)

        #OTP_Entry
        self.txtotp=Entry(Forgot2frame,font=("arial",15),relief="flat")
        self.txtotp.place(x=134,y=510,width=180,height=30)

        #Backupbutton_Image
        img5 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img5 = img5.resize((66, 41), Image.ANTIALIAS)
        self.PhotoImage5 = ImageTk.PhotoImage(img5)
        b2 = Button(Forgot2frame,image=self.PhotoImage5,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Forgot_2)
        b2.place(x=12, y=74, width=66, height=41)

        img10 = Image.open(r"JARVIS IMAGES\ResendOTP_Button_Figma.png")
        img10 = img10.resize((135, 41), Image.ANTIALIAS)
        self.PhotoImage10 = ImageTk.PhotoImage(img10)
        b2 = Button(Forgot2frame,image=self.PhotoImage10,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=40, y=575, width=137, height=43)

        img11 = Image.open(r"JARVIS IMAGES\VerifyOTP_Button_Figma.png")
        img11 = img11.resize((121, 41), Image.ANTIALIAS)
        self.PhotoImage11 = ImageTk.PhotoImage(img11)
        b2 = Button(Forgot2frame,command=self.check_image_captcha,image=self.PhotoImage11,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=277, y=575, width=123, height=43)

        img12 = Image.open(r"JARVIS IMAGES\ShowCaptcha_Button_Figma.png")
        img12 = img12.resize((195, 45), Image.ANTIALIAS)
        self.PhotoImage12 = ImageTk.PhotoImage(img12)
        b2 = Button(Forgot2frame,command=self.generate_image_captcha,image=self.PhotoImage12,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=128, y=215, width=197, height=47)

        img13 = Image.open(r"JARVIS IMAGES\RegenerateCaptcha_Button_Figma.png")
        img13 = img13.resize((268, 48), Image.ANTIALIAS)
        self.PhotoImage13 = ImageTk.PhotoImage(img13)
        b2 = Button(Forgot2frame,command=self.regenerate_image_captcha,image=self.PhotoImage13,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=90, y=394, width=270, height=50)

        self.image_captcha = ''



    def generate_captcha(self):
        data_set = list(string.ascii_letters + string.digits)  # a-z,A-Z,0-9
        s = ''
        for i in range(6):
            a = random.choice(data_set)
            s = s + a
            data_set.remove(a)

        global image_captcha
        image_captcha = s

        print(s)
        return s


    def generate_digit_captcha(self):
        s1 = '';
        s = ''
        for i in range(4):
            a = str(random.randint(0, 9))
            s = s + a
            s1 = s1 + a + " "

        global audio_captcha
        audio_captcha = s

        return s1


    def generate_image_captcha(self):
        os.startfile('c1.png')


    def generate_first_image(self):
        img = ImageCaptcha()

        s = self.generate_captcha()
        # print(s)
        value = img.generate(s)
        img.write(s, "c1.png")


    def regenerate_image_captcha(self):
        img = ImageCaptcha()

        s = self.generate_captcha()
        # print(s)
        value = img.generate(s)
        img.write(s, "c1.png")
        os.startfile('c1.png')
        # print("Image Captcha Generated.\n\n")

    def get_image(self):
        return image_captcha

    def SendPassword(self):

        try:
            
            conn = mysql.connector.connect(host="localhost", user="root", password="inarr42712", database="jarvis_final")
            my_cursor = conn.cursor()
            query = ("Select Name,Password from users where Email=%s")
            value = (Forgot_Password_1.Email,)

            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            conn.commit()
            conn.close()

    
            EMAIL_ADDRESS = "jarvis.ai.bot2022@gmail.com"
            EMAIL_PASSWORD = "jarvis@123"
            with open("Cred.html", "r", encoding='utf-8') as f:
                text= f.read()
            msg = EmailMessage()
            text = text.replace("uuuuuu",row[0])
            text = text.replace("pppppp",row[1])
            msg['Subject'] = 'Login Credentials'
            msg['From'] = "jarvis.ai.bot2022@gmail.com"
            msg['To'] = Forgot_Password_1.Email

            msg.set_content('This is a plain text email')

            msg.add_alternative(text, subtype='html')


            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)




        except:
            messagebox.showerror("Password ot Sent","Please check your OTP and Captcha")

    def check_image_captcha(self):

         if  self.ans1.get() == self.get_image() and otp == self.txtotp.get():
            messagebox.showinfo("SUCCESS!", "Captcha Code and OTP Matched.")
            self.ans1.set("")
            self.SendPassword()

         else:
            messagebox.showerror("WRONG!", "Captcha Code does not Matched.")
            self.ans1.set("")

    def Destroy_Forgot_2(self):
        self.root.destroy()
#



#folder = 'C:\\Users\\skt\\Music\\YouTube\\'

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(audio):
    print('Jarvis:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        query=myCommand()


    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')

class Jarvis:
    def __init__(self,root):
        self.root=root
        self.root.title("J.A.R.V.I.S")
        self.root.geometry("1536x864+225+50")
        self.root.resizable(width=False, height=False)
        framej=Frame(self.root,bg="black")
        framej.place(x=0,y=0,relwidth=1,relheight=1)

        imgj = PIL.Image.open(r"JARVIS IMAGES\Jarvis_mainwindow_Figma.png")
        imgj = imgj.resize((1536, 864), PIL.Image.ANTIALIAS)
        self.PhotoImagej = ImageTk.PhotoImage(imgj)
        lblimg6 = Label(framej,image=self.PhotoImagej, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)


        frameog=Frame(self.root,bg="black")
        frameog.place(x=394,y=30,width=750,height=800)

        img17 = PIL.Image.open(r"JARVIS IMAGES\Jarvis_mainwindow_Frame_Figma.png")
        img17 = img17.resize((750, 800), PIL.Image.ANTIALIAS)
        self.PhotoImage17 = ImageTk.PhotoImage(img17)
        lblimg6 = Label(frameog,image=self.PhotoImage17, borderwidth=0)
        lblimg6.place(x=0, y=0, width=750, height=800)

        self.compText = StringVar()
        self.userText = StringVar()

        self.userText.set('Click \'Start Listening\' to Give commands')

        userFrame = Frame(self.root,bg="black")
        userFrame.place(x=465, y=166,width=580,height=241)

        usermsg = Message(userFrame, textvariable=self.userText, bg='black', fg='white')
        usermsg.config(font=("ariel", 12))
        usermsg.pack(fill='both', expand='yes')

        self.compFrame = Frame(self.root,bg="black")
        self.compFrame.place(x=465, y=480,width=580,height=241)
        self.lblimg1 = Label(self.compFrame,text="",bg="#131722",borderwidth=0)


        jarvismsg = Message(self.compFrame, textvariable=self.compText, bg='black', fg='white')
        jarvismsg.config(font=("ariel", 12))
        jarvismsg.pack(fill='both', expand='yes')

        img18 = PIL.Image.open(r"JARVIS IMAGES\Hamburger_Button_Figma.png")
        img18 = img18.resize((60, 60), PIL.Image.ANTIALIAS)
        self.PhotoImage18 = ImageTk.PhotoImage(img18)
        b2 = Button(frameog,command=self.Hamburger,image=self.PhotoImage18,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=653, y=16, width=60, height=60)

        img19 = PIL.Image.open(r"JARVIS IMAGES\StartListening_Button_Figma.png")
        img19 = img19.resize((256, 50), PIL.Image.ANTIALIAS)
        self.PhotoImage19 = ImageTk.PhotoImage(img19)
        b2 = Button(frameog,image=self.PhotoImage19,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=lambda: threading.Thread(target=self.clicked,daemon=True).start())
        b2.place(x=247, y=736, width=258, height=52)

        img20 = PIL.Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img20 = img20.resize((61, 42), PIL.Image.ANTIALIAS)
        self.PhotoImage20 = ImageTk.PhotoImage(img20)
        b2 = Button(frameog,image=self.PhotoImage20,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Jarvis_main)
        b2.place(x=43, y=25, width=61, height=42)

        speak('Hello, I am Jarvis! What should I do for You?')
        self.compText.set('Hello, I am Jarvis! What should I do for You?')

    def clicked(self):

        self.lblimg1.place_forget()
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
        import pywhatkit as kit
        if 'open cleaner' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'C:\Program Files\CCleaner\CCleaner.exe')

        elif "online music" in query:
            speak("sir what i have to search")
            m1 = myCommand()

            kit.playonyt(f"{m1}")

        elif "food" in query:
            speak("sir what i have to search")
            m1 = myCommand()
            kit.playonyt(f"{m1}")

        # elif 'open google chrome' in query:
        #     self.compText.set('okay')
        #     speak('okay')
        #     subprocess.call('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\chrome.exe')

        elif 'wish' in query :
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("Good Morning!")
                self.compText.set("Good Morning!")

            elif hour >= 12 and hour < 18:
                speak("Good Afternoon!")

            else:
                speak("Good Evening!")
                self.compText.set("Good Evening!")


        # elif "change window" in query or "switch window" in query:
        #     speak("Sir, till which window you have to swith")
        #     win=myCommand()0

        #     self.compText.set("Okay sir, Switching the window")
        #     for x in int (win):
        #         pyautogui.keyDown("alt")
        #         pyautogui.press("tab")
        #         time.sleep(1)
        #         pyautogui.keyUp("alt")
        #     self.userText.set("done sir")
        #     speak("done sir")


        elif 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            raw_data = urllib.request.urlopen(wikipedia.page(query).images[0]).read()
            logoimg = Image.open(io.BytesIO(raw_data))
            logoimg = logoimg.resize((120,120),Image.ANTIALIAS)
            self.photoimage1 = ImageTk.PhotoImage(logoimg)
            self.lblimg1 = Label(self.compFrame,image=self.photoimage1,bg="black",borderwidth=0)
            self.lblimg1.place(x=15,y=50,width=120,height=120)
            self.compText.set(results)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        elif 'open code' in query:
            self.compText.set('okay')
            speak('okay')
            subprocess.call(r'.JARVIS\steam.exe')

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        # elif 'open google' in query:
        #     self.compText.set('okay')
        #     speak('okay')
        #     webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            # self.compText.set("speak except @gmail.com")
            # speak('speak except gmail.com')
            recipient = myCommand().lower()
            self.userText.set(recipient)



            self.compText.set('What should I say?')
            speak('What should I say?')
            content = myCommand()
            time.sleep(10)
            self.userText.set(content)


            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login("jarvis.ai.bot2022@gmail.com", 'jarvis@123')
            conn=mysql.connector.connect(host="localhost",user="root",password="inarr42712",database="jarvis_final",)
            my_cursor=conn.cursor()
            query="""Select Email from add_friend where Name =%s """
            my_cursor.execute(query,(recipient,))
            row=my_cursor.fetchone()
            print(row)
            #for r1 in row:
            #   print(r1)
            conn.commit()

            x1=server.sendmail('jarvis.ai.bot2022@gmail.com', f"{row[0]}", content)
            print(x1)
            server.close()
            self.compText.set('Email sent!')
            speak('Email sent!')

                # creates SMTP session




        elif "jarvis" in query :
            app_id = wolframalpha.Client("5HHGU7-YHAJWXUTA8")
            try :
                self.compText.set("what is your query")
                speak("what is your query")
                logic1=myCommand().lower()
                self.userText.set(logic1)
                res=app_id.query(logic1)
                self.userText.set(next(res.results).text)
                speak(next(res.results).text)
            except Exception :
                self.userText.set("network error")

        elif "who are you" in query:
            print("hello")
            speak("Allow me to introduce myself,I am Jarvis, a virtual artificial intellegence and I am here to help you with the variety of task ,just click on Help section in Hamburger menu")
            self.compText.set("Allow me to introduce myself,I am Jarvis, a virtual artificial intellegence and I am here to help you with the variety of task ,just click on Help section in Hamburger menu")

        elif "latest news" in query:
            import requests
            # speak("what do I have to search")
            # ns=myCommand().lower()
            API_KEY = 'fb3a5891a786455bb898f36e92b09f24'

            params = {

                'q': "latest news" ,
                'source': 'bbc-news',
                'sortBy': 'top',
                'language': 'en',
                #'category': 'business',
                #'country': 'us',
                #'apiKey': API_KEY,
            }

            headers = {
                'X-Api-Key': API_KEY,  # KEY in header to hide it from url
            }

            url = 'https://newsapi.org/v2/top-headlines'

            response = requests.get(url, params=params, headers=headers)
            data = response.json()

            articles = data["articles"]
            
            results = [arr["title"] for arr in articles]

            for i, arr in enumerate(results, 1):
                print(i, arr)
            self.compText.set(results)

        elif "take screenshot" in query :
            self.compText.set("sir please tell me file name in which you have to save screenshot ")
            speak("sir please tell me file name in which you have to save screenshot ")
            ss=myCommand().lower()
            #self.userText(f"ss")
            speak("wait few seconds")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{ss}.png")
            speak("work done")

        elif "joke" in query:
            self.compText.set("ok sir telling jokes")
            speak("ok sir telling jokes")
            joke = pyjokes.get_joke()
            self.userText.set(f"joke")
            speak(joke)

        elif "send message" in query:
            speak("name of friend")
            self.compText.set("name of friend")
            s1=myCommand().lower()
            self.userText.set(s1)

            speak("message")
            self.compText.set("Message")
            s2=myCommand().lower()
            self.userText.set(s2)

            speak("Time in hours")
            self.compText.set("Time in hours")
            s3=myCommand().lower()
            self.userText.set(s3)
            speak("Time in minutes")
            self.compText.set("Time in minutes")
            s4=myCommand().lower()
            self.userText.set(s4)


            conn=mysql.connector.connect(host="localhost",user="root",password="inarr42712",database="jarvis_final",)
            my_cursor=conn.cursor()
            query="""Select Phone from add_friend where name =%s """
            my_cursor.execute(query,(s1,))
            row=my_cursor.fetchone()
            print(row)
            #for r1 in row:
            #   print(r1)
            conn.commit()

            while 1:
                try:
                    print(f"{row[0]}",f"{s2}",s3,s4)
                    kit.sendwhatmsg(f"{row[0]}",f"{s2}",int(s3),int(s4))
                    break
                except Exception as e:
                    print(e)
                    speak("Time in hours")
                    self.compText.set("Time in hours")
                    s3=myCommand().lower()
                    self.userText.set(s3)
                    speak("Time in minutes")
                    self.compText.set("Time in minutes")
                    s4=myCommand().lower()
                    self.userText.set(s4)
                    conn=mysql.connector.connect(host="localhost",user="root",password="inarr42712",database="jarvis_final",)
                    my_cursor=conn.cursor()
                    query="""Select Phone from add_friend where name =%s """
                    my_cursor.execute(query,(s1,))
                    row=my_cursor.fetchone()
                    print(row)
                    #for r1 in row:
                    #   print(r1)
                    conn.commit()



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            self.compText.set('Bye Sir, have a good day.')
            speak('Bye Sir, have a good day.')

        elif "read book" in query :
            book=open("cn.pdf",'rb')
            pdfReader=PyPDF2.PdfFileReader(book)
            pages=pdfReader.numPages
            self.compText.set(f"Total numbers of pages in this book {pages} ")
            speak(f"Total numbers of pages in this book {pages} ")
            speak("sir which page i have to read")
            reading_pg=myCommand().lower()
            self.userText.set(reading_pg)
            page=pdfReader.getPage(f"reading_pg")
            text=page.extractText()
            speak(text)
        elif 'hello' in query:
            self.compText.set('Hello Sir')
            speak('Hello Sir')

        elif 'open google' in query:
            speak("sir what i have to search")
            cm=myCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'news' in query:
            speak("sir what i have to search")
            cm=myCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'bye' in query:
            self.compText.set('Bye ' + 'Sir' + ', have a good day.')
            speak('Bye ' + 'Sir' + ', have a good day.')

        elif 'play music' in query:
            music_folder = 'C:\\Users\\skt\\Music\\YouTube\\'
            music = ['Edison', 'bensound-actionable', 'bensound-buddy', 'Micro', 'Lucid_Dreamer']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)

            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')


    # def Jarvis2_Destroy(self):
    #     self.new_win = Toplevel(self.root)
    #     self.app = Jarvis2(self.new_win)

    # def Jarvis(self):
    #     self.root.destroy()

    def Destroy_Jarvis_main(self):
        self.root.destroy()

    # Funcn Signup
    def Hamburger(self):
        self.new_win = Toplevel(self.root)
        self.app = Hamburger(self.new_win)


class Hamburger:
    def __init__(self,root):
        self.root=root
        self.root.title("Add Friend")
        self.root.geometry("1536x864+225+50")

        frameburger = Frame(self.root,bg="black")
        frameburger.place(x=0, y=0,relwidth=1,relheight=1)

        img21 = Image.open(r"JARVIS IMAGES\Hamburger_Window_Figma.png")
        img21 = img21.resize((1536, 864), Image.ANTIALIAS)
        self.photoimage21 = ImageTk.PhotoImage(img21)
        lbl= Label(frameburger,image=self.photoimage21,bg="black", borderwidth=0,activebackground="black")
        lbl.place(x=0, y=0, width=1536, height=864)


        img22 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img22 = img22.resize((70, 44), Image.ANTIALIAS)
        self.photoimage22 = ImageTk.PhotoImage(img22)
        b2 = Button(frameburger,image=self.photoimage22,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Hamburger)
        b2.place(x=456, y=156, width=70, height=44)

        img23 = Image.open(r"JARVIS IMAGES\Help_Button_Figma.png")
        img23 = img23.resize((100, 45), Image.ANTIALIAS)
        self.photoimage23 = ImageTk.PhotoImage(img23)
        b2 = Button(frameburger,command=self.Helpwin,image=self.photoimage23,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=523, y=284, width=102, height=47)

        img24 = Image.open(r"JARVIS IMAGES\AddFriends_Hamburger_Button_Figma.png")
        img24 = img24.resize((200, 45), Image.ANTIALIAS)
        self.photoimage24= ImageTk.PhotoImage(img24)
        b2 = Button(frameburger,command=self.Addfriends,image=self.photoimage24,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=842, y=457, width=202, height=47)

        img25 = Image.open(r"JARVIS IMAGES\Feedback_Button_Figma.png")
        img25 = img25.resize((162, 45), Image.ANTIALIAS)
        self.photoimage25 = ImageTk.PhotoImage(img25)
        b2 = Button(frameburger,image=self.photoimage25,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Feedbackwin)
        b2.place(x=504, y=634, width=164, height=47)

    def Destroy_Hamburger(self):
        self.root.destroy()

    def Feedbackwin(self):
        self.new_win = Toplevel(self.root)
        self.app = Feedback(self.new_win)

    # Funcn Signup
    def Addfriends(self):
        self.new_win = Toplevel(self.root)
        self.app = Add_Friend(self.new_win)

    def Helpwin(self):
        self.new_win = Toplevel(self.root)
        self.app = Help(self.new_win)

class Add_Friend:
    valid_p=False
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    def __init__(self,root):
        self.root=root
        self.root.title("Add Friend")
        self.root.geometry("1536x864+225+50")

        self.var_Name=StringVar()
        self.var_Email=StringVar()
        self.var_Phone=StringVar()

        frame6=Frame(self.root,bg="black")
        frame6.place(x=0,y=0,relwidth=1,relheight=1)

        imgd = Image.open(r"JARVIS IMAGES\AddFriend_Window_Figma.png")
        imgd = imgd.resize((1536, 864), Image.ANTIALIAS)
        self.PhotoImaged = ImageTk.PhotoImage(imgd)
        lblimg6 = Label(frame6,image=self.PhotoImaged, borderwidth=0)
        lblimg6.place(x=0, y=0, width=1536, height=864)


        AddFriendFrame=Frame(self.root,bg="black")
        AddFriendFrame.place(x=548,y=152,width=440,height=560)

        img14 = Image.open(r"JARVIS IMAGES\AddFriend_Frame_Figma.png")
        img14 = img14.resize((440, 560), Image.ANTIALIAS)
        self.PhotoImage14 = ImageTk.PhotoImage(img14)
        lblimg6 = Label(AddFriendFrame,image=self.PhotoImage14, borderwidth=0)
        lblimg6.place(x=0, y=0, width=440, height=560)

        #OTP_Entry
        self.name=Entry(AddFriendFrame,textvariable=self.var_Name,font=("arial",13),relief="flat")
        self.name.place(x=65,y=224,width=270,height=20)

        #OTP_Entry
        self.phone=Entry(AddFriendFrame,textvariable=self.var_Phone,font=("arial",13),relief="flat")
        self.phone.place(x=65,y=311,width=270,height=20)

        #OTP_Entry
        self.txtmail=Entry(AddFriendFrame,textvariable=self.var_Email,font=("arial",13),relief="flat")
        self.txtmail.place(x=65,y=396,width=270,height=20)

        img15 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img15 = img15.resize((66, 41), Image.ANTIALIAS)
        self.PhotoImage15 = ImageTk.PhotoImage(img15)
        b2 = Button(AddFriendFrame,image=self.PhotoImage15,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Add_Friend)
        b2.place(x=14, y=83, width=66, height=41)

        img16 = Image.open(r"JARVIS IMAGES\AddFriend_Button_Figma.png")
        img16 = img16.resize((187, 45), Image.ANTIALIAS)
        self.PhotoImage16 = ImageTk.PhotoImage(img16)
        b2 = Button(AddFriendFrame,command=self.AddFriend_Data,image=self.PhotoImage16,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=126, y=476, width=189, height=47)



    def AddFriend_Data(self):
        if self.Check_phone_number() =="a" or self.Check_email()== "a" :
            return
        elif self.Check_phone_number() =="a" and self.Check_email()== "a" :
            return

        if self.var_Name.get()=="":
            messagebox.showerror("Error","Enter your Username",parent=self.root)

            if self.var_Email.get()=="":
               messagebox.showerror("Error","Enter your Email Address",parent=self.root)

            elif  self.var_Phone.get()=="":
                messagebox.showerror("Error","Enter your Phone Number",parent=self.root)

            else:
                messagebox.showerror("Error","All fields are required",parent=self.root)
                
        elif len(self.var_Name.get())>=3 and len(self.var_Name.get())>=20:
            messagebox.showerror("Error","Name should be between 3 to 20 chararcters")
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="inarr42712" ,database="jarvis_final",auth_plugin = 'mysql_native_password',)
            my_cursor=conn.cursor()
            query=("Select * from add_friend where Phone=%s")
            value=(self.var_Phone.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Phone no. already exists, please try another phone no.")
            else:
                my_cursor.execute("insert into add_friend values(%s,%s,%s)",(self.var_Name.get(),self.var_Email.get(),self.var_Phone.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Successfully added friend ","Added Friend Successflly")
            self.new_win = Toplevel(self.root)
            self.app = Hamburger(self.new_win)

    def Destroy_Add_Friend(self):
        self.root.destroy()

    # Checking email validation
    def Check_email(self):
        if(re.search(Add_Friend.regex, self.var_Email.get())):
            return 
        else:
            messagebox.showerror("Error","Please enter a valid email",parent=self.root)
            return "a"

    # Checking phone number validation
    def Check_phone_number(self):
        try:
            number=str(self.var_Phone.get())
            print(number)
            Add_Friend.valid_p=phonenumbers.is_valid_number(phonenumbers.parse(number))
            print(Add_Friend.valid_p)
        except phonenumbers.NumberParseException:
            messagebox.showerror("Error","Enter a valid phone number!",parent=self.root)
            return "a"

class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback")
        self.root.geometry("1536x864+225+50")

        self.var_Email = StringVar()
        self.INPUT = StringVar()

        feedframe=Frame(self.root,bg="black")
        feedframe.place(x=0,y=0,relwidth=1,relheight=1)

        img26 = Image.open(r"JARVIS IMAGES\Feedback_Window_Figma.png")
        img26 = img26.resize((1536, 864), Image.ANTIALIAS)
        self.photoimage26 = ImageTk.PhotoImage(img26)
        lbl= Label(feedframe,image=self.photoimage26,bg="black", borderwidth=0,activebackground="black")
        lbl.place(x=0, y=0, width=1536, height=864)

        self.txtmail=Entry(feedframe,font=("arial",12),relief="flat",textvariable=self.var_Email)
        self.txtmail.place(x=495,y=375,width=270,height=25)

        # self.txtfed=Entry(feedframe,font=("arial",12,),relief="flat")
        # self.txtfed.place(x=480,y=475,width=580,height=160)

        self.com = Text(feedframe, width=30, height=4,font=("ariel",13),relief="flat")
        self.com.grid(row=3, column=0, columnspan=2)
        self.com.place(x=500,y=475)
        self.com.config(wrap ='word')

        img27 = Image.open(r"JARVIS IMAGES\SubmitFeedback_Button_Figma.png")
        img27= img27.resize((265, 45), Image.ANTIALIAS)
        self.photoimage27 = ImageTk.PhotoImage(img27)
        b2 = Button(feedframe,command=self.Feedback,image=self.photoimage27,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=636, y=668, width=265, height=45)

        img28 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img28 = img28.resize((66, 41), Image.ANTIALIAS)
        self.PhotoImage28 = ImageTk.PhotoImage(img28)
        b2 = Button(feedframe,image=self.PhotoImage28,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Feedback)
        b2.place(x=14, y=83, width=66, height=41)


    def Feedback(self):
        if self.var_Email.get()=="":
            messagebox.showerror("Error","All fields are required")

        else:
                conn=mysql.connector.connect(host="localhost",user="root",password="inarr42712",database="jarvis_final",auth_plugin='mysql_native_password',)
                my_cursor=conn.cursor()
                query=("Select * from feedback where Email=%s")
                value=(self.var_Email.get(),)
                value1= self.com.get("1.0", "end-1c")
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showwarning("Error","You have been already commented")
                else:
                    my_cursor.execute("insert into feedback values(%s,%s)",(self.var_Email.get(),value1,))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Great","Thankyou")

    def Destroy_Feedback(self):
        self.root.destroy()

engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak2(audio):
    print('Jarvis:', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.setProperty("rate",100)
    engine.say(audio)
    engine.runAndWait()


def myCommand2():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Try again')
        query=myCommand2()


    return query



class Help:
    def __init__(self,root):
        self.root=root
        self.root.title("Feedback")
        self.root.geometry("1536x864+225+50")

        helpframe=Frame(self.root,bg="black")
        helpframe.place(x=0,y=0,relwidth=1,relheight=1)

        img29 = Image.open(r"JARVIS IMAGES\Help_Window_Figma.png")
        img29 = img29.resize((1536, 864), Image.ANTIALIAS)
        self.photoimage29 = ImageTk.PhotoImage(img29)
        lbl= Label(helpframe,image=self.photoimage29,bg="black", borderwidth=0,activebackground="black")
        lbl.place(x=0, y=0, width=1536, height=864)

        help2frame=Frame(self.root,bg="black")
        help2frame.place(x=417,y=85,width=674,height=647)

        

        img31 = Image.open(r"JARVIS IMAGES\Help_Window_Frame_Figma.png")
        img31 = img31.resize((674, 647), Image.ANTIALIAS)
        self.photoimage31 = ImageTk.PhotoImage(img31)
        lbl= Label(help2frame,image=self.photoimage31,bg="black", borderwidth=0,activebackground="black")
        lbl.place(x=0, y=0, width=674, height=647)

        img30 = Image.open(r"JARVIS IMAGES\Back_Button_Figma.jpg")
        img30 = img30.resize((70, 44), Image.ANTIALIAS)
        self.PhotoImage30 = ImageTk.PhotoImage(img30)
        b2 = Button(help2frame,image=self.PhotoImage30,bg="black", borderwidth=0, cursor="hand2",activebackground="black",command=self.Destroy_Help)
        b2.place(x=35, y=26, width=70, height=44)

        img32 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img32= img32.resize((20, 20), Image.ANTIALIAS)
        self.photoimage32 = ImageTk.PhotoImage(img32)
        b2 = Button(help2frame,command=self.b1,image=self.photoimage32,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=124, width=20, height=20)

        img33 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img33= img33.resize((20, 20), Image.ANTIALIAS)
        self.photoimage33 = ImageTk.PhotoImage(img33)
        b2 = Button(help2frame,command=self.b2,image=self.photoimage33,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=175, width=20, height=20)

        img34 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img34= img34.resize((20, 20), Image.ANTIALIAS)
        self.photoimage34 = ImageTk.PhotoImage(img34)
        b2 = Button(help2frame,command=self.b3,image=self.photoimage34,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=223, width=20, height=20)

        img35 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img35= img35.resize((20, 20), Image.ANTIALIAS)
        self.photoimage35 = ImageTk.PhotoImage(img35)
        b2 = Button(help2frame,command=self.b4,image=self.photoimage35,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=295, width=20, height=20)

        img36 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img36= img36.resize((20, 20), Image.ANTIALIAS)
        self.photoimage36 = ImageTk.PhotoImage(img36)
        b2 = Button(help2frame,command=self.b5,image=self.photoimage36,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=347, width=20, height=20)

        img37 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img37= img37.resize((20, 20), Image.ANTIALIAS)
        self.photoimage37 = ImageTk.PhotoImage(img37)
        b2 = Button(help2frame,command=self.b6,image=self.photoimage37,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=398, width=20, height=20)

        img38 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img38= img38.resize((20, 20), Image.ANTIALIAS)
        self.photoimage38 = ImageTk.PhotoImage(img38)
        b2 = Button(help2frame,command=self.b7,image=self.photoimage38,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=449, width=20, height=20)

        img39 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img39= img39.resize((20, 20), Image.ANTIALIAS)
        self.photoimage39 = ImageTk.PhotoImage(img39)
        b2 = Button(help2frame,command=self.b8,image=self.photoimage39,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=500, width=20, height=20)

        img40 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img40= img40.resize((20, 20), Image.ANTIALIAS)
        self.photoimage40 = ImageTk.PhotoImage(img40)
        b2 = Button(help2frame,command=self.b9,image=self.photoimage40,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=548, width=20, height=20)

        img41 = Image.open(r"JARVIS IMAGES\Help_MIC.png")
        img41= img41.resize((20, 20), Image.ANTIALIAS)
        self.photoimage41 = ImageTk.PhotoImage(img41)
        b2 = Button(help2frame,command=self.b10,image=self.photoimage41,bg="black", borderwidth=0, cursor="hand2",activebackground="black")
        b2.place(x=576, y=596, width=20, height=20)

    def b1(self):
        speak2("jarvis")
    
    def b2(self):
        speak2("online music")

    def b3(self):
        speak2("open google")

    def b4(self):
        speak2("Wikipedia on")

    def b5(self):
        speak2("send messege")

    def b6(self):
        speak2("email")

    def b7(self):
        speak2("open youtube")

    def b8(self):
        speak2("latest news")

    def b9(self):
        speak2("food")

    def b10(self):
        speak2("jarvis and then temperature on")

    def Destroy_Help(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

