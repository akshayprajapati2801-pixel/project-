from tkinter import *

from ui.fee.fee_payment_ui import FeePaymentUI
from ui.fee.fee_report_ui import FeeReportUI


class FeeMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Fee Module")
        self.root.geometry("400x300")

        Label(self.root,
              text="FEE MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Fee Payment",
               width=20,
               height=2,
               command=self.open_fee_payment).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="Fee Reports",
               width=20,
               height=2,
               command=self.open_fee_report).grid(row=0,column=1,padx=10,pady=10)


    def open_fee_payment(self):
        FeePaymentUI()

    def open_fee_report(self):
        FeeReportUI()


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    app = FeeMenuUI()
    app.run()
