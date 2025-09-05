import RPi.GPIO as GPIO
import time

LED = 11
SW = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=0)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

start = time.time()
ledState = False
nextTime = start

f = open("data.txt", "w")

try:
    while time.time() - start < 10:
        now = time.time()
        sw = GPIO.input(SW)

        if sw == 1:      
            GPIO.output(LED,GPIO.HIGH)
        else:
            GPIO.output(LED,GPIO.LOW)

        if now >= nextTime:
            ledState = not ledState
            GPIO.output(LED, ledState)
            f.write(f"{now - start:.3f}\t{'on' if sw else 'off'}\n")
            nextTime = now

        time.sleep(0.01)
finally:
    f.close()
    GPIO.cleanup()
