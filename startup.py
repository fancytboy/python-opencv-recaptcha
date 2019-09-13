import os
import sys
import cv2
import random
import webbrowser

import numpy as np
import tkinter as tk
import tkinter.messagebox as tkMessageBox

from tkinter import *
from tkinter import ttk 
from threading import Timer
from PIL import Image, ImageTk
from datetime import datetime

class Gif(Label):
    def __init__(self, master, image=None, height=None , width=None):
        im = Image.open(image)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0], bg='white', height=10)

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        

class GUI:
    def remove(self, element, pl=True):
        if not pl:
            element.pack_forget()
        else:
            element.place_forget()

    def add(self, element, **kwargs):
        element.place(**kwargs)

class ApplicationSelfDefinedClass:

    def exit(self):
        confirm = tkMessageBox.askyesno("Exit Application", "Are you sure you want to quit?")
        if confirm:
            print("Exiting application... " , datetime.now())
            root.quit()
            os._exit(0)
    
    def restart(self):
        print ("Restarting application..." , datetime.now())
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

class WebCaptchaSelfDefinedClass:

    def __init__(self , cap=None):
        self.t = None
        self.cap = cap

    def open(self):
        interface = GUI()
        self.cap.release()
        cv2.destroyAllWindows()

        new=2
        url='file://' + os.path.realpath('resources/index.html')
        webbrowser.open(url, new=new)
        interface.remove(isWorking)
        interface.add(isSuccess, x=20, y=20)
        print("Open webpage")

    def start(self, d=5):
        if not self.t:
            print("Timer initialized")
            gesture_status.config(text="Detected.. Please hold still" , width="100", fg='green', font=Trebuchet9bold)
            gesture_status.update_idletasks()
            self.t = Timer(d , self.open)
            self.t.start()
    
    def stop(self):
        if self.t and self.t.is_alive():
            print("Timer is cancelled")
            gesture_status.config(text="Not detected..." , width="100", fg='red', font=Trebuchet9bold)
            gesture_status.update_idletasks()
            self.t.cancel()
            self.t = None

