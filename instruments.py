# instruments.py

import pyvisa

class InstrumentManager:

    def __init__(self):

        self.rm = pyvisa.ResourceManager()

    def connect(self, address):

        inst = self.rm.open_resource(address)

        inst.timeout = 5000

        print(inst.query("*IDN?"))

        return inst
      
class PowerSupply:

    def __init__(self, instrument):

        self.ps = instrument

    def configure(self, voltage, current):

        self.ps.write(f"VOLT {voltage}")

        self.ps.write(f"CURR {current}")

    def output_on(self):

        self.ps.write("OUTP ON")

    def output_off(self):

        self.ps.write("OUTP OFF")

 class ElectronicLoad:

    def __init__(self, instrument):

        self.load = instrument

    def set_current(self, current):

        self.load.write("FUNC CURR")

        self.load.write(f"CURR {current}")

    def input_on(self):

        self.load.write("INPUT ON")

    def input_off(self):

        self.load.write("INPUT OFF")

class DMM:

    def __init__(self, instrument):

        self.dmm = instrument

    def measure_voltage(self):

        return float(self.dmm.query("MEAS:VOLT:DC?"))

  class Oscilloscope:

    def __init__(self, instrument):

        self.scope = instrument

    def autoscale(self):

        self.scope.write(":AUToscale")

    def single(self):

        self.scope.write(":SINGLE")

    def run(self):

        self.scope.write(":RUN")

    def stop(self):

        self.scope.write(":STOP")

    
