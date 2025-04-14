# Electrical Components Testing

Before assembling the box, it's a good idea to verify that the electronics function as expected. There are two output devices to test:

1. **Linear Actuators**  
   There are 2 linear actuators. Verify that they can be extended and retracted, and that they can be controlled through a GPIO pin from a microcontroller.

2. **AC Relay**  
   Verify that the AC relay can turn on/off (you should hear a clicking sound) when controlled through a GPIO pin from a microcontroller.

---

## Wiring Diagram

The wiring diagram outlines the setup. The two relays (DC relay for actuators and AC relay for the lamp) can be tested separately. At this stage, the output terminals of the AC relay don’t need to be connected. It’s enough to just hear the relay click during testing.

---

## Brief Instructions

- Refer to the BOM for the electrical parts. I think it's missing some power supplies and connector (12V to power the actuators and i think 5V is necessary to activate the coil on the relay) 
- Components **A2-A5** were soldered to a protoboard according to the wiring diagram. If the diagram is unclear, feel free to ask ChatGPT for clarification.
- I added header pins to the protoboard to connect the actuator, power supply, and the Pico. I’ve labeled them for easier identification.
- The AC relay is wired separately. It comes with a 4-pin cable, one of which is not used. This cable is connected separately to the Pico and power supply for testing.
- This is incomplete I will continue working on it. 