class CaptchaGestureSelfDefinedClass:

    # Gesture 1
    # Nose detection
    # Make sure your nose is detected for 5 seconds
    def nose_detection(self):
        
        # Display gesture instruction to user
        tkMessageBox.showinfo("Gesture Request ", "Move your face to the camera and make sure your nose is not covered")
        
        # Load the nose detection classifier
        detector2= cv2.CascadeClassifier('bin/haarcascade_mcs_nose.xml')

        # Start the video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite Loop
        while(True):
            ret2, img2 = cap.read()
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            faces2 = detector2.detectMultiScale(gray2, 1.3, 5)
            if(len(faces2)!=0):
                for (x,y,w,h) in faces2:
                    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
                    t.start()
            else:
                t.stop()
                    
            cv2.imshow('frame',img2)

            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    # Gesture 2
    # Eye detection
    # Stare at the screen for 5 seconds 
    def eye_detection(self):
    
        # Display gesture instruction to user
        tkMessageBox.showinfo("Gesture Request", "Keep your eyes open for 5 seconds")
        
        # Load eye detection classifier
        detector3= cv2.CascadeClassifier('bin/haarcascade_mcs_lefteye.xml')
        
        # Start the video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite Loop
        while(True):
            ret2, img2 = cap.read()
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            faces2 = detector3.detectMultiScale(gray2, 1.3, 5)
            if(len(faces2)!=0):
                for (x,y,w,h) in faces2:
                    cv2.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
                    t.start()
            else:
                t.stop()
            
            cv2.imshow('frame',img2)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    # Gesture 3
    # Mouth detection
    def mouth_detection(self):

        # Display gesture instruction to user
        tkMessageBox.showinfo("Gesture Request", "Smile at the camera")

        # Load mouth detection classifier
        detector5= cv2.CascadeClassifier('bin/haarcascade_mcs_mouth.xml')
        
        # Start the video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite loop
        while(True):
            ret5, img5 = cap.read()
            gray = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
            faces5 = detector5.detectMultiScale(gray, 1.3, 5)
            if(len(faces5)!=0):
                for (x,y,w,h) in faces5:
                    cv2.rectangle(img5,(x,y),(x+w,y+h),(0,255,0),2)
                    t.start()
            else:
                t.stop()
        
            cv2.imshow('frame',img5)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    # Gesture 4
    # Face detection
    def face_detection(self):
        
        # Display gesture insturction to user
        tkMessageBox.showinfo("Gesture Request", "Stare at the camera for 5 seconds")

        # Load face detection classifier
        detector6= cv2.CascadeClassifier('bin/haarcascade_frontalface_default.xml')
        
        # Start video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite loop
        while(True):
            ret6, img6 = cap.read()
            gray = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
            faces6 = detector6.detectMultiScale(gray, 1.3, 5)
            if(len(faces6)!=0):
                for (x,y,w,h) in faces6:
                    cv2.rectangle(img6,(x,y),(x+w,y+h),(0,255,0),1)
                    t.start()
            else:
                t.stop()
        
            cv2.imshow('frame',img6)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    # Gesture 5
    # Face and Nose detection          
    def face_and_nose_detection(self):

        face, nose = None, None

        # Display gesture instruction to user
        tkMessageBox.showinfo("Gesture Request", "Align your face to the camera till box boxes appear then keep still for 3 seconds")

        # Load face detection classifier
        detector7= cv2.CascadeClassifier('bin/haarcascade_frontalface_default.xml')

        # Load nose detection classifier
        detector8= cv2.CascadeClassifier('bin/haarcascade_mcs_nose.xml')

        # Start video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an infinite loop
        while(True):
            ret7, img7 = cap.read()
            gray = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
            faces7 = detector7.detectMultiScale(gray, 1.3, 5)
            if(len(faces7)!=0):
                for (x,y,w,h) in faces7:
                    cv2.rectangle(img7,(x,y),(x+w,y+h),(255,0,0),2)
                    face = True
            else:
                face = False
        
            cv2.imshow('frame',img7)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                break
            
            ret8, img8 = cap.read()
            gray = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)
            faces8 = detector8.detectMultiScale(gray, 1.3, 5)
            if(len(faces8)!=0):
                for (x,y,w,h) in faces8:
                    cv2.rectangle(img8,(x,y),(x+w,y+h),(0,255,0),1)
                    nose = True
            else:
                nose = False
        
            cv2.imshow('frame',img8)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                break             
            
                cap.release()
                cv2.destroyAllWindows()

            if face and nose:
                t.start(2)
            else:
                t.stop()

    # Gesture 6
    # Fist detection
    # Hold your fist up for 5 seconds
    def fist_detection(self):
        
        # Display gesture insturction to user
        tkMessageBox.showinfo("Gesture Request", "Hold your fist to the camera")

        # Load face detection classifier
        detector6= cv2.CascadeClassifier('bin/haarcascade_a_gfist.xml')
        
        # Start video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite loop
        while(True):
            ret6, img6 = cap.read()
            faces6 = detector6.detectMultiScale(img6, 1.3, 5)
            if(len(faces6)!=0):
                for (x,y,w,h) in faces6:
                    cv2.rectangle(img6,(x,y),(x+w,y+h),(0,255,0),2)
                    t.start(2)
            else:
                t.stop()
        
            cv2.imshow('frame',img6)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    # Gesture 7
    # Palm detection
    # Spread your palm and face it to the camera for 5 seconds
    def palm_detection(self):
        
        # Display gesture insturction to user
        tkMessageBox.showinfo("Gesture Request", "Spread your palm and face it to the camera")

        # Load face detection classifier
        detector6= cv2.CascadeClassifier('bin/haarcascade_palm_v4.xml')
        
        # Start video capture
        cap = cv2.VideoCapture(0)

        # Create an instacnce of WebCaptchaSelfDefinedClass
        t = WebCaptchaSelfDefinedClass(cap)

        # Create an Infinite loop
        while(True):
            ret6, img6 = cap.read()
            faces6 = detector6.detectMultiScale(img6, 1.3, 5)
            if(len(faces6)!=0):
                for (x,y,w,h) in faces6:
                    cv2.rectangle(img6,(x,y),(x+w,y+h),(0,255,0),2)
                    t.start(2)
            else:
                t.stop()
        
            cv2.imshow('frame',img6)
            if cv2.waitKey(1) & 0xFF == ord('a'):
                cap.release()
                cv2.destroyAllWindows()

    def pickRandomGesture(self):
        classMethods = [i for i in dir(self) if not i.startswith('__') and not i.endswith('__')]
        classMethods.remove('pickRandomGesture')
        selected = random.choice(classMethods)
        print("[Running 0]:", selected)
        getattr(self, selected)()

