from pyfirmata import Arduino, util
import time
a = 0 + 1
board = Arduino("COM3")

while True:
    board.digital[13].write(a)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
