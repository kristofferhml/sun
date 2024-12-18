import RPi.GPIO as GPIO

class Lamp():
    def __init__(self, PIN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.HIGH)
        self.current = GPIO.HIGH
        self.PIN = PIN
        
    def light(self):
        if self.current == GPIO.LOW:
            return
       
        GPIO.output(self.PIN, GPIO.LOW)
        self.current = GPIO.LOW

    def dark(self):
        if self.current == GPIO.HIGH:
            return
        
        GPIO.output(self.PIN, GPIO.HIGH)
        self.current = GPIO.HIGH
       
    def shutdown(self):
        GPIO.cleanup()