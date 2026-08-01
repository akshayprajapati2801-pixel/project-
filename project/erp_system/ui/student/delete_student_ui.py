from tkinter import *
from tkinter import messagebox


class DeleteStudentUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Delete Student")
        self.root.geometry("400x250")

        Label(self.root,
              text="DELETE STUDENT",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Label(frame,text="Student ID",width=15).grid(row=0,column=0,pady=10)

        self.student_id = Entry(frame,width=25)
        self.student_id.grid(row=0,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Delete",
               width=15,
               command=self.delete_student).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def delete_student(self):

        sid = self.student_id.get()

        if sid == "":
            messagebox.showerror("Error","Enter Student ID")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete this student?"
        )

        if confirm:
            # later delete from database
            messagebox.showinfo("Success","Student Deleted Successfully")
            self.clear_form()


    def clear_form(self):

        self.student_id.delete(0,END)


    def run(self):
        self.root.mainloop()
