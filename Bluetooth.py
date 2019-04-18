############################################
# You need to install packages before getting started
# $ sudo apt-get update
# $ sudo apt-get upgrade
# $ sudo apt-get install bluetooth blueman bluez
# $ sudo reboot
#
# $ sudo apt-get install python-bluetooth
# $ sudo apt-get install python-rpi.gpio
#
### procedures below is execute in terminal 
# $ sudo bluetoothctl
#
# you need to check all the commands of bluetoothctl
# after bluetooth is ON
# enter commands below
#
# [bluetooth]# power on
# [bluetooth]# agent on
# [bluetooth]# discoverable on
# [bluetooth]# pairable on
# [bluetooth]# scan on
#
# After "scan on" you will see your Bluetooth device in the list,
# then using command below to pair to your phone.
# [bluetooth]# pair <MAC address of your phone>

### if you use VNC viewer, pair device by bluetooth icon.

############################################

import RPi.GPIO as GPIO
import bluetooth
import time



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
pwm1.stop()                 # Stop the Motor
"""

pwm1 = GPIO.PWM(pin1, 100)		# GPIO.PWM([pin],[frequency])
pwm2 = GPIO.PWM(pin2, 100)		# GPIO.PWM([pin],[frequency])
pwm3 = GPIO.PWM(pin3, 100)		# GPIO.PWM([pin],[frequency])
pwm4 = GPIO.PWM(pin4, 100)		# GPIO.PWM([pin],[frequency])




# Creating socket for Bluetooth RFCOMM communication
server_socket=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1

# Server binds the script on host to port
server_socket.bind(("",port))

# Server listens to accept one connection at a time
server_socket.listen(1)

# Server accepts client's connection request and assign the
# mac address to the variable address, client_socket is the client's socket
client_socket, address = server_socket.accept()
print("Accepted connection from", address)

input = ""


class RC_CAR():

    def __init__(self):
        print('Ready!!')

    def forward(self, speed):

        print('forward')

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
        pwm1.start(70)
        pwm3.start(100)

    def left(self):

        print('left')

        pwm2.stop()
        pwm4.stop()
        pwm1.start(100)
        pwm3.start(70)
    """
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
    """

RC_CAR = RC_CAR()

while True:
    input = client_socket.recv(1024)
    print("Received: %s" % input)

    if (input == "f"):
        RC_CAR.forward()

    elif (input == "b"):
        RC_CAR.backward()

    elif (input == "l"):
        RC_CAR.left()

    elif (input == "r"):
        RC_CAR.right()

    elif (input == "s"):
        RC_CAR.stop()

    elif (input == "q"):
        print("Quit")
        break

client_socket.close()
server_socket.close()
GPIO.cleanup()
sys.exit()
