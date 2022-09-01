#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import subprocess

GPIO.setmode(GPIO.BCM)

# GPIO 21 set up as input. It is pulled up to stop false signals
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# init list with pin numbers

pinList = [5, 6, 13, 16, 19, 20, 26]

# loop through pins and set mode and state to 'low'

for h in pinList:
    GPIO.setup(h, GPIO.OUT)
    GPIO.output(h, GPIO.HIGH)

# time to sleep between operations

SleepTimeL = 2


# main loop
# gpio 13 to turn switch light on
GPIO.output(13, 1)



try:

  for i in range(1, 100, +1): # loop counter

# gpio 13 to turn switch light on
    GPIO.output(13, 1)   

    GPIO.wait_for_edge(21, GPIO.FALLING)
    print ("\nFalling edge detected. Now your program can continue with pushing pinochios nose out.")
    # os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/SHREK-theme song.mp3" &')
    # subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/SHREK-theme song.mp3"', shell=True)

# gpio 13 to turn switch light off
    GPIO.output(13, 0)


# gpio 5 to push out pinochios nose
    GPIO.output(5, 0)
    print ("pinochios nose")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Do You Know the Muffin Man Scene.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Do You Know the Muffin Man Scene.mp3"', shell=True)

    time.sleep(1)
    GPIO.output(5, 1)

# gpio 13 to turn switch light on
    GPIO.output(13, 1)

    GPIO.wait_for_edge(21, GPIO.FALLING)
    print ("\nFalling edge detected. Now your program can continue with turning fionias head.")

# gpio 13 to turn switch light off
    GPIO.output(13, 0)

# gpio 6 to turn fionias head
    GPIO.output(6, 0)
    print ("fionas head")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Fiona changing into Orge.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Fiona changing into Orge.mp3"', shell=True)

    time.sleep(1)
    GPIO.output(6, 1)

# gpio 13 to turn switch light on
    GPIO.output(13, 1)

    GPIO.wait_for_edge(21, GPIO.FALLING)
    print ("\nFalling edge detected. Now your program can continue with shreks fart.")

# gpio 13 to turn switch light off
    GPIO.output(13, 0)

# gpio 20 shreks fart
    GPIO.output(20, 0)
    print ("shreks fart")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Better out than in, I always say..mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Better out than in, I always say..mp3"', shell=True)

    time.sleep(1);
    GPIO.output(20, 1)

# gpio 13 to turn switch light on
    GPIO.output(13, 1)

    GPIO.wait_for_edge(21, GPIO.FALLING)
    print ("\nFalling edge detected. Now your program can continue with donkey flying")

# gpio 13 to turn switch light off
    GPIO.output(13, 0)

# gpio 26 flying donkey
    GPIO.output(26, 0)
    print ("flying donkey")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Donkey talks and flies.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Donkey talks and flies.mp3"', shell=True)

    time.sleep(1);
    GPIO.output(26, 1)

# gpio 13 to turn switch light on
    GPIO.output(13, 1)

    GPIO.wait_for_edge(21, GPIO.FALLING)
    print ("\nFalling edge detected. Now your program can continue with dragon smoke")

# gpio 13 to turn switch light off
    GPIO.output(13, 0)

# gpio 19 dragon smoke
    GPIO.output(19, 0)
    print ("dragon smoke")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Accidentally in Love song.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Accidentally in Love song.mp3"', shell=True)

    time.sleep(1);
    GPIO.output(19, 1)



    print ((i))

  


# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()



