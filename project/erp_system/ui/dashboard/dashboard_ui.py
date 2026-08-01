from tkinter import *
from ui.student.student_menu_ui import StudentMenuUI
from ui.employee.employee_menu_ui import EmployeeMenuUI
from ui.course.course_menu_ui import CourseMenuUI
from ui.fee.fee_menu_ui import FeeMenuUI
from ui.attendance.attendance_menu_ui import AttendanceMenuUI
from ui.enquiry.enquiry_menu_ui import EnquiryMenuUI


class DashboardUI:

    def __init__(self):

        self.root = Tk()
        self.root.title("ERP Dashboard")
        self.root.geometry("700x500")

        Label(self.root,
              text="ERP DASHBOARD",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=40)

        #Button(frame,text="Student Module",width=20,height=2).grid(row=0,column=0,padx=10,pady=10)
        Button(frame,
            text="Student Module",
            width=20,
            height=2,
            command=self.open_student_module).grid(row=0,column=0,padx=10,pady=10)

        #Button(frame,text="Employee Module",width=20,height=2).grid(row=0,column=1,padx=10,pady=10)
        Button(frame,
            text="Employee Module",
            width=20,
            height=2,
            command=self.open_employee_module).grid(row=0,column=1,padx=10,pady=10)


        #Button(frame,text="Course Module",width=20,height=2).grid(row=1,column=0,padx=10,pady=10)
        Button(frame,
            text="Course Module",
            width=20,
            height=2,
            command=self.open_course_module).grid(row=1,column=0,padx=10,pady=10)

        #Button(frame,text="Fee Module",width=20,height=2).grid(row=1,column=1,padx=10,pady=10)
        Button(frame,
            text="Fee Module",
            width=20,
            height=2,
            command=self.open_fee_module).grid(row=1,column=1,padx=10,pady=10)

        #Button(frame,text="Attendance Module",width=20,height=2).grid(row=2,column=0,padx=10,pady=10)
        Button(frame,
            text="Attendance Module",
            width=20,
            height=2,
            command=self.open_attendance_module).grid(row=2,column=0,padx=10,pady=10)

        #Button(frame,text="Reports",width=20,height=2).grid(row=2,column=1,padx=10,pady=10)
        Button(frame,
               text="Enquiry Module",
               width=20,
               height=2,
               command=self.open_enquiry_module).grid(row=0,column=0,padx=10,pady=10)

    def open_student_module(self):
        student_menu = StudentMenuUI()
        student_menu.run()

    def open_employee_module(self):
        EmployeeMenuUI()
    
    def open_course_module(self):
        CourseMenuUI()

    def open_fee_module(self):
        FeeMenuUI()
    
    def open_attendance_module(self):
        AttendanceMenuUI()
    
    def open_enquiry_module(self):
        EnquiryMenuUI()

    def run(self):
        self.root.mainloop()
