from tkinter import *
from tkinter import messagebox


class AddCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Add Course")
        self.root.geometry("500x400")

        Label(self.root,
              text="ADD COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack(pady=10)

        # Course ID
        Label(form, text="Course ID", width=15, anchor="w").grid(row=0, column=0, pady=10)
        self.course_id = Entry(form, width=30)
        self.course_id.grid(row=0, column=1)

        # Course Name
        Label(form, text="Course Name", width=15, anchor="w").grid(row=1, column=0, pady=10)
        self.course_name = Entry(form, width=30)
        self.course_name.grid(row=1, column=1)

        # Duration
        Label(form, text="Duration", width=15, anchor="w").grid(row=2, column=0, pady=10)
        self.duration = Entry(form, width=30)
        self.duration.grid(row=2, column=1)

        # Fees
        Label(form, text="Course Fees", width=15, anchor="w").grid(row=3, column=0, pady=10)
        self.fees = Entry(form, width=30)
        self.fees.grid(row=3, column=1)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=30)

        Button(btn_frame,
               text="Save Course",
               width=15,
               command=self.save_course).grid(row=0, column=0, padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0, column=1, padx=10)


    def save_course(self):

        cid = self.course_id.get()
        cname = self.course_name.get()

        if cid == "" or cname == "":
            messagebox.showerror("Error", "Course ID and Course Name required")
            return

        # Temporary logic (later connect service layer + database)
        messagebox.showinfo("Success", "Course Saved Successfully")

        self.clear_form()


    def clear_form(self):

        self.course_id.delete(0, END)
        self.course_name.delete(0, END)
        self.duration.delete(0, END)
        self.fees.delete(0, END)


    def run(self):
        self.root.mainloop()


# testing purpose
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    app = AddCourseUI()
    app.run()
