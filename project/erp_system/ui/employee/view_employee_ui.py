from tkinter import *
from tkinter import ttk


class ViewEmployeeUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("View Employees")
        self.root.geometry("850x500")

        Label(self.root,
              text="EMPLOYEE LIST",
              font=("Arial",18,"bold")).pack(pady=10)

        # Search Frame
        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame,text="Search Employee").grid(row=0,column=0,padx=5)

        self.search_box = Entry(search_frame,width=30)
        self.search_box.grid(row=0,column=1,padx=5)

        Button(search_frame,
               text="Search",
               width=12).grid(row=0,column=2,padx=5)

        Button(search_frame,
               text="Show All",
               width=12,
               command=self.load_employees).grid(row=0,column=3,padx=5)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scrollbar_y = Scrollbar(table_frame)
        scrollbar_y.pack(side=RIGHT,fill=Y)

        scrollbar_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM,fill=X)

        self.emp_table = ttk.Treeview(
            table_frame,
            columns=("id","name","designation","department","phone","email","salary"),
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        scrollbar_y.config(command=self.emp_table.yview)
        scrollbar_x.config(command=self.emp_table.xview)

        self.emp_table.heading("id",text="ID")
        self.emp_table.heading("name",text="Name")
        self.emp_table.heading("designation",text="Designation")
        self.emp_table.heading("department",text="Department")
        self.emp_table.heading("phone",text="Phone")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("salary",text="Salary")

        self.emp_table["show"] = "headings"

        self.emp_table.column("id",width=80)
        self.emp_table.column("name",width=150)
        self.emp_table.column("designation",width=120)
        self.emp_table.column("department",width=120)
        self.emp_table.column("phone",width=120)
        self.emp_table.column("email",width=180)
        self.emp_table.column("salary",width=100)

        self.emp_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=10)

        Button(btn_frame,
               text="Refresh",
               width=12,
               command=self.load_employees).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Close",
               width=12,
               command=self.root.destroy).grid(row=0,column=1,padx=10)

        # Load data
        self.load_employees()


    def load_employees(self):

        # Clear table
        for row in self.emp_table.get_children():
            self.emp_table.delete(row)

        # Dummy data (later from database)
        employees = [
            (101,"Ravi Kumar","Trainer","IT","9876543210","ravi@gmail.com",35000),
            (102,"Amit Singh","Developer","IT","9876543211","amit@gmail.com",45000),
            (103,"Neha Sharma","HR","HR","9876543212","neha@gmail.com",30000),
        ]

        for emp in employees:
            self.emp_table.insert("",END,values=emp)


    def run(self):
        self.root.mainloop()


# Testing
if __name__ == "__main__":
    app = ViewEmployeeUI()
    app.run()
