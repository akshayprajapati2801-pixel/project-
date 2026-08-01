from tkinter import *
from tkinter import messagebox


class DeleteCourseUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Delete Course")
        self.root.geometry("350x200")

        Label(self.root,
              text="DELETE COURSE",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Course ID",width=15).grid(row=0,column=0,pady=10)

        self.course_id = Entry(frame,width=20)
        self.course_id.grid(row=0,column=1)

        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Delete",
               width=12,
               command=self.delete_course).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=12,
               command=self.clear_field).grid(row=0,column=1,padx=10)


    def delete_course(self):

        if self.course_id.get() == "":
            messagebox.showerror("Error","Enter Course ID")
            return

        confirm = messagebox.askyesno("Confirm","Delete this course?")

        if confirm:
            # later connect database
            messagebox.showinfo("Deleted","Course Deleted Successfully")
            self.clear_field()


    def clear_field(self):
        self.course_id.delete(0,END)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DeleteCourseUI()
    app.run()
