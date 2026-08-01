from tkinter import *
from tkinter import messagebox


class AddEmployeeUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Add Employee")
        self.root.geometry("500x450")

        Label(self.root,
              text="ADD EMPLOYEE",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack()

        # Employee ID
        Label(form,text="Employee ID",width=15,anchor="w").grid(row=0,column=0,pady=10)
        self.emp_id = Entry(form,width=30)
        self.emp_id.grid(row=0,column=1)

        # Name
        Label(form,text="Name",width=15,anchor="w").grid(row=1,column=0,pady=10)
        self.name = Entry(form,width=30)
        self.name.grid(row=1,column=1)

        # Department
        Label(form,text="Department",width=15,anchor="w").grid(row=2,column=0,pady=10)
        self.department = Entry(form,width=30)
        self.department.grid(row=2,column=1)

        # Designation
        Label(form,text="Designation",width=15,anchor="w").grid(row=3,column=0,pady=10)
        self.designation = Entry(form,width=30)
        self.designation.grid(row=3,column=1)

        # Phone
        Label(form,text="Phone",width=15,anchor="w").grid(row=4,column=0,pady=10)
        self.phone = Entry(form,width=30)
        self.phone.grid(row=4,column=1)

        # Salary
        Label(form,text="Salary",width=15,anchor="w").grid(row=5,column=0,pady=10)
        self.salary = Entry(form,width=30)
        self.salary.grid(row=5,column=1)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=30)

        Button(btn_frame,
               text="Save Employee",
               width=15,
               command=self.save_employee).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def save_employee(self):

        emp_id = self.emp_id.get()
        name = self.name.get()

        if emp_id == "" or name == "":
            messagebox.showerror("Error","Employee ID and Name required")
            return

        # Temporary logic (later connect service layer)
        messagebox.showinfo("Success","Employee Saved Successfully")

        self.clear_form()


    def clear_form(self):

        self.emp_id.delete(0,END)
        self.name.delete(0,END)
        self.department.delete(0,END)
        self.designation.delete(0,END)
        self.phone.delete(0,END)
        self.salary.delete(0,END)


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = AddEmployeeUI()
    app.run()
