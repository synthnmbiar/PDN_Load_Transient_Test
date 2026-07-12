# config.py

# VISA Addresses (Replace with actual VISA resource names)

POWER_SUPPLY = "USB0::0x05E6::0x2230::1234567::INSTR"
ELOAD = "USB0::0x05E6::0x2380::7654321::INSTR"
OSCILLOSCOPE = "USB0::0x2A8D::0x1766::MY123456::INSTR"
DMM = "USB0::0x05E6::0x6500::987654::INSTR"


# Input Supply

INPUT_VOLTAGE = 5.0
CURRENT_LIMIT = 5.0


# Load Settings

LOAD_LOW = 0.1      #10%
LOAD_HIGH = 0.9     #90%


# Acceptance Criteria

MAX_RIPPLE = 0.050          #50mV
MAX_OVERSHOOT = 0.100       #100mV
MAX_UNDERSHOOT = 0.100
MAX_RECOVERY = 200e-6       #200us


# Rails

RAILS = {

    "3V6":2.5,

    "3V3":3.0,

    "1V8":3.0,

    "2V5":1.5

}
