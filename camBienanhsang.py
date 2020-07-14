import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:0:i')

while True:
    analog_value = analog_input.read()
    print(analog_value)
    time.sleep(0.1)
    if(analog_value == None):
        pass
    elif(analog_value > 0.6):
        board.digital[13].write(1)
    else:
        board.digital[13].write(0)