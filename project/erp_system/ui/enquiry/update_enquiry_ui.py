from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class UpdateEnquiryUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Update Enquiry")
        self.root.geometry("450x400")

        Label(self.root,
              text="UPDATE ENQUIRY",
              font=("Arial",18,"bold")).pack(pady=15)

        frame = Frame(self.root)
        frame.pack(pady=10)

        Label(frame,text="Enquiry ID").grid(row=0,column=0,pady=5)
        self.enquiry_id = Entry(frame)
        self.enquiry_id.grid(row=0,column=1)

        Button(frame,
               text="Search",
               command=self.search).grid(row=0,column=2,padx=5)

        Label(frame,text="Name").grid(row=1,column=0,pady=5)
        self.name = Entry(frame)
        self.name.grid(row=1,column=1)

        Label(frame,text="Phone").grid(row=2,column=0,pady=5)
        self.phone = Entry(frame)
        self.phone.grid(row=2,column=1)

        Label(frame,text="Course").grid(row=3,column=0,pady=5)
        self.course = ttk.Combobox(frame,
                                   values=("Python","Java","Data Science","Web Development"))
        self.course.grid(row=3,column=1)

        Label(frame,text="Status").grid(row=4,column=0,pady=5)
        self.status = ttk.Combobox(frame,
                                   values=("New","Follow-up","Interested","Not Interested","Converted"))
        self.status.grid(row=4,column=1)

        Button(self.root,
               text="Update",
               width=15,
               command=self.update_enquiry).pack(pady=20)

    def search(self):

        messagebox.showinfo("Search","Search logic will connect to database")

    def update_enquiry(self):

        messagebox.showinfo("Success","Enquiry Updated Successfully")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = UpdateEnquiryUI()
    app.run()
