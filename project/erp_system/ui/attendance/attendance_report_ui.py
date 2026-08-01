from tkinter import *
from tkinter import ttk


class AttendanceReportUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Attendance Report")
        self.root.geometry("750x450")

        Label(self.root,
              text="ATTENDANCE REPORT",
              font=("Arial",18,"bold")).pack(pady=10)

        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scroll_y = Scrollbar(table_frame)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.table = ttk.Treeview(
            table_frame,
            columns=("student_id","course","date","status"),
            yscrollcommand=scroll_y.set
        )

        scroll_y.config(command=self.table.yview)

        self.table.heading("student_id",text="Student ID")
        self.table.heading("course",text="Course")
        self.table.heading("date",text="Date")
        self.table.heading("status",text="Status")

        self.table["show"] = "headings"

        self.table.column("student_id",width=120)
        self.table.column("course",width=150)
        self.table.column("date",width=150)
        self.table.column("status",width=120)

        self.table.pack()

        self.load_data()


    def load_data(self):

        data = [
            (101,"Python Full Stack","10-03-2026","Present"),
            (102,"Data Science","10-03-2026","Absent"),
            (103,"Web Development","10-03-2026","Present")
        ]

        for row in data:
            self.table.insert("",END,values=row)