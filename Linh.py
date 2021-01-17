import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
     
def chayTraiPhai():
    n = 0
    while n < 3:
        chay = 2
        for i in range(2,7,1):
            for i in range(2,7,1):
                board.digital[i].write(0)
            board.digital[chay].write(1)
            time.sleep(0.2)
            chay = chay+1
            if(chay>6):
                chay = 2
        n = n + 1
    #board.digital[13].write(0)    
def chayPhaiTrai():
    n = 0
    while n < 3:
        chay = 6
        for i in range(2,7,1):
            for i in range(2,7,1):
                board.digital[i].write(0)
            board.digital[chay].write(1)
            time.sleep(0.2)
            chay = chay-1
            if(chay<2):
                chay = 6
        n = n + 1
    #board.digital[2].write(0)  
 
def chayDontraiphai():
    n = 0
    while n < 3:
        chay = 6
        for i in range(2,7,1):
            board.digital[chay].write(0)
            time.sleep(0.2)
            chay = chay-1
            if(chay<2):
                chay = 6
        for i in range(2,7,1):
            board.digital[chay].write(1)
            time.sleep(0.2)
            chay = chay-1
            if(chay<2):
                chay = 6       
        n = n+1
    for i in range(2,7,1):
        board.digital[i].write(0)
def chayDonphaitrai():
    n = 0
    while n < 3:
        for i in range(2,7,1):
            board.digital[i].write(0)
            time.sleep(0.2)
        for i in range(2,7,1):
            board.digital[i].write(1)
            time.sleep(0.2)
        n = n+1  
    for i in range(2,7,1):
        board.digital[i].write(0)

def chayhet():
    for i in range(2,14,1):
        board.digital[i].write(1)

def tongHop():
    m = 0
    while m < 5:
        chayDonphaitrai()
        chayDontraiphai()
        chayPhaiTrai()
        chayTraiPhai()
        chayhet()
        m = m+1

tongHop()
   