# CircutPython

### Description
I wrote this code an eterity ago, with an incredibly out of date metro express (version 2.1.4) im still in amazment and bewilderment that this worked at some point. but after i updated my board it stopped working. so  ¯ \_(ツ)_/¯.
### Evidense

```python
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

print("Make it red!")

while True:
     dot.fill((100,0,0))
     time.sleep(100)
     dot.fill((100,0,0))
     time.sleep(100)
```
# CircutPython Servo
### Description
hank helped me write his code in my time of need.  basically when, when i touch either A4 or A5, my finger will send a current and the servo will switch direction, depending on which way its spinning. https://github.com/hdpow/CircutPython
### Evidence
```python
import board
import time
import servo
import pulseio
import touchio

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
 
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

# create a Cap Touch value
touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)

while True:
    print("ITS WORKING! ITS WORKING!")
    if touch_A4.value:
        my_servo.angle = 0
        print("diddled A4!")
    if touch_A5.value:
        my_servo.angle = 180
        print("diddled A5!")
    time.sleep(0.05)
```

### Images
https://mail.google.com/mail/u/0?ui=2&ik=7570d4066c&attid=0.1&permmsgid=msg-a:r-5730145700624361546&th=1772aa7454c10aa1&view=att&disp=safe&realattid=1772aa67656ebf9fdc91

# Circuit python LCD
### description
in this assignment we were instructed to make an LCD display a increment that would go up or down in value using Touch.io wires.  My code was heavily inspired by Alden dents code with a few changes. Aldens cod had the LCD constantly updateing its display, which created a few problems; it would constantly be blinking making the display hard to read, and the value wouldnt show its display imidiatly, you had to wait for the LCD to finish updateing.  So I made the LCD only update when I pressed one of the Wires, which is much more pleasing to look at.  I also trimmed a lot of the fat off of aldens code, the only part of this code thats entirly his is the logic.  https://github.com/adent11/CircuitPython

### Evidense
```python 
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


  ```

### images
    
<img src="/20210524_110610.jpg" >
20210524_110700_1.mp4


