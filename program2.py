import RPi.GPIO as GPIO
import time

LED = 15
SW = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT, initial=0)

start = time.time()
ledState = False
nextTime = start

f = open("data.txt", "w")

try:
        while time.time() - start < 10:
                now = time.time()
                sw = GPIO.input(SW)

                if sw == 0:
                        interval = 1.0
                else:
                        interval = 2.0


                if now >= nextTime:
                        ledState = not ledState
                        GPIO.output(LED, ledState)
                        f.write(f"{now - start:.3f}\t{'on' if sw else 'off'}\n")
                        nextTime = now + interval

                time.sleep(0.01)
finally:
    f.close()
    GPIO.cleanup()
