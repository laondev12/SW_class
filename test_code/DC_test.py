import RPi.GPIO as GPIO
import sys
import time
import numpy as np

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

        self.state = 0
        self.velocity = 0
        self.accel_raw_x = np.zeros([1,10])
        self.accel_raw_y = np.zeros([1,10])
        self.accel_raw_z = np.zeros([1,10])
        self.gyro_raw_x = np.zeros([1,10])
        self.gyro_raw_y = np.zeros([1,10])
        self.gyro_raw_z = np.zeros([1,10])

        self.accel_x = 0
        self.accel_y = 0
        self.accel_z = 0
        self.gyro_x = 0
        self.gyro_y = 0
        self.gyro_z = 0


    def forward(self, speed):

        print('forward')

        GPIO.output(pin2, False)
        GPIO.output(pin4, False)

        pwm1.start(speed)
        pwm3.start(speed)

    def stop(self):

        print('stop')

        GPIO.output(pin1, False)
        GPIO.output(pin2, False)
        GPIO.output(pin3, False)
        GPIO.output(pin4, False)
		
    def backward(self, speed):

        print('backward')

        GPIO.output(pin1, False)
        GPIO.output(pin3, False)
		
        pwm2.start(speed)
        pwm4.start(speed)

    def right(self):

        print('right')

        GPIO.output(pin2, False)
        GPIO.output(pin4, False)
		
        pwm1.start(30)
        pwm3.start(60)

    def left(self):

        print('left')

        GPIO.output(pin2, False)
        GPIO.output(pin4, False)
		
        pwm1.start(60)
        pwm3.start(30)

    def speed_up(self, speed):

        print('speed up')

        GPIO.output(pin2, False)
        GPIO.output(pin4, False)

        pwm1.ChangeDutyCycle(speed)
        pwm3.ChangeDutyCycle(speed)
		
    def slow_down(self, speed):

        print('slow_down')

        GPIO.output(pin2, False)
        GPIO.output(pin4, False)

        pwm1.ChangeDutyCycle(speed)
        pwm3.ChangeDutyCycle(speed)



if __name__ == "__main__":

    RC_CAR = RC_CAR()

    try:
        while True:
            RC_CAR.forward(70)
            RC_CAR.stop()
            RC_CAR.backward(70)
            RC_CAR.stop()
            RC_CAR.right()
            RC_CAR.stop()
            RC_CAR.left()
            RC_CAR.stop()
            RC_CAR.forward(60)
            RC_CAR.speed_up(100)
            RC_CAR.slow_down(40)
            RC_CAR.stop()

    except KeyboardInterrupt:
        pwm1.stop()
        GPIO.cleanup()
        sys.exit()
