from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from service.enquiry_service import EnquiryService
from model.enquiry import Enquiry


class AddEnquiryUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Add Enquiry")
        self.root.geometry("500x450")

        Label(self.root,
              text="ADD NEW ENQUIRY",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack(pady=10)

        # Name
        Label(frame,text="Name",width=15,anchor="w").grid(row=0,column=0,pady=5)
        self.name = Entry(frame,width=30)
        self.name.grid(row=0,column=1)

        # Phone
        Label(frame,text="Phone",width=15,anchor="w").grid(row=1,column=0,pady=5)
        self.phone = Entry(frame,width=30)
        self.phone.grid(row=1,column=1)

        # Email
        Label(frame,text="Email",width=15,anchor="w").grid(row=2,column=0,pady=5)
        self.email = Entry(frame,width=30)
        self.email.grid(row=2,column=1)

        # Course
        Label(frame,text="Course",width=15,anchor="w").grid(row=3,column=0,pady=5)

        self.course = ttk.Combobox(frame,width=27)
        self.course["values"] = ("Python","Java","Data Science","Web Development","C++")
        self.course.grid(row=3,column=1)

        # Source
        Label(frame,text="Source",width=15,anchor="w").grid(row=4,column=0,pady=5)

        self.source = ttk.Combobox(frame,width=27)
        self.source["values"] = ("Walk-in","Website","Facebook","Instagram","Referral")
        self.source.grid(row=4,column=1)

        # Status
        Label(frame,text="Status",width=15,anchor="w").grid(row=5,column=0,pady=5)

        self.status = ttk.Combobox(frame,width=27)
        self.status["values"] = ("New","Follow-up","Interested","Not Interested","Converted")
        self.status.grid(row=5,column=1)

        # Remark
        Label(frame,text="Remark",width=15,anchor="w").grid(row=6,column=0,pady=5)
        self.remark = Entry(frame,width=30)
        self.remark.grid(row=6,column=1)

        # Buttons
        btn_frame = Frame(self.root)
        btn_frame.pack(pady=20)

        Button(btn_frame,
               text="Save",
               width=15,
               command=self.save_enquiry).grid(row=0,column=0,padx=10)

        Button(btn_frame,
               text="Clear",
               width=15,
               command=self.clear_form).grid(row=0,column=1,padx=10)

        Button(btn_frame,
               text="Close",
               width=15,
               command=self.root.destroy).grid(row=0,column=2,padx=10)


    def save_enquiry(self):
        service = EnquiryService()
        enquiry = Enquiry(
            None,
            self.name.get(),
            self.phone.get(),
            self.email.get(),
            self.course.get(),
            self.source.get(),
            self.status.get(),
            self.remark.get()
        )
        service.save_enquiry(enquiry)

        # name = self.name.get()
        # phone = self.phone.get()

        # if name == "" or phone == "":
        #     messagebox.showerror("Error","Name and Phone are required")
        #     return

        # # Later connect Service layer
        messagebox.showinfo("Success","Enquiry Saved Successfully")
        self.clear_form()


    def clear_form(self):

        self.name.delete(0,END)
        self.phone.delete(0,END)
        self.email.delete(0,END)
        self.course.set("")
        self.source.set("")
        self.status.set("")
        self.remark.delete(0,END)

    def run(self):
        self.root.mainloop()

# testing
# if __name__ == "__main__":
#     app = AddEnquiryUI()
#     app.run()