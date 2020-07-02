import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

while True:
    for i in range(2,6,1):
        board.digital[i].write(1)
    time.sleep(10)
    for i in range(2,6,1):
        board.digital[i].write(0)
    for i in range(6,10,1):
        board.digital[i].write(1)
    time.sleep(15)
    for i in range(6,10,1):
        board.digital[i].write(0)
    for i in range(10,14,1):
        board.digital[i].write(1)
    time.sleep(5)
    for i in range(10,14,1):
        board.digital[i].write(0)