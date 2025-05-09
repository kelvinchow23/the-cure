# the cure - a UV curing module for well plates


![image](https://github.com/user-attachments/assets/059c375e-af60-4fa5-8ffc-84d85557fd96)


## Purpose
The main function of the curing module is for photopolymerization of a sample using a [UV flood lamp](https://www.amazon.ca/Everbeam-365nm-50W-Black-Light/dp/B08635F9CX/?th=1), intended for samples in a well plate. 
Since UV light poses safety risks, the module includes a motorized tray that slides in and out of a fully enclosed housing. This shields users and the surrounding environment from exposure during operation.
The module is intended to integrate into an automated workflow where a robot arm can pick and place well plates into the box for curing.

## Requirements
- **Microcontroller:** Raspberry Pi Pico W running MicroPython. Honestly, the firmware is very simple and can be adapted to other controllers. It's a matter of controlling 2 digital IO pins for turning on/off relays.
- **Host Computer:** Required to upload firmware and communicate via USB serial. The Pico could potentially operate standalone (e.g., over MQTT), but you’ll still need a computer to flash it initially.
- **Power Source:** Build instructions are for 120VAC (standard NEMA 5-15 plug).
- **Lamp:** The UV lamp has an on/off switch — make sure it is switched *on* for operation.

## Build Overview

This repository includes a three-part guide:
1. **Electronics:** Build and test the electrical components. Instructions are in the `/electrical` folder. 
2. **Mechanical Assembly:** Build instructions for the mechanical housing are in the `/mechanical` folder. 
3. **Firmware & Control:** Use the provided scripts (or your own) to control the module. See **Module Operation** below for operation. 

## Module Operation

The `/scripts` folder contains two key scripts.  
The main firmware script, `UV_module.py`, is uploaded to the microcontroller and provides three core functions:

1. **`move_wellplate_out()`** – Extends the well plate tray.
2. **`move_wellplate_in()`** – Retracts the well plate tray.
3. **`turn_on_UV(duration)`** – Turns on the UV lamp for a specified duration (in minutes).

These functions can be called directly from the microcontroller or remotely via a host computer using tools like `mpremote`.

The `UV_module_controller.py` script is designed to be run on a host computer.  
It communicates with the microcontroller over a serial COM port (currently set to `COM4`, but this may need to be updated based on your system).

When executed, the current workflow is as follows:
1. Retract the well plate tray.
2. Cure the sample for 30 seconds.
3. Extend the well plate tray.


## Notes
- Most 3D-printed parts are made from ASA filament, which is more UV-resistant than standard materials. If ASA printing isn't available, use an alternative UV-resistant material for the housing.
- The actuator's 200mm extension matches the UV lamp’s length (~8"). If using a different lamp, adjust the actuator and tray length to suit.  Note that the guide drawer slides must have an extension longer than the actuator's extension. In this case, the drawer slides have an 8" [203.2mm] extension length.
- This module was designed to mount to an M6 breadboard table. If mounting elsewhere, change the hole features in the UVouter base [C5]. STEP and fusion files are [here](https://github.com/kelvinchow23/the-cure/tree/main/mechanical/3D%20prints%20and%20CAD%20files).

---
  
## Future Steps
- **Electronics:** swap out the perfboard electronics with something a bit cleaner.  it's currently using a dpdt relay since the actuonix actuators were intended to use without an external conntroller. I think this can be done cleaner with an H-bridge module or a 2-channel SPDT relay module. It would still be necessary to have the 3rd relay for controlling the lamp.
- **Housing:**.  The outer and inner housing can be merged together.  This was initially done in two steps because initially, there was no thought of how the moudule would be fixed to a table.
- **UV Lamp:** The lamp itself is not characterized well apart from knowing the wavelength.  Intensity and spatial distribution isn't well known. 
- **Mechanical Housing:** Simplify the housing. The base can likely be reduced from two parts to one. Originally, the two-piece base was added to allow mounting to a plate, which might now be unnecessary with design tweaks.

## Revision History
- **Revision A** - Updated: 2025-04-14
