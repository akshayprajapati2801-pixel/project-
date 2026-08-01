from tkinter import *
from tkinter import ttk


class ViewStudentUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("View Students")
        self.root.geometry("800x500")

        Label(self.root,
              text="STUDENT LIST",
              font=("Arial",18,"bold")).pack(pady=10)

        # Search Frame
        search_frame = Frame(self.root)
        search_frame.pack(pady=10)

        Label(search_frame,text="Search Student").grid(row=0,column=0,padx=5)

        self.search_box = Entry(search_frame,width=30)
        self.search_box.grid(row=0,column=1,padx=5)

        Button(search_frame,
               text="Search",
               width=12).grid(row=0,column=2,padx=5)

        Button(search_frame,
               text="Show All",
               width=12).grid(row=0,column=3,padx=5)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scrollbar_y = Scrollbar(table_frame)
        scrollbar_y.pack(side=RIGHT,fill=Y)

        scrollbar_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scrollbar_x.pack(side=BOTTOM,fill=X)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("id","name","course","phone","email","fees"),
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )

        scrollbar_y.config(command=self.student_table.yview)
        scrollbar_x.config(command=self.student_table.xview)

        self.student_table.heading("id",text="ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("fees",text="Fees")

        self.student_table["show"] = "headings"

        self.student_table.column("id",width=80)
        self.student_table.column("name",width=150)
        self.student_table.column("course",width=120)
        self.student_table.column("phone",width=120)
        self.student_table.column("email",width=180)
        self.student_table.column("fees",width=80)

        self.student_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=10)

        Button(btn_frame,
               text="Refresh",
               width=12,
               command=self.load_students).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Close",
               width=12,
               command=self.root.destroy).grid(row=0,column=1,padx=10)

        # Temporary data
        self.load_students()


    def load_students(self):

        # Clear table
        for row in self.student_table.get_children():
            self.student_table.delete(row)

        # Dummy data (later from database)
        students = [
            (1,"Rahul","Python","9876543210","rahul@gmail.com",5000),
            (2,"Amit","Java","9876543211","amit@gmail.com",6000),
            (3,"Neha","Data Science","9876543212","neha@gmail.com",8000)
        ]

        for student in students:
            self.student_table.insert("",END,values=student)


    def run(self):
        self.root.mainloop()


# testing
if __name__ == "__main__":
    app = ViewStudentUI()
    app.run()
