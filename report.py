# report.py

import pandas as pd
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

CSV_FILE = "results/measurements.csv"
PDF_FILE = "results/Test_Report.pdf"


class ReportGenerator:

    def generate(self):

        # Read CSV

        df = pd.read_csv(CSV_FILE)

        # Statistics

        total = len(df)

        passed = len(df[df["Result"] == "PASS"])

        failed = len(df[df["Result"] == "FAIL"])

        pass_percentage = (passed / total) * 100

        avg_voltage = df["Voltage(V)"].mean()

        avg_ripple = df["Ripple(V)"].mean()

        max_ripple = df["Ripple(V)"].max()

        max_overshoot = df["Overshoot(V)"].max()

        max_undershoot = df["Undershoot(V)"].max()

        avg_recovery = df["Recovery(us)"].mean()

        # Create PDF

        doc = SimpleDocTemplate(PDF_FILE)

        styles = getSampleStyleSheet()

        elements = []

        elements.append(
            Paragraph(
                "<b>PDN Load Transient Test Report</b>",
                styles["Title"]
            )
        )

        elements.append(
            Paragraph(
                "Automated Qualification Test",
                styles["Heading2"]
            )
        )

        elements.append(
            Paragraph(
                f"Total Tests : {total}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Passed : {passed}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Failed : {failed}",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Pass Percentage : {pass_percentage:.2f} %",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Voltage : {avg_voltage:.3f} V",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Ripple : {avg_ripple:.3f} V",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Maximum Ripple : {max_ripple:.3f} V",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Maximum Overshoot : {max_overshoot:.3f} V",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Maximum Undershoot : {max_undershoot:.3f} V",
                styles["Normal"]
            )
        )

        elements.append(
            Paragraph(
                f"Average Recovery : {avg_recovery:.2f} us",
                styles["Normal"]
            )
        )

        # Add Table

        table_data = [list(df.columns)]

        table_data += df.values.tolist()

        table = Table(table_data)

        table.setStyle(

            TableStyle([

                ('BACKGROUND',(0,0),(-1,0),colors.grey),

                ('TEXTCOLOR',(0,0),(-1,0),colors.white),

                ('GRID',(0,0),(-1,-1),1,colors.black),

                ('BACKGROUND',(0,1),(-1,-1),colors.beige)

            ])

        )

        elements.append(table)

        doc.build(elements)

        print("PDF Report Generated")

  
