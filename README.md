# CircuitPython.
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
    print("This works!")
    if touch_A4.value:
        my_servo.angle = 0
        print("Touched A4!")
    if touch_A5.value:
        my_servo.angle = 180
        print("Touched A5!")
    time.sleep(0.05)
