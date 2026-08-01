from tkinter import *
from tkinter import messagebox


class FeePaymentUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Fee Payment")
        self.root.geometry("500x450")

        Label(self.root,
              text="FEE PAYMENT",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack(pady=10)

        # Student ID
        Label(form, text="Student ID", width=15, anchor="w").grid(row=0, column=0, pady=10)
        self.student_id = Entry(form, width=30)
        self.student_id.grid(row=0, column=1)

        # Student Name
        Label(form, text="Student Name", width=15, anchor="w").grid(row=1, column=0, pady=10)
        self.student_name = Entry(form, width=30)
        self.student_name.grid(row=1, column=1)

        # Course
        Label(form, text="Course", width=15, anchor="w").grid(row=2, column=0, pady=10)
        self.course = Entry(form, width=30)
        self.course.grid(row=2, column=1)

        # Total Fees
        Label(form, text="Total Fees", width=15, anchor="w").grid(row=3, column=0, pady=10)
        self.total_fees = Entry(form, width=30)
        self.total_fees.grid(row=3, column=1)

        # Paid Amount
        Label(form, text="Paid Amount", width=15, anchor="w").grid(row=4, column=0, pady=10)
        self.paid_amount = Entry(form, width=30)
        self.paid_amount.grid(row=4, column=1)

        # Payment Method
        Label(form, text="Payment Method", width=15, anchor="w").grid(row=5, column=0, pady=10)

        self.payment_method = StringVar()
        self.payment_method.set("Cash")

        OptionMenu(form,
                   self.payment_method,
                   "Cash",
                   "UPI",
                   "Card",
                   "Bank Transfer").grid(row=5, column=1, sticky="w")

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=30)

        Button(btn_frame,
               text="Submit Payment",
               width=15,
               command=self.submit_payment).grid(row=0, column=0, padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0, column=1, padx=10)


    def submit_payment(self):

        sid = self.student_id.get()
        paid = self.paid_amount.get()

        if sid == "" or paid == "":
            messagebox.showerror("Error", "Student ID and Paid Amount required")
            return

        # temporary logic
        messagebox.showinfo("Success", "Fee Payment Recorded Successfully")

        self.clear_form()


    def clear_form(self):

        self.student_id.delete(0, END)
        self.student_name.delete(0, END)
        self.course.delete(0, END)
        self.total_fees.delete(0, END)
        self.paid_amount.delete(0, END)


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = FeePaymentUI()
    app.run()
