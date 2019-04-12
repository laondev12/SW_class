"""
reference
https://m.blog.naver.com/PostView.nhn?blogId=noxburn&logNo=220989147307&proxyReferer=https%3A%2F%2Fwww.google.com%2F
"""

# Vcc --> 5V
# Trig --> GPIO 2
# Echo --> GPIO 3
# GND --> GND


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 2
echo = 3

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    while True:
        GPIO.output(trig, False)
        time.sleep(0.5)

        GPIO.output(trig, True)
        #time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
	        pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()
		
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)
	
        print("distance :", distance, "cm")
	
except KeyboardInterrupt:
    GPIO.cleanup()


