# main.py

import config

from instruments import (
    InstrumentManager,
    PowerSupply,
    ElectronicLoad,
    DMM,
    Oscilloscope
)

from transient_test import LoadTransientTest
from logger import CSVLogger
from report import ReportGenerator


def main():

    print("===================================")
    print("PDN Load Transient Test Automation")
    print("===================================")

    # ---------------------------------------------------
    # Connect to VISA Resource Manager
    # ---------------------------------------------------

    manager = InstrumentManager()

    print("\nConnecting to Instruments...\n")

    ps_inst = manager.connect(config.POWER_SUPPLY)
    eload_inst = manager.connect(config.ELOAD)
    dmm_inst = manager.connect(config.DMM)
    scope_inst = manager.connect(config.OSCILLOSCOPE)

    # ---------------------------------------------------
    # Create Objects
    # ---------------------------------------------------

    power_supply = PowerSupply(ps_inst)
    electronic_load = ElectronicLoad(eload_inst)
    dmm = DMM(dmm_inst)
    scope = Oscilloscope(scope_inst)

    # ---------------------------------------------------
    # Configure Power Supply
    # ---------------------------------------------------

    print("\nConfiguring Power Supply...")

    power_supply.configure(

        config.INPUT_VOLTAGE,

        config.CURRENT_LIMIT

    )

    # ---------------------------------------------------
    # Create Test Object
    # ---------------------------------------------------

    tester = LoadTransientTest(

        power_supply,

        electronic_load,

        dmm,

        scope

    )

    logger = CSVLogger()

    print("\nStarting Tests...\n")

    # ---------------------------------------------------
    # Test Every Rail
    # ---------------------------------------------------

    for rail, current in config.RAILS.items():

        result = tester.run_test(

            rail,

            current

        )

        logger.log(result)

        print(result)

    # ---------------------------------------------------
    # Close CSV
    # ---------------------------------------------------

    logger.close()

    # ---------------------------------------------------
    # Generate Report
    # ---------------------------------------------------

    report = ReportGenerator()

    report.generate()

    # ---------------------------------------------------
    # Turn Off Instruments
    # ---------------------------------------------------

    electronic_load.input_off()

    power_supply.output_off()

    print("\n===================================")

    print("Testing Completed Successfully")

    print("CSV Saved")

    print("PDF Report Generated")

    print("===================================")


if __name__ == "__main__":

    main()
