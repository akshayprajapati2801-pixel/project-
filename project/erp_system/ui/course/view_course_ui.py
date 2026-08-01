from tkinter import *
from tkinter import ttk


class ViewCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("View Courses")
        self.root.geometry("750x450")

        Label(self.root,
              text="COURSE LIST",
              font=("Arial",18,"bold")).pack(pady=10)

        # Search Frame
        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame, text="Search Course").grid(row=0, column=0, padx=5)

        self.search_box = Entry(search_frame, width=30)
        self.search_box.grid(row=0, column=1, padx=5)

        Button(search_frame,
               text="Search",
               width=12).grid(row=0, column=2, padx=5)

        Button(search_frame,
               text="Show All",
               width=12,
               command=self.load_courses).grid(row=0, column=3, padx=5)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scrollbar_y = Scrollbar(table_frame)
        scrollbar_y.pack(side=RIGHT, fill=Y)

        scrollbar_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM, fill=X)

        self.course_table = ttk.Treeview(
            table_frame,
            columns=("id", "name", "duration", "fees"),
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        scrollbar_y.config(command=self.course_table.yview)
        scrollbar_x.config(command=self.course_table.xview)

        self.course_table.heading("id", text="Course ID")
        self.course_table.heading("name", text="Course Name")
        self.course_table.heading("duration", text="Duration")
        self.course_table.heading("fees", text="Fees")

        self.course_table["show"] = "headings"

        self.course_table.column("id", width=100)
        self.course_table.column("name", width=200)
        self.course_table.column("duration", width=150)
        self.course_table.column("fees", width=100)

        self.course_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=10)

        Button(btn_frame,
               text="Refresh",
               width=12,
               command=self.load_courses).grid(row=0, column=0, padx=10)

        Button(btn_frame,
               text="Close",
               width=12,
               command=self.root.destroy).grid(row=0, column=1, padx=10)

        self.load_courses()


    def load_courses(self):

        # Clear table
        for row in self.course_table.get_children():
            self.course_table.delete(row)

        # Temporary dummy data
        courses = [
            (101, "Python Programming", "3 Months", 8000),
            (102, "Java Development", "4 Months", 10000),
            (103, "Data Science", "6 Months", 15000),
        ]

        for course in courses:
            self.course_table.insert("", END, values=course)


    def run(self):
        self.root.mainloop()


# Testing
if __name__ == "__main__":
    app = ViewCourseUI()
    app.run()
