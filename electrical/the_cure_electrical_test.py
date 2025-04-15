from machine import Pin
import time

# Set up GPIO pins
track_relay = Pin(26, Pin.OUT)  # GPIO 26 for the track relay
lamp_relay = Pin(27, Pin.OUT)  # GPIO 27 for the lamp relay
led = Pin('LED', Pin.OUT)  # Onboard LED for status indication

# Ensure relays are initially off
lamp_relay.value(0)
track_relay.value(0)
led.value(0)

# Main loop
while True:
    # Turn on the track relay
    print("Turning on track relay...")
    track_relay.value(1)
    led.value(1)  # Turn on onboard LED as an indicator
    time.sleep(15)  # Delay for 15 seconds

    # Turn off the track relay
    print("Turning off track relay...")
    track_relay.value(0)
    led.value(0)
    time.sleep(10)  # Delay for 10 seconds

    # Turn on the lamp relay
    print("Turning on lamp relay...")
    lamp_relay.value(1)
    led.value(1)
    time.sleep(5)  # Delay for 5 seconds

    # Turn off the lamp relay
    print("Turning off lamp relay...")
    lamp_relay.value(0)
    led.value(0)
    time.sleep(3)  # Delay for 3 seconds
