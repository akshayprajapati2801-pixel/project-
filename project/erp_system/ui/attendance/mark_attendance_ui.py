from tkinter import *
from tkinter import messagebox


class MarkAttendanceUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Mark Attendance")
        self.root.geometry("400x350")

        Label(self.root,
              text="MARK ATTENDANCE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Student ID").grid(row=0,column=0,pady=10)
        self.student_id = Entry(frame,width=25)
        self.student_id.grid(row=0,column=1)

        Label(frame,text="Course").grid(row=1,column=0,pady=10)
        self.course = Entry(frame,width=25)
        self.course.grid(row=1,column=1)

        Label(frame,text="Date").grid(row=2,column=0,pady=10)
        self.date = Entry(frame,width=25)
        self.date.grid(row=2,column=1)

        Label(frame,text="Status (Present/Absent)").grid(row=3,column=0,pady=10)
        self.status = Entry(frame,width=25)
        self.status.grid(row=3,column=1)

        Button(self.root,
               text="Submit",
               width=15,
               command=self.submit_attendance).pack(pady=20)


    def submit_attendance(self):

        if self.student_id.get() == "":
            messagebox.showerror("Error","Student ID required")
            return

        messagebox.showinfo("Success","Attendance Recorded")