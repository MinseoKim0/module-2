import RPi.GPIO as GPIO
import argparse  
from time import sleep    
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BOARD)  

parser = argparse.ArgumentParser(description='Data for this program.')
parser.add_argument('--n', action='store', type=int, default=5,
                    help='time for program to run in seconds')
args = parser.parse_args()

ITER_COUNT = args.n 
pin1 = 11

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

while ITER_COUNT > 0: 
   ITER_COUNT -= 1 
   GPIO.output(pin1, GPIO.HIGH) 
   sleep(1)                     
   GPIO.output(pin1, GPIO.LOW)  
   sleep(1)            
GPIO.cleanup()

