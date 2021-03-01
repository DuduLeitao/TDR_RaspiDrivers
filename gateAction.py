#!/usr/bin/env python3

# Import libraries.
import RPi.GPIO as GPIO
import time

# Variable declaration.
relay_pin = 37
activation_time = .5

# GPIO configuration.
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)

# Activation of the relay.
GPIO.output(relay_pin,GPIO.HIGH)
time.sleep(activation_time)
GPIO.output(relay_pin,GPIO.LOW)
GPIO.cleanup()
