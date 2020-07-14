import pyfirmata
import time
import win32com.client
import speech_recognition as sr
speaker = win32com.client.Dispatch("SAPI.SpVoice",userName="Female")
r = sr.Recognizer()
import tkinter
from tkinter import*
#import serial

board = pyfirmata.Arduino('COM3')
tk = Tk()
tk.geometry("400x400")

def batDen():
    speaker.Speak("moi ban noi bat den")
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)
            audio = r.recognize_google(audio, language='vi-VN')
        print(audio)
        if(audio != " "):
            if(audio == "bật đèn"):
                board.digital[5].write(1)
            elif(audio == "Tắt Đèn"):
                board.digital[5].write(0)
            else:
                speaker.Speak("mời nói lại")
        else:
            speaker.Speak("Mời bạn nói lại")
        # if(0xFF == ord('q')):
        #     break
def tatDen():
    board.digital[5].write(0)

Btn_chayhet = Button(tk, text = "Bật đèn", font =("Time New Roman", 14), bg = "green", command = batDen)
Btn_chayhet.place(x=200, y=200)
Btn_tathet = Button(tk, text = "Tắt đèn", font =("Time New Roman", 14), bg = "green", command = tatDen)
Btn_tathet.place(x=200, y=260)
    
tk.mainloop()