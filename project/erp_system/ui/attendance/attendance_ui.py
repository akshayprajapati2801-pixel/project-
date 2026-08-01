from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class AttendanceUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Student Attendance")
        self.root.geometry("800x500")

        Label(self.root,
              text="ATTENDANCE MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=10)

        # Top Frame
        top_frame = Frame(self.root)
        top_frame.pack(pady=10)

        Label(top_frame,text="Course").grid(row=0,column=0,padx=5)

        self.course_box = ttk.Combobox(top_frame,width=20)
        self.course_box['values'] = ("Python","Java","Data Science")
        self.course_box.grid(row=0,column=1,padx=5)

        Label(top_frame,text="Date").grid(row=0,column=2,padx=5)

        self.date_entry = Entry(top_frame,width=15)
        self.date_entry.grid(row=0,column=3,padx=5)

        Button(top_frame,
               text="Load Students",
               command=self.load_students).grid(row=0,column=4,padx=10)

        # Table Frame
        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scrollbar = Scrollbar(table_frame)
        scrollbar.pack(side=RIGHT,fill=Y)

        self.att_table = ttk.Treeview(
            table_frame,
            columns=("id","name","status"),
            yscrollcommand=scrollbar.set
        )

        scrollbar.config(command=self.att_table.yview)

        self.att_table.heading("id",text="Student ID")
        self.att_table.heading("name",text="Student Name")
        self.att_table.heading("status",text="Status")

        self.att_table["show"] = "headings"

        self.att_table.column("id",width=100)
        self.att_table.column("name",width=200)
        self.att_table.column("status",width=100)

        self.att_table.pack()

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Mark Present",
               width=15,
               command=self.mark_present).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Mark Absent",
               width=15,
               command=self.mark_absent).grid(row=0,column=1,padx=10)

        Button(btn_frame,
               text="Save Attendance",
               width=15,
               command=self.save_attendance).grid(row=0,column=2,padx=10)


    def load_students(self):

        for row in self.att_table.get_children():
            self.att_table.delete(row)

        # Dummy student data
        students = [
            (101,"Rahul"),
            (102,"Amit"),
            (103,"Neha"),
            (104,"Pooja")
        ]

        for s in students:
            self.att_table.insert("",END,values=(s[0],s[1],"Absent"))


    def mark_present(self):

        selected = self.att_table.selection()

        for item in selected:
            values = list(self.att_table.item(item,"values"))
            values[2] = "Present"
            self.att_table.item(item,values=values)


    def mark_absent(self):

        selected = self.att_table.selection()

        for item in selected:
            values = list(self.att_table.item(item,"values"))
            values[2] = "Absent"
            self.att_table.item(item,values=values)


    def save_attendance(self):

        data = []

        for row in self.att_table.get_children():
            data.append(self.att_table.item(row,"values"))

        # Later connect database
        messagebox.showinfo("Saved","Attendance Saved Successfully")


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = AttendanceUI()
    app.run()
