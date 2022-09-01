#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import os
import subprocess

## ADDED FOR RANDOM FUNCTIONS
from random import randrange


# SET PIN MODE
GPIO.setmode(GPIO.BCM)


# GPIO 21 set up as input. It is pulled up to stop false signals
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# INIT LIST WITH PIN NUMBERS
pinList = [5, 6, 13, 16, 19, 20, 26]


# LOOP THROUGH PINS TO SET MODE AND STATE TO LOW
for h in pinList:
    GPIO.setup(h, GPIO.OUT)
    GPIO.output(h, GPIO.HIGH)


# DEFINE TIME TO SLEEP (UN-USED)
SleepTimeL = 2



## VARS FOR ACTION SELECTOR
last_action_number = -1
current_action_number = -1



## START OF FLASHING LIGHT ACTIONS

def turn_off_switch_light():
    GPIO.output(13, 0)

def turn_on_switch_light():
    GPIO.output(13, 1)

## END OF FLASHING LIGHT ACTIONS



## START OF PINOCHOIS NOSE ACTIONS

def push_out_pinochios_nose():
    GPIO.output(5, 0)

def pull_in_pinochios_nose():
    GPIO.output(5, 1)

## END OF PINOCHOIS NOSE ACTIONS



## START OF ACTION RUNNER

def run_current_action():
  last_action_number = current_action_number
  if current_action_number == 0:
    
    # gpio 5 to PUSH OUT pinochios nose
    push_out_pinochios_nose()

    print ("pinochios nose")
    
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Do You Know the Muffin Man Scene.mp3" &')
    
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Do You Know the Muffin Man Scene.mp3"', shell=True)

    time.sleep(1)
    
    # gpio 5 to PULL IN pinochios nose
    pull_in_pinochios_nose()


  elif current_action_number == 1:
    # gpio 6 to turn fionias head
    GPIO.output(6, 0)
    print ("fionas head")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Fiona changing into Orge.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Fiona changing into Orge.mp3"', shell=True)

    time.sleep(1)
    GPIO.output(6, 1)

  elif current_action_number == 2:
    # gpio 20 shreks fart
    GPIO.output(20, 0)
    print ("shreks fart")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Better out than in, I always say..mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Better out than in, I always say..mp3"', shell=True)

    time.sleep(1);
    GPIO.output(20, 1)
  elif current_action_number == 3:

    # gpio 26 flying donkey
    GPIO.output(26, 0)
    print ("flying donkey")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Donkey talks and flies.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Donkey talks and flies.mp3"', shell=True)

    time.sleep(1);
    GPIO.output(26, 1)

  elif current_action_number == 4:
    # gpio 19 dragon smoke
    GPIO.output(19, 0)
    print ("dragon smoke")
    os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/Accidentally in Love song.mp3" &')
    subprocess.call('sudo python synchronized_lights.py --file="/home/pi/lightshowpi/py/Shrek/soundtracks/Accidentally in Love song.mp3"', shell=True)

    time.sleep(1);
    GPIO.output(19, 1)

## END OF ACTION RUNNER



## START OF ACTION SELECTOR
def run_action_selector():

  # STOP ANY PAST PLAYS
  os.system('killall mpg123')
  # TURN FLASHING LIGHT ON 
  turn_on_switch_light()
  
  # PLAY THEME 
  os.system('mpg123 -q "/home/pi/lightshowpi/py/Shrek/soundtracks/SHREK-theme song.mp3" &')
  
  # WAIT FOR RED BUTTON PRESS 
  GPIO.wait_for_edge(21, GPIO.FALLING)

  # ECHO TO USER 
  print ("\nFalling edge detected. Now your program can continue with pushing pinochios nose out.")

  # STOP PLAYING THEME 
  os.system('killall mpg123')

  # TURN FLASHING LIGHT OFF 
  turn_off_switch_light()

  # GENERATE RANDOM NUMBER 0 TO 4 == 5
  current_action_number=random.randint(0, 4);

  # COMPARE TO LAST NUMBER
  if last_action_number == current_action_number:
    # RUN THIS FUNCTION AGAIN TO GET NEW ACTION
    run_action_selector()
    # RETURN TO STOP FUNCTION
    # return
  else;
    # RUN THE CURRENT ACTIONS NUMBER
    run_current_action()

## END OF ACTION SELECTOR


## START OF SCRIPT RUN TIME
try:

  for i in range(1, 100, +1): # loop counter
    

    run_action_selector();

    time.sleep(2)

    print ((i))

## END OF SCRIPT RUN TIME


# End program cleanly with keyboard
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
