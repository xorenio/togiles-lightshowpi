##!/usr/bin/env python3
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import time
import RPi.GPIO as GPIO
import subprocess
import os
from gpiozero import LED
red_led = LED(20)
green_led = LED(26)
blue_led = LED(6)
yellow_led = LED(5)
GPIO.setmode(GPIO.BCM)

# GPIO 21 set up as input. It is pulled up to stop false signals
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO 20 set up as output.
GPIO. setup(20, GPIO.OUT)
# GPIO 16 set up as output.
GPIO. setup(16, GPIO.OUT)
# GPIO 19 set up as output.
GPIO. setup(19, GPIO.OUT)
# GPIO 26 set up as output.
GPIO. setup(26, GPIO.OUT)
# GPIO 6 set up as output
GPIO. setup(6, GPIO.OUT)
# GPIO 6 set up as output
GPIO. setup(5, GPIO.OUT)
# GPIO 13 set up as output
GPIO. setup(13, GPIO.OUT)

## START TEST
#
#
# $ (mpg123 -q "Serenity-1130896858.mp3" &) && sleep $(soxi -D "Serenity-1130896858.mp3") && killall mpg123
# Make\ Way\ for\ Noddy.mp3
os.system('mpg123 -q Make\ Way\ for\ Noddy.mp3 &') ## Play sound
os.system('sleep $(soxi -D Make\ Way\ for\ Noddy.mp3) && killall mpg123 &') ## sleep for length of sound then kill mpg123
subprocess.call("sudo python synchronized_lights.py --file=/home/pi/lightshowpi/py/Make\ Way\ for\ Noddy.mp3", shell=True)

#
#
## END TEST
