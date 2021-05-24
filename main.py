
import time
import board
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)

switch = touchio.TouchIn(board.A0)
button = touchio.TouchIn(board.A5)

change = 1
value = 0

stopper1 = False
stopper2 = False

while True:
    if switch.value and not stopper1:
        lcd.clear()
        stopper1 = True
        value = value + change


    if not switch.value:

        stopper1 = False


    if button.value and not stopper2:
        lcd.clear()
        stopper2 = True
        value = value - change


    if not button.value:

        stopper2 = False


    time.sleep(.1)



    lcd.set_cursor_pos(0,0)
    lcd.print('Increment ' + str(change))
    lcd.set_cursor_pos(1,0)
    lcd.print('Value ' + str(value))

    #Prints the increment and value to the serial monitor
    print('Increment ' + str(change))
    print('Value ' + str(value))
    time.sleep(.1)