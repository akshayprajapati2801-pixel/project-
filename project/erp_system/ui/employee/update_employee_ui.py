from tkinter import *
from tkinter import messagebox


class UpdateEmployeeUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Update Employee")
        self.root.geometry("500x450")

        Label(self.root,
              text="UPDATE EMPLOYEE",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack()

        # Employee ID
        Label(form,text="Employee ID",width=15,anchor="w").grid(row=0,column=0,pady=10)
        self.emp_id = Entry(form,width=30)
        self.emp_id.grid(row=0,column=1)

        Button(form,
               text="Search",
               command=self.search_employee).grid(row=0,column=2,padx=5)

        # Name
        Label(form,text="Employee Name",width=15,anchor="w").grid(row=1,column=0,pady=10)
        self.name = Entry(form,width=30)
        self.name.grid(row=1,column=1)

        # Designation
        Label(form,text="Designation",width=15,anchor="w").grid(row=2,column=0,pady=10)
        self.designation = Entry(form,width=30)
        self.designation.grid(row=2,column=1)

        # Department
        Label(form,text="Department",width=15,anchor="w").grid(row=3,column=0,pady=10)
        self.department = Entry(form,width=30)
        self.department.grid(row=3,column=1)

        # Phone
        Label(form,text="Phone",width=15,anchor="w").grid(row=4,column=0,pady=10)
        self.phone = Entry(form,width=30)
        self.phone.grid(row=4,column=1)

        # Email
        Label(form,text="Email",width=15,anchor="w").grid(row=5,column=0,pady=10)
        self.email = Entry(form,width=30)
        self.email.grid(row=5,column=1)

        # Salary
        Label(form,text="Salary",width=15,anchor="w").grid(row=6,column=0,pady=10)
        self.salary = Entry(form,width=30)
        self.salary.grid(row=6,column=1)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=30)

        Button(btn_frame,
               text="Update",
               width=15,
               command=self.update_employee).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def search_employee(self):

        emp_id = self.emp_id.get()

        if emp_id == "":
            messagebox.showerror("Error","Enter Employee ID")
            return

        # Temporary dummy data (later from database)
        self.name.delete(0,END)
        self.name.insert(0,"Ravi Kumar")

        self.designation.delete(0,END)
        self.designation.insert(0,"Trainer")

        self.department.delete(0,END)
        self.department.insert(0,"IT")

        self.phone.delete(0,END)
        self.phone.insert(0,"9876543210")

        self.email.delete(0,END)
        self.email.insert(0,"ravi@gmail.com")

        self.salary.delete(0,END)
        self.salary.insert(0,"35000")


    def update_employee(self):

        if self.emp_id.get() == "":
            messagebox.showerror("Error","Employee ID required")
            return

        # Later connect service layer
        messagebox.showinfo("Success","Employee Updated Successfully")


    def clear_form(self):

        self.emp_id.delete(0,END)
        self.name.delete(0,END)
        self.designation.delete(0,END)
        self.department.delete(0,END)
        self.phone.delete(0,END)
        self.email.delete(0,END)
        self.salary.delete(0,END)


    def run(self):
        self.root.mainloop()


# Testing
if __name__ == "__main__":
    app = UpdateEmployeeUI()
    app.run()
