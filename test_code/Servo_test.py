"""
Reference
https://ljs93kr.tistory.com/40
"""



# Orange = PWM Pin --> GPIO 18
# Red = Vcc --> 5V
# Brown = GND --> GND
#
# You need to install "GPIO.PRi" library
#
# $ sudo apt-get update
# $ sudo apt-get install python-rpi.gpio


import RPi.GPIO as GPIO
import time

pin = 18 # PWM pin num 18

GPIO.setmode(GPIO.BCM)
gpio.setup(pin, GPIO.OUT)
servo = GPIO.PWM(pin, 50)
servo.start()

try:
    while True:
        servo.ChangeDutyCycle(1)
        print("angle: 1")
        time.sleep(1)
        servo.ChangeDutyCycle(1)
        print("angle: 1")
        time.sleep(1)
        servo.ChangeDutyCycle(1)
        print("angle: 1")
        time.sleep(1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()



