from tkinter import *

from ui.course.add_course_ui import AddCourseUI
from ui.course.view_course_ui import ViewCourseUI
from ui.course.update_course_ui import UpdateCourseUI
from ui.course.delete_course_ui import DeleteCourseUI


class CourseMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Course Module")
        self.root.geometry("500x400")

        Label(self.root,
              text="COURSE MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Add Course",
               width=20,
               height=2,
               command=self.open_add_course).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="View Courses",
               width=20,
               height=2,
               command=self.open_view_course).grid(row=0,column=1,padx=10,pady=10)

        Button(frame,
               text="Update Course",
               width=20,
               height=2,
               command=self.open_update_course).grid(row=1,column=0,padx=10,pady=10)

        Button(frame,
               text="Delete Course",
               width=20,
               height=2,
               command=self.open_delete_course).grid(row=1,column=1,padx=10,pady=10)


    def open_add_course(self):
        AddCourseUI()

    def open_view_course(self):
        ViewCourseUI()

    def open_update_course(self):
        UpdateCourseUI()

    def open_delete_course(self):
        DeleteCourseUI()


    def run(self):
        self.root.mainloop()


# testing purpose
if __name__ == "__main__":
    app = CourseMenuUI()
    app.run()
