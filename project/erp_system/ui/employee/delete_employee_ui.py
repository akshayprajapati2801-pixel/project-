from tkinter import *
from tkinter import messagebox


class DeleteEmployeeUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Delete Employee")
        self.root.geometry("400x250")

        Label(self.root,
              text="DELETE EMPLOYEE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame,
              text="Employee ID",
              width=15).grid(row=0,column=0,pady=10)

        self.emp_id = Entry(frame,width=25)
        self.emp_id.grid(row=0,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Delete",
               width=15,
               command=self.delete_employee).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def delete_employee(self):

        emp_id = self.emp_id.get()

        if emp_id == "":
            messagebox.showerror("Error","Enter Employee ID")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this employee?"
        )

        if confirm:
            # Later connect DAO layer
            messagebox.showinfo("Success","Employee Deleted Successfully")
            self.clear_form()


    def clear_form(self):

        self.emp_id.delete(0,END)


    def run(self):
        self.root.mainloop()


# Testing
if __name__ == "__main__":
    app = DeleteEmployeeUI()
    app.run()
