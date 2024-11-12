import machine
import utime

# Define GPIO pins for the LED's
red_pin = machine.Pin(16, machine.Pin.OUT);
yellow_pin = machine.Pin(17, machine.Pin.OUT);
green_pin = machine.Pin(18, machine.Pin.OUT);

# Function to turn all LEDs off
def all_off():
    print('** all off')
    red_pin.value(0)
    yellow_pin.value(0)
    green_pin.value(0)
    
def red(duration):
    print('** red on')
    red_pin.value(1)
    utime.sleep(duration)
    
def yellow(duration):
    print('** yellow on')
    yellow_pin.value(1)
    utime.sleep(duration)
    
def green(duration):
    print('** green on')
    green_pin.value(1)
    utime.sleep(duration)

# Main Loop
while True:
    all_off()  # Turn all LEDs off    
    red(5)     # Turn red LED on for 5 seconds
    all_off()  # Turn all LEDs off
    yellow(2)  # Turn yellow LED on for 1 seconds
    all_off()  # Turn all LEDs off
    green(4)   # Turn green LED on for 4 seconds