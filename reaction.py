import RPi.GPIO as GPIO
import time
import random

left_name = raw_input('left player name is: ')
rigth_name = raw_input('rigth player name is: ')

names = [left_name,rigth_name]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
rigth_button = 15
left_button = 14


GPIO.setup(led,GPIO.OUT)
GPIO.setup(rigth_button,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(left_button,GPIO.IN,GPIO.PUD_UP)


GPIO.output(led,1)

time.sleep(random.uniform(5,10))

GPIO.output(led,0)

while True:
  if GPIO.input(left_button) == False:
    print(names[0] + " won")
    break
  if GPIO.input(rigth_button) == False:
    print(names[1] + " won")
    break


GPIO.cleanup()
