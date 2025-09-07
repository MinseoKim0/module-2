import RPi.GPIO as GPIO
import time
import argparse
from time import sleep

LED = 15
SW = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial=0)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

parser = argparse.ArgumentParser(description='Data for this program.')
parser.add_argument('--tim', action='store', type=int, default=10,
                    help='time for program to run in seconds')
parser.add_argument('--delay', action='store', type=float, default=1.0,
                    help='time in between messages')
parser.add_argument('--debug', action='store_true', 
                    help='specifies if debug statements are printed')
parser.add_argument('--write', action='store_true', 
                    help='accept a command line argument write to the file')
args = parser.parse_args()

start = time.time()
ledState = False
nextTime = start

f = open("data.txt", "w")

try:
    while time.time() - start < args.tim:
        now = time.time()
        sw = GPIO.input(SW)

        if sw == 0:
            GPIO.output(LED, GPIO.LOW)
            sleep(args.delay)
        else:
            GPIO.output(LED, GPIO.LOW)
            sleep(args.delay)
            GPIO.output(LED, GPIO.HIGH)
            sleep(args.delay)

        if args.debug:
            print(f'{now:.3f}\t{"on" if sw else "off"}')

        if args.write:
            f.write(f'{now:.3f}\t{"on" if sw else "off"}\n')

        time.sleep(0.01)
finally:
       f.close()
       GPIO.cleanup()