class Captcha:
    def __init__(self):
        # Instatiate the Captcha Gesture class::
        self.gesture = CaptchaGestureSelfDefinedClass()

        # Instatiate the GUI class::
        self.interface = GUI()  

    def __begin__(self):
        # Remove the captcha box
        self.interface.remove(CaptchaCheckBox, False)

        # Show is working loader
        self.interface.add(isWorking, x=10, y=8, height=60, width=60)

        # Pick a random gesture
        self.gesture.pickRandomGesture()

# Instatiate the Captcha class::
captcha = Captcha()

# Instatiate the ApplicationSelfDefinedClass class::
Application = ApplicationSelfDefinedClass()

# Define fonts
robo9 = ("roboto", 9)
robo11 = ("roboto", 11)
robo14 = ("Roboto", 12)
helv11 = ('helvetica', 11)
abadi12b = ('Trebuchet MS', 11)
Trebuchet9bold = ('Trebuchet MS', 9 , 'bold')

# Instatiate the Tkiter GUI class
root = Tk()

# Set the window title
root.title("Face Detection reCAPTCHA")

# Set window size
root.geometry('350x200+30+30')

# Set window and app icon
root.iconbitmap('resources/logo_xbM_icon.ico')

# Load ReCaptcha Image
# Resize image to 60x60
reCaptchaImage = ImageTk.PhotoImage(Image.open('resources/recaptcha.png').resize((60, 60),Image.ANTIALIAS))

# Create a frame for the captcha
# Other elements can be added to a frame
CaptchaFrame = Frame(root, bg='white', bd=1, relief=SUNKEN, height='78', width='304')
CaptchaFrame.pack(pady=10)
CaptchaFrame.pack_propagate(False)

# Add Captcha Image to Captcha Frame
CaptchaImageLabel = Label(CaptchaFrame, image=reCaptchaImage, bg="white", height='60', width='60').place(x=230, y=5)

# Load image for captcha isWorking state
isWorking = Gif(CaptchaFrame, image='resources/ajax-loader.gif')

# Load image for captcha isSuccess state
isSuccessImage = ImageTk.PhotoImage(Image.open('resources/tick.png').resize((30, 30), Image.ANTIALIAS))
isSuccess = Label(CaptchaFrame , image=isSuccessImage, bg='white')

# Add Captcha Checkbox to Captcha Frame
ttk.Style().configure("TButton", padding=4, relief="flat",background="#fff")
CaptchaCheckBox = ttk.Checkbutton(CaptchaFrame, style='TButton', width=3, command=captcha.__begin__)
CaptchaCheckBox.pack(side='left', padx=(20,25))

# Add 'I am not a robot' Label
CaptchaLabel = Label(CaptchaFrame, text='I\'m not a robot', bg='white', font=abadi12b).place(x=70, y=23)

# Create the application Menubar
menubar = Menu(root)

# Add the file submenu to the Menu bar
filemenu = Menu(menubar , tearoff=0, font=robo9)
filemenu.add_command(label="Restart", command=Application.restart)
filemenu.add_separator()
# filemenu.add_checkbutton(label="Status")
# filemenu.add_separator()
filemenu.add_command(label="Exit", command=Application.exit)
menubar.add_cascade(label="Options", menu=filemenu)

# Create a label to show the gesture status
gesture_status = Label(root, text="Waiting..." )
gesture_status.pack()

#Add the menu bar to the root
root.config(menu=menubar)

# Display the window
root.mainloop()
