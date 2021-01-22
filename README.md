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

