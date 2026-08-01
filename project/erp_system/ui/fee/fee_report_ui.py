from tkinter import *
from tkinter import ttk


class FeeReportUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Fee Report")
        self.root.geometry("750x450")

        Label(self.root,
              text="FEE REPORT",
              font=("Arial",18,"bold")).pack(pady=20)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(fill=BOTH, expand=True)

        columns = ("student_id", "student_name", "course", "total_fees", "paid_amount", "payment_method")

        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tree.heading("student_id", text="Student ID")
        self.tree.heading("student_name", text="Student Name")
        self.tree.heading("course", text="Course")
        self.tree.heading("total_fees", text="Total Fees")
        self.tree.heading("paid_amount", text="Paid Amount")
        self.tree.heading("payment_method", text="Payment Method")

        self.tree.column("student_id", width=100)
        self.tree.column("student_name", width=150)
        self.tree.column("course", width=120)
        self.tree.column("total_fees", width=100)
        self.tree.column("paid_amount", width=100)
        self.tree.column("payment_method", width=120)

        scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=15)

        Button(btn_frame,
               text="Load Report",
               width=15,
               command=self.load_report).grid(row=0, column=0, padx=10)

        Button(btn_frame,
               text="Close",
               width=15,
               command=self.root.destroy).grid(row=0, column=1, padx=10)


    def load_report(self):

        # temporary sample data (later from database)
        data = [
            (1, "Rahul", "Python", 50000, 25000, "UPI"),
            (2, "Amit", "Java", 60000, 60000, "Cash"),
            (3, "Neha", "Data Science", 80000, 40000, "Card")
        ]

        for row in data:
            self.tree.insert("", END, values=row)


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = FeeReportUI()
    app.run()
