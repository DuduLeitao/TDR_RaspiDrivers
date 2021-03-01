#!/usr/bin/env python3

# This code uses the webcam to take a picture of the front gate area
import time
import os
from datetime import datetime, timedelta

#os.system('fswebcam --no-banner --greyscale -r 640x480 --jpeg 50 --save /home/pi/CamPics/%Y-%m-%d_%H-%M-%S.jpg')
os.system('fswebcam -r 640x480 -S 10 --jpeg 50 --save /var/www/tdr/backend/campic.jpg')
