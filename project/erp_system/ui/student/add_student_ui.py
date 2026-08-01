from tkinter import *
from tkinter import messagebox


class AddStudentUI:

    def __init__(self):

        self.root = Tk()
        self.root.title("Add Student")
        self.root.geometry("500x450")

        Label(self.root,
              text="ADD STUDENT",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack()

        # Student ID
        Label(form,text="Student ID",width=15,anchor="w").grid(row=0,column=0,pady=10)
        self.student_id = Entry(form,width=30)
        self.student_id.grid(row=0,column=1)

        # Student Name
        Label(form,text="Student Name",width=15,anchor="w").grid(row=1,column=0,pady=10)
        self.name = Entry(form,width=30)
        self.name.grid(row=1,column=1)

        # Course
        Label(form,text="Course",width=15,anchor="w").grid(row=2,column=0,pady=10)
        self.course = Entry(form,width=30)
        self.course.grid(row=2,column=1)

        # Phone
        Label(form,text="Phone",width=15,anchor="w").grid(row=3,column=0,pady=10)
        self.phone = Entry(form,width=30)
        self.phone.grid(row=3,column=1)

        # Email
        Label(form,text="Email",width=15,anchor="w").grid(row=4,column=0,pady=10)
        self.email = Entry(form,width=30)
        self.email.grid(row=4,column=1)

        # Fees
        Label(form,text="Fees",width=15,anchor="w").grid(row=5,column=0,pady=10)
        self.fees = Entry(form,width=30)
        self.fees.grid(row=5,column=1)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=30)

        Button(btn_frame,
               text="Save Student",
               width=15,
               command=self.save_student).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)

    def save_student(self):

        sid = self.student_id.get()
        name = self.name.get()
        course = self.course.get()
        phone = self.phone.get()
        email = self.email.get()
        fees = self.fees.get()

        if sid=="" or name=="":
            messagebox.showerror("Error","Student ID and Name required")
            return

        # Temporary logic (later connect service layer)
        messagebox.showinfo("Success","Student Saved Successfully")

        self.clear_form()


    def clear_form(self):

        self.student_id.delete(0,END)
        self.name.delete(0,END)
        self.course.delete(0,END)
        self.phone.delete(0,END)
        self.email.delete(0,END)
        self.fees.delete(0,END)


    def run(self):
        self.root.mainloop()


# testing purpose
if __name__ == "__main__":
    app = AddStudentUI()
    app.run()
