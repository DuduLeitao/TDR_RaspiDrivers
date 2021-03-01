#!/usr/bin python3

# This code detects when the gate is closed/opened using a button that is
# pressed in one case and not prressed in the other.

# Import libraries
import RPi.GPIO as GPIO
import time
import requests
import json

# Variable declaration
button_pin = 36
flag_button_event = 0
url = 'http://localhost'
headers = {'content-type': 'application/json'}

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin,GPIO.IN)

# This function is called whenever an event is detected in the button.
def eventDetected(button_pin):
	global flag_button_event
	if(GPIO.input(button_pin) == GPIO.LOW and flag_button_event == 0):
		payload = {"user":"Gate","type":"command","value":"open"}
		flag_button_event = 1
		response = requests.post(url, data=json.dumps(payload), headers=headers)
		print("Gate closed")
		#print(response.text)
	elif(GPIO.input(button_pin) == GPIO.HIGH  and flag_button_event == 1):
		payload = {"user":"Gate","type":"command","value":"close"}
		flag_button_event = 0
		response = requests.post(url, data=json.dumps(payload), headers=headers)
		print("Gate opened")
		#print(response.text)

# Configure interruption
GPIO.add_event_detect(button_pin, GPIO.BOTH)  # Add rising/falling edge detection on a channel
GPIO.add_event_callback(button_pin, eventDetected) # Call "event_detected" function when an event is det$

# Loop forever
while True:
	time.sleep(3600*24)

GPIO.cleanup()
