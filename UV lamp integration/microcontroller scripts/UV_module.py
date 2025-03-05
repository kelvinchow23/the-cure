from machine import Pin
import time

    
def move_wellplate_out(): 
    track_relay = Pin(27, Pin.OUT)  # GPIO 27 for the track relay
    led = Pin('LED', Pin.OUT)  # Onboard LED for status indication
     
    print("Moving wellplate out")
    track_relay.value(1) # Turn on the track relay
    led.value(1)  # Turn on onboard LED as an indicator
    time.sleep(7)  # Delay for 7 seconds (need time for tray to move in)
    

def move_wellplate_in():
    track_relay = Pin(27, Pin.OUT)  # GPIO 27 for the track relay
    led = Pin('LED', Pin.OUT) 
    
    print("Moving wellplate in")
    track_relay.value(0) # Turn off the track relay
    led.value(0)
    time.sleep(7)  # Delay for 7 seconds (need time for tray to move out)
    
def turn_on_UV(duration): #duration in minutes
    """
    Turns on relay for UV lamp for the specified duration of time (in minutes) & turns the lamp off after the duration is complete.
    """
    lamp_relay = Pin(26, Pin.OUT)  # GPIO 26 for the lamp relay
    led = Pin('LED', Pin.OUT)  # Onboard LED for status indication
    
    duration_seconds = duration*60
    print(f"Turning on lamp for {duration} minutes")
    lamp_relay.value(1)
    led.value(1)
    time.sleep(duration_seconds)  # Delay for duration in seconds
    
    # Turn off the lamp relay after duration is over
    lamp_relay.value(0)
    led.value(0)
    print("UV Lamp turned off")
    time.sleep(1)  # Delay for 1 second to ensure light is off (maybe not needed)
  
# to run methods  
#move_wellplate_out()
#move_wellplate_in()
#turn_on_UV(0.2)
#move_wellplate_out()



### old (archived) methods:
"""
def initialize_crosslinker(): 
    # Set up GPIO pins
    lamp_relay = Pin(26, Pin.OUT)  # GPIO 26 for the lamp relay
    track_relay = Pin(27, Pin.OUT)  # GPIO 27 for the track relay
    led = Pin('LED', Pin.OUT)  # Onboard LED for status indication

    # Ensure relays are initially off
    #lamp_relay.value(0)
    #track_relay.value(0)
    led.value(0)
    print("Initialization complete")
    return track_relay, lamp_relay, led 
"""