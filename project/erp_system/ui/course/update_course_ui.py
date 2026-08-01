from tkinter import *
from tkinter import messagebox


class UpdateCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Update Course")
        self.root.geometry("400x350")

        Label(self.root,
              text="UPDATE COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        form = Frame(self.root)
        form.pack()

        # Course ID
        Label(form,text="Course ID",width=15,anchor="w").grid(row=0,column=0,pady=10)
        self.course_id = Entry(form,width=25)
        self.course_id.grid(row=0,column=1)

        Button(form,
               text="Search",
               command=self.search_course).grid(row=0,column=2,padx=5)

        # Course Name
        Label(form,text="Course Name",width=15,anchor="w").grid(row=1,column=0,pady=10)
        self.course_name = Entry(form,width=25)
        self.course_name.grid(row=1,column=1)

        # Duration
        Label(form,text="Duration",width=15,anchor="w").grid(row=2,column=0,pady=10)
        self.duration = Entry(form,width=25)
        self.duration.grid(row=2,column=1)

        # Fees
        Label(form,text="Fees",width=15,anchor="w").grid(row=3,column=0,pady=10)
        self.fees = Entry(form,width=25)
        self.fees.grid(row=3,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Update",
               width=15,
               command=self.update_course).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)


    def search_course(self):

        if self.course_id.get() == "":
            messagebox.showerror("Error","Enter Course ID")
            return

        # Dummy data (replace later with DB)
        self.course_name.delete(0,END)
        self.course_name.insert(0,"Python Programming")

        self.duration.delete(0,END)
        self.duration.insert(0,"3 Months")

        self.fees.delete(0,END)
        self.fees.insert(0,"8000")


    def update_course(self):

        if self.course_id.get() == "":
            messagebox.showerror("Error","Course ID required")
            return

        messagebox.showinfo("Success","Course Updated Successfully")


    def clear_form(self):

        self.course_id.delete(0,END)
        self.course_name.delete(0,END)
        self.duration.delete(0,END)
        self.fees.delete(0,END)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = UpdateCourseUI()
    app.run()
