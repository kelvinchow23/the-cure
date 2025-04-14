# the cure - A UV curing module for well plates
![image](https://github.com/user-attachments/assets/ea43d303-7357-4c05-b2b1-cb8a85ad2cb5)

## Purpose
The main function of the curing module is for photopolymerization of a sample using a [[UV flood lamp](https://www.amazon.ca/Everbeam-365nm-50W-Black-Light/dp/B08635F9CX/?th=1)], intended for samples in a well plate. 
Since there are hazards associated with UV light, the module was desgined to push out a tray in/out of a box so that the light is shielded from the surrounding users/environment during curing.  
The intention of this module is to be used in an automated workflow with a robot arm to pick and place from this module as a curing station. 

## Requirements
- Firmware: The module's controller is a raspberry pico w, which runs on Micropython. honestly if you dig into the program, it's stupid simple and can be replaced by any microcontroller really. 
- Needs a host computer. The pico is connected to the computer via USB serial.  It could be configured to run standalone (and say receive MQTT commands), but a computer will be necessary to upload the firmware regardless
- Needs a 120VAC source (plugs into a NEMA 5-15 receptacle)
- The UV lamp has an on/off switch. This needs to be set to the on position for the lamp to operateate method for making a UV resistant housing.
- The module is built around the UV flood lamp, which has a length of about 8". Based on this, the actuator extension length (200mm) and the supporting slides (8")

## Build Overview
This repository contains build instructions, which can be divided into 3 steps:
1) Build and test the functionality of the electronic components
2) Assemble the curing module
3) Use the scripts (or your own) to control the module

## Module Operation
Refer to the scripts in the firmware folder

## Random Notes
- Many of these components are 3D-printed in ASA, which is more UV resistant than most standard filmanets.  Ensure that there is this capabiltiy to print in ASA, or find an alternative way to make the housing out of a UV resistant material
- The module was designed around the UV lamp, which has a length of ~8 inches. Based on this, the tray extension was designed to extend about 8 inches (200mm).  If choosing a different lamp, try to match the extension with the length/width of the light source
  
## Future Steps
- the electrrical wiring could use some updating. Replace the protoboard with a pcb.
- the housing could probably be simplified to less parts.  Specifically, the base can be merged from 2 parts into 1. The initial design did not consider the need for mounting to a base plate, which was why the outer base housing was necessary. 
