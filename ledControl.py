import pyfirmata
import time
import tkinter
from tkinter import*

board = pyfirmata.Arduino('COM3')
tk = Tk()
tk.geometry("400x400")
def tathet():
    for i in range(2,14,1):
        board.digital[i].write(0)
def kieuNhapNhay():
    n = 0
    while n < 5:
        for i in range(2,14,1):
            board.digital[i].write(0)
            time.sleep(0.1)
            board.digital[i].write(1)
            time.sleep(0.1)
        n = n+1
        
def chayTraiPhai():
    n = 0
    while n < 5:
        chay = 2
        for i in range(2,14,1):
            for i in range(2,14,1):
                board.digital[i].write(0)
            board.digital[chay].write(1)
            time.sleep(0.1)
            chay = chay+1
            if(chay>13):
                chay = 2
        n = n + 1
    board.digital[13].write(0)    
def chayPhaiTrai():
    n = 0
    while n < 5:
        chay = 13
        for i in range(2,14,1):
            for i in range(2,14,1):
                board.digital[i].write(0)
            board.digital[chay].write(1)
            time.sleep(0.1)
            chay = chay-1
            if(chay<2):
                chay = 13
        n = n + 1
    board.digital[2].write(0)  
def chayTrongngoai():
    n = 0 
    while n<5:
        for i in range(2,14,1):
            board.digital[i].write(0)
        time.sleep(0.1)
        board.digital[7].write(1)
        board.digital[8].write(1)
        time.sleep(0.1)
        board.digital[6].write(1)
        board.digital[9].write(1)
        time.sleep(0.1)
        board.digital[5].write(1)
        board.digital[10].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[11].write(1)
        time.sleep(0.1)
        board.digital[3].write(1)
        board.digital[12].write(1)
        time.sleep(0.1)
        board.digital[2].write(1)
        board.digital[13].write(1)
        time.sleep(0.1)
        n= n+1 
def chayDontraiphai():
    n = 0
    while n < 5:
        chay = 13
        for i in range(2,14,1):
            board.digital[chay].write(0)
            time.sleep(0.1)
            chay = chay-1
            if(chay<2):
                chay = 13
        for i in range(2,14,1):
            board.digital[chay].write(1)
            time.sleep(0.1)
            chay = chay-1
            if(chay<2):
                chay = 13       
        n = n+1
    for i in range(2,14,1):
        board.digital[i].write(0)
def chayDonphaitrai():
    n = 0
    while n < 5:
        for i in range(2,14,1):
            board.digital[i].write(0)
            time.sleep(0.1)
        for i in range(2,14,1):
            board.digital[i].write(1)
            time.sleep(0.1)
        n = n+1  
    for i in range(2,14,1):
        board.digital[i].write(0)

def chayDonvaotrong():
    n = 0 
    while n<5:
        for i in range(2,14,1):
            board.digital[i].write(0)
        time.sleep(0.1)
        board.digital[2].write(1)
        board.digital[13].write(1)
        time.sleep(0.1)
        board.digital[3].write(1)
        board.digital[12].write(1)
        time.sleep(0.1)
        board.digital[4].write(1)
        board.digital[11].write(1)
        time.sleep(0.1)
        board.digital[5].write(1)
        board.digital[10].write(1)
        time.sleep(0.1)
        board.digital[6].write(1)
        board.digital[9].write(1)
        time.sleep(0.1)
        board.digital[7].write(1)
        board.digital[8].write(1)
        time.sleep(0.1)
        n= n+1 
def chayhet():
    for i in range(2,14,1):
        board.digital[i].write(1)


Btn11 = Button(tk, text = "Kiểu nhấp nháy", font =("Time New Roman", 14), bg = "green", command = kieuNhapNhay)
Btn11.place(x=10, y=20)
Btn12 = Button(tk, text = "Chạy trái phải", font =("Time New Roman", 14), bg = "green", command = chayTraiPhai)
Btn12.place(x=10, y=80)
Btn13 = Button(tk, text = "Chạy phải trái", font =("Time New Roman", 14), bg = "green", command = chayPhaiTrai)
Btn13.place(x=10, y=140)
Btn14 = Button(tk, text = "Chạy dồn ra ngoài", font =("Time New Roman", 14), bg = "green", command = chayTrongngoai)
Btn14.place(x=10, y=200)
Btn14 = Button(tk, text = "Chạy dồn trái phải", font =("Time New Roman", 14), bg = "green", command = chayDontraiphai)
Btn14.place(x=10, y=260)
Btn14 = Button(tk, text = "Chạy dồn phải trái", font =("Time New Roman", 14), bg = "green", command = chayDonphaitrai)
Btn14.place(x=200, y=140)
Btn14 = Button(tk, text = "Chạy dồn vào trong", font =("Time New Roman", 14), bg = "green", command = chayDonvaotrong)
Btn14.place(x=200, y=80)
Btn_chayhet = Button(tk, text = "Bật sáng hết", font =("Time New Roman", 14), bg = "green", command = chayhet)
Btn_chayhet.place(x=200, y=200)
Btn_tathet = Button(tk, text = "Tắt đèn led", font =("Time New Roman", 14), bg = "green", command = tathet)
Btn_tathet.place(x=200, y=260)
    
tk.mainloop()