# PDN_Load_Transient_Test
# PDN Load Transient Test Automation

****Overview****

This project automates the load transient testing of a Power Distribution Network (PDN) designed for a satellite payload. The automation framework communicates with laboratory instruments using PyVISA and SCPI commands to perform load transient tests, capture oscilloscope waveforms, log measurements, evaluate Pass/Fail criteria, and generate a PDF test report.

The project is developed as part of the Junior Hardware Test Engineer assessment.

---------------------------------

## Features

- Automatic instrument initialization
- Instrument communication using PyVISA
- SCPI-based instrument control
- Automated load transient testing
- Voltage measurement using Digital Multimeter
- Oscilloscope waveform capture
- CSV result logging
- Automatic Pass/Fail evaluation
- Statistical analysis
- PDF report generation
- Timestamped waveform storage

----------------------------------

## Hardware Used

Equipment and Model 

Programmable DC Power Supply | Keithley 2230-30-1 
Electronic Load | Keithley 2380 Series 
Oscilloscope | Keysight DSOX6004A 
Digital Multimeter | Keithley DMM6500 

-----------------------------

## Software Requirements

- Python 3.10 or later
- PyVISA
- PyVISA-py
- Pandas
- NumPy
- ReportLab

-------------------------------
## Test Procedure

The automation performs the following sequence:

1. Connect to all instruments.
2. Verify communication using **SCPI *IDN?**.
3. Configure the programmable power supply.
4. Configure the electronic load.
5. Configure the oscilloscope.
6. Apply the nominal input voltage.
7. Perform load transient testing on each output rail.
8. Measure output voltage.
9. Capture transient waveform.
10. Measure ripple, overshoot, undershoot and recovery time.
11. Compare measurements with acceptance criteria.
12. Store results in CSV.
13. Generate a PDF report.

-------------------------


## Acceptance Criteria

| Parameter     | Limit   |

| Voltage       | ±5%.    |
| Ripple        | <50 mV  |
| Overshoot     | <100 mV |
| Undershoot    | <100 mV |
| Recovery Time | <200 µs |

----------------------------

## Running the Test

Execute


python main.py

--------------------------

## Output

After execution, the following files are generated.


results/

measurements.csv

Test_Report.pdf

waveforms/

3V6_20260715_101210.png

3V3_20260715_101530.png

1V8_20260715_101845.png

2V5_20260715_102015.png


------------------------------


## Author

Sayanth Mohandas

Junior Hardware Test Engineer Assessment

