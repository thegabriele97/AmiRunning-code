from Adafruit_MotorShield import Adafruit_MotorShield
from Adafruit_StepperMotor import Adafruit_StepperMotor
import time

# Create the motor shield object with the default I2C address
AFMS = Adafruit_MotorShield()
# Or, create it with a different I2C address (say for stacking)
# AFMS = Adafruit_MotorShield(0x61); 

# Connect a stepper motor with 200 steps per revolution (1.8 degree)
# to motor port #2 (M3 and M4)
myMotor = AFMS.getStepper(200, 2)

AFMS.begin() # create with the default frequency 1.6KHz
#AFMS.begin(1100);  #// OR with a different frequency, say 1KHz

myMotor.setSpeed(20);  # 10 rpm

try:
	while (True):
		myMotor.step(400, Adafruit_StepperMotor.FORWARD, Adafruit_StepperMotor.DOUBLE)

except KeyboardInterrupt:
	myMotor.release() #remove current flow accross motor
	print ("Clean ")
  
