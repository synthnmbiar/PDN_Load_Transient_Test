# logger.py

import csv
import os
from datetime import datetime

RESULT_FOLDER = "results"
CSV_FILE = os.path.join(RESULT_FOLDER, "measurements.csv")


class CSVLogger:

    def __init__(self):

        os.makedirs(RESULT_FOLDER, exist_ok=True)

        file_exists = os.path.isfile(CSV_FILE)

        self.file = open(CSV_FILE, 'a', newline='')

        self.writer = csv.writer(self.file)

        if not file_exists:

            self.writer.writerow([

                "Timestamp",
                "Rail",
                "Voltage(V)",
                "Ripple(V)",
                "Overshoot(V)",
                "Undershoot(V)",
                "Recovery(us)",
                "Result"

            ])

    def log(self, data):

        self.writer.writerow([

            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            data["Rail"],

            round(data["Voltage"],3),

            round(data["Ripple"],3),

            round(data["Overshoot"],3),

            round(data["Undershoot"],3),

            round(data["Recovery"]*1e6,1),

            data["Result"]

        ])

        self.file.flush()

    def close(self):

        self.file.close()

  
