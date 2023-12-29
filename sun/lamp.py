import RPi.GPIO as GPIO

PIN = 14

class Lamp():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.HIGH)
        
    def light(self):
        GPIO.output(PIN, GPIO.LOW)

    def dark(self):
        GPIO.output(PIN, GPIO.HIGH)
       
    def shutdown(self):
        GPIO.cleanup()