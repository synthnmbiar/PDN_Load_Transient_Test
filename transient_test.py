# transient_test.py

import time
from datetime import datetime
import config


class LoadTransientTest:

    def __init__(self, ps, eload, dmm, scope):

        self.ps = ps
        self.eload = eload
        self.dmm = dmm
        self.scope = scope

    def run_test(self, rail_name, max_current):

        print(f"\nTesting {rail_name}")

        low_current = max_current * config.LOAD_LOW
        high_current = max_current * config.LOAD_HIGH

        # Enable Supply
        self.ps.output_on()

        # Configure Oscilloscope
        self.scope.run()

        # Apply Low Load
        self.eload.set_current(low_current)
        self.eload.input_on()

        time.sleep(1)

        voltage_low = self.dmm.measure_voltage()

        # Apply High Load
        self.eload.set_current(high_current)

        time.sleep(1)

        voltage_high = self.dmm.measure_voltage()

        # Trigger Scope
        self.scope.single()

        time.sleep(2)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        waveform_name = f"results/waveforms/{rail_name}_{timestamp}.png"

        self.save_waveform(waveform_name)

        # Example Measurements
        ripple = self.measure_ripple()
        overshoot = self.measure_overshoot()
        undershoot = self.measure_undershoot()
        recovery = self.measure_recovery()

        result = self.evaluate(
            voltage_high,
            ripple,
            overshoot,
            undershoot,
            recovery
        )

        self.eload.input_off()

        return {

            "Rail": rail_name,
            "Voltage": voltage_high,
            "Ripple": ripple,
            "Overshoot": overshoot,
            "Undershoot": undershoot,
            "Recovery": recovery,
            "Result": result,
            "Waveform": waveform_name

        }

    def save_waveform(self, filename):

        print(f"Saving waveform : {filename}")

        # Actual SCPI command depends on oscilloscope model

        # Example:
        # image = self.scope.scope.query_binary_values(
        # ":DISPlay:DATA? PNG",
        # datatype='B'
        # )
        #
        # with open(filename,'wb') as f:
        #     f.write(bytearray(image))

    def measure_ripple(self):

        # Replace by SCPI query

        return 0.028

    def measure_overshoot(self):

        return 0.060

    def measure_undershoot(self):

        return 0.055

    def measure_recovery(self):

        return 120e-6

    def evaluate(self,
                 voltage,
                 ripple,
                 overshoot,
                 undershoot,
                 recovery):

        if ripple > config.MAX_RIPPLE:
            return "FAIL"

        if overshoot > config.MAX_OVERSHOOT:
            return "FAIL"

        if undershoot > config.MAX_UNDERSHOOT:
            return "FAIL"

        if recovery > config.MAX_RECOVERY:
            return "FAIL"

        return "PASS"
