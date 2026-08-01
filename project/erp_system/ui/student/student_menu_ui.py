from tkinter import *
from ui.student.add_student_ui import AddStudentUI
from ui.student.view_student_ui import ViewStudentUI
from ui.student.update_student_ui import UpdateStudentUI
from ui.student.delete_student_ui import DeleteStudentUI
# later we will import other screens


class StudentMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Student Module")
        self.root.geometry("500x400")

        Label(self.root,
              text="STUDENT MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Add Student",
               width=20,
               height=2,
               command=self.open_add_student).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="View Students",
               width=20,
               height=2,
               command=self.open_view_students).grid(row=0,column=1,padx=10,pady=10)

        Button(frame,
               text="Update Student",
               width=20,
               height=2,
               command=self.open_update_student).grid(row=1,column=0,padx=10,pady=10)

        Button(frame,
               text="Delete Student",
               width=20,
               height=2,
               command=self.open_delete_student).grid(row=1,column=1,padx=10,pady=10)



    def open_add_student(self):

        add = AddStudentUI()

    def open_view_students(self):
        view = ViewStudentUI()
     
    def open_update_student(self):
        UpdateStudentUI()

    def open_delete_student(self):
        DeleteStudentUI()
 
    def run(self):
        self.root.mainloop()
