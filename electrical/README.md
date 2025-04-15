# ⚡ Electrical Components Testing

Before assembling the box, it's a good idea to verify that the electronics function as expected. There are two output devices to test:

1. **Linear Actuators**  
   Verify that the two actuators can extend and retract, and that they are controllable via a GPIO pin on a microcontroller.

2. **AC Relay**  
   Confirm that the AC relay clicks (indicating switching) when triggered by a GPIO pin from a microcontroller.

---

## 🧾 Bill of Materials (BOM)

| #    | Part Description                    | QTY | Vendor   | Vendor/Mfr Part #       | Notes / Link                                                              |
|------|-------------------------------------|-----|----------|--------------------------|---------------------------------------------------------------------------|
| A1   | Raspberry Pi Pico WH (RP2040)       | 1   | Digikey  | SC0919                   | Could substitute with another microcontroller                            |
| A2   | DPDT Relay, 12V, 5V Coil            | 1   | Digikey  | J104B2C12VDC.15S         | Also available from Actuonix (same part)                                 |
| A3   | NPN Transistor                      | 1   | Digikey  | TIP120                   | Interchangeable with similar-rated parts                                 |
| A4   | Flyback Diode                       | 1   | Digikey  | 1N4004G-T                | Interchangeable with similar-rated parts                                 |
| A5   | 1kΩ Resistor                        | 1   | Digikey  | -                        | Interchangeable with similar-rated parts                                 |
| A6   | Header Pins, 0.1" Pitch             | 9   | Digikey  | PRPC040SACN-RC           | Interchangeable with similar-rated parts                                 |
| A7   | 3.2" x 2" Protoboard                | 1   | Digikey  | DKS-SOLDERBREAD-02       | —                                                                         |
| A8   | AC Relay (3.3V Coil)                | 1   | Digikey  | 103020005                | Interchangeable with similar-rated parts                                 |
| A9   | Grove 4-Pin Female Jumper           | 1   | Digikey  | 110990028                | —                                                                         |
| A10  | 100mm Stroke Linear Actuator, 12VDC | 2   | Actuonix | L16-100-63-12-S          | [Link](https://www.actuonix.com/l16-100-63-12-s)                          |
| A11  | 12VDC Power Supply                  | 1   | Actuonix | dcpowersupply            | Can use alternative 12V supply for testing                                |
| A12  | USB Micro-B to USB-A Cable          | 1   | Digikey  | DH-20M50057              | Interchangeable with similar-rated parts                                 |

---

## 🧰 Wiring Diagram

![Wiring Diagram](https://github.com/kelvinchow23/the-cure/blob/main/electrical/electrical%20components%20test%20wiring%20diagram.png)  
![Physical Example](https://github.com/kelvinchow23/the-cure/blob/main/electrical/wired%20example.png)

- The diagram outlines the setup. The two relays—DC (for actuators) and AC (for a lamp)—can be tested independently.
- You don't need to connect the output terminals of the AC relay yet; a click is sufficient for now.
- A fuse is shown in the diagram connecting V+ to the relay. You can replace this with a jumper wire for testing.
- Wiring on the underside of the protoboard may not be visible in the physical photo.

---

## 🧪 Build & Test Instructions

1. Gather the components listed in the BOM. Substitutes are generally acceptable.
2. Solder components **A1–A6** onto the **A7** protoboard, following the wiring diagram.
   - **Pins 1–2**: 12V Power Supply (V+ and GND)
   - **Pins 3–6**: Actuator outputs (reverse polarity to change direction)
   - **Pins 7–9**: Grove connector to external relay
   - **Pin 10**: external 5V power input (not required if the pico is powered via USB. This will be necessary if it's a standalone module)
3. Connect the linear actuators to pins 3–6. Confirm they move **together**.
4. Connect the AC relay module to pins 7–9 via the Grove jumper. The white cable is not connected.
5. Power the board with a 12V supply through pins 1–2.
6. Connect the Raspberry Pi Pico to your computer using the USB cable.
7. Flash the Pico with **MicroPython firmware**.
8. Upload and run the script `the_cure_electrical_test.py`.
9. The test script will run the following loop:
   - a. Extend actuators  
   - b. Delay: 15 seconds  
   - c. Retract actuators  
   - d. Delay: 10 seconds  
   - e. Turn relay ON (click)  
   - f. Delay: 5 seconds  
   - g. Turn relay OFF  
   - h. Delay: 3 seconds

✅ If the actuators cycle correctly and you hear the relay click, the electronics are working. You can now proceed with the mechanical assembly.

> ⚠️ If actuators **start by retracting**, reverse their polarity or adjust the code.
