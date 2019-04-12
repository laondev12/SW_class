import RPi.GPIO as GPIO
import sys
import time
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin1 = 23	# GPIO pin number
pin2 = 24
pin3 = 22
pin4 = 27

GPIO.setup(pin1, GPIO.OUT)	# Set GPIO pin as OUTPUT
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

"""
pwm1 = GPIO.PWM(pin1, 100)	# Use PWM to control the speed of DC_Motor
pwm1.start(50)				# Start the Motor
"""

pwm1 = GPIO.PWM(pin1, 100)		# GPIO.PWM([pin],[frequency])
pwm2 = GPIO.PWM(pin2, 100)		# GPIO.PWM([pin],[frequency])
pwm3 = GPIO.PWM(pin3, 100)		# GPIO.PWM([pin],[frequency])
pwm4 = GPIO.PWM(pin4, 100)		# GPIO.PWM([pin],[frequency])



class RC_CAR:

    def __init__(self):
        print('Ready!!')


    def forward(self, speed):

        print('forward')

        #GPIO.output(pin2, False)
        #GPIO.output(pin4, False)
        pwm2.stop()
        pwm4.stop()
        pwm1.start(speed)
        pwm3.start(speed)

    def stop(self):

        print('stop')
	
        pwm1.stop()
        pwm2.stop()
        pwm3.stop()
        pwm4.stop()
		
    def backward(self, speed):

        print('backward')

        pwm1.stop()
        pwm3.stop()
        pwm2.start(speed)
        pwm4.start(speed)

    def right(self):

        print('right')

        pwm2.stop()
        pwm4.stop()
        pwm1.start(60)
        pwm3.start(100)

    def left(self):

        print('left')

        pwm2.stop()
        pwm4.stop()
        pwm1.start(100)
        pwm3.start(50)

    def speed_up(self, speed):

        print('speed up')

        pwm2.stop()
        pwm4.stop()
        pwm1.ChangeDutyCycle(speed)
        pwm3.ChangeDutyCycle(speed)
		
    def slow_down(self, speed):

        print('slow_down')

        pwm2.stop()
        pwm4.stop()
        pwm1.ChangeDutyCycle(speed)
        pwm3.ChangeDutyCycle(speed)



if __name__ == "__main__":

    RC_CAR = RC_CAR()

    try:
        while True:
            RC_CAR.forward(70)
            time.sleep(3)

            RC_CAR.stop()
            time.sleep(1)

            RC_CAR.backward(70)
            time.sleep(3)

            RC_CAR.stop()
            time.sleep(1)

            RC_CAR.right()
            time.sleep(3)

            RC_CAR.stop()
            time.sleep(1)

            RC_CAR.left()
            time.sleep(3)

            RC_CAR.stop()
            time.sleep(1)

            RC_CAR.forward(70)
            time.sleep(3)
            RC_CAR.speed_up(100)
            time.sleep(3)
            RC_CAR.slow_down(40)
            time.sleep(3)

            RC_CAR.stop()
            time.sleep(1)

    except KeyboardInterrupt:
        pwm1.stop()
        GPIO.cleanup()
        sys.exit()
