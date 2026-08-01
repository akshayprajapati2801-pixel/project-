from tkinter import *

from ui.employee.add_employee_ui import AddEmployeeUI
from ui.employee.view_employee_ui import ViewEmployeeUI
from ui.employee.update_employee_ui import UpdateEmployeeUI
from ui.employee.delete_employee_ui import DeleteEmployeeUI


class EmployeeMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Employee Module")
        self.root.geometry("500x400")

        Label(self.root,
              text="EMPLOYEE MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Add Employee",
               width=20,
               height=2,
               command=self.open_add_employee).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="View Employees",
               width=20,
               height=2,
               command=self.open_view_employee).grid(row=0,column=1,padx=10,pady=10)

        Button(frame,
               text="Update Employee",
               width=20,
               height=2,
               command=self.open_update_employee).grid(row=1,column=0,padx=10,pady=10)

        Button(frame,
               text="Delete Employee",
               width=20,
               height=2,
               command=self.open_delete_employee).grid(row=1,column=1,padx=10,pady=10)


    def open_add_employee(self):
        AddEmployeeUI()


    def open_view_employee(self):
        ViewEmployeeUI()


    def open_update_employee(self):
        UpdateEmployeeUI()


    def open_delete_employee(self):
        DeleteEmployeeUI()
