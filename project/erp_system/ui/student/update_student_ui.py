from tkinter import *
from tkinter import messagebox


class UpdateStudentUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Update Student")
        self.root.geometry("500x420")

        Label(self.root,
              text="UPDATE STUDENT",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack()

        Label(form,text="Student ID",width=15,anchor="w").grid(row=0,column=0,pady=10)
        self.student_id = Entry(form,width=30)
        self.student_id.grid(row=0,column=1)

        Button(form,
               text="Search",
               command=self.search_student).grid(row=0,column=2,padx=5)

        Label(form,text="Name",width=15,anchor="w").grid(row=1,column=0,pady=10)
        self.name = Entry(form,width=30)
        self.name.grid(row=1,column=1)

        Label(form,text="Course",width=15,anchor="w").grid(row=2,column=0,pady=10)
        self.course = Entry(form,width=30)
        self.course.grid(row=2,column=1)

        Label(form,text="Phone",width=15,anchor="w").grid(row=3,column=0,pady=10)
        self.phone = Entry(form,width=30)
        self.phone.grid(row=3,column=1)

        Label(form,text="Email",width=15,anchor="w").grid(row=4,column=0,pady=10)
        self.email = Entry(form,width=30)
        self.email.grid(row=4,column=1)

        Label(form,text="Fees",width=15,anchor="w").grid(row=5,column=0,pady=10)
        self.fees = Entry(form,width=30)
        self.fees.grid(row=5,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Update",
               width=15,
               command=self.update_student).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def search_student(self):

        sid = self.student_id.get()

        if sid == "":
            messagebox.showerror("Error","Enter Student ID")
            return

        # Dummy data (later from database)
        self.name.delete(0,END)
        self.name.insert(0,"Rahul")

        self.course.delete(0,END)
        self.course.insert(0,"Python")

        self.phone.delete(0,END)
        self.phone.insert(0,"9876543210")

        self.email.delete(0,END)
        self.email.insert(0,"rahul@gmail.com")

        self.fees.delete(0,END)
        self.fees.insert(0,"5000")


    def update_student(self):

        messagebox.showinfo("Success","Student Updated Successfully")


    def clear_form(self):

        self.student_id.delete(0,END)
        self.name.delete(0,END)
        self.course.delete(0,END)
        self.phone.delete(0,END)
        self.email.delete(0,END)
        self.fees.delete(0,END)


    def run(self):
        self.root.mainloop()
