from time import sleep
from pyfirmata import Arduino, util, SERVO

board = Arduino('COM4', 9600)
sleep(5)
board.digital[3].mode = SERVO
def servo(posiciones):
    board.digital[3].write(posiciones)

while True:
    posiciones = input("Angulo")
    servo(posiciones)