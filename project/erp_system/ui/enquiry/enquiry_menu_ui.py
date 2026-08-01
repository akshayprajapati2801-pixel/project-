from tkinter import *

from ui.enquiry.add_enquiry_ui import AddEnquiryUI
from ui.enquiry.view_enquiry_ui import ViewEnquiryUI
from ui.enquiry.update_enquiry_ui import UpdateEnquiryUI
from ui.enquiry.delete_enquiry_ui import DeleteEnquiryUI


class EnquiryMenuUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Enquiry Module")
        self.root.geometry("500x400")

        Label(self.root,
              text="ENQUIRY MANAGEMENT",
              font=("Arial",18,"bold")).pack(pady=30)

        frame = Frame(self.root)
        frame.pack(pady=20)

        Button(frame,
               text="Add Enquiry",
               width=20,
               height=2,
               command=self.open_add_enquiry).grid(row=0,column=0,padx=10,pady=10)

        Button(frame,
               text="View Enquiries",
               width=20,
               height=2,
               command=self.open_view_enquiry).grid(row=0,column=1,padx=10,pady=10)

        Button(frame,
               text="Update Enquiry",
               width=20,
               height=2,
               command=self.open_update_enquiry).grid(row=1,column=0,padx=10,pady=10)

        Button(frame,
               text="Delete Enquiry",
               width=20,
               height=2,
               command=self.open_delete_enquiry).grid(row=1,column=1,padx=10,pady=10)


    def open_add_enquiry(self):
        AddEnquiryUI()


    def open_view_enquiry(self):
        ViewEnquiryUI()


    def open_update_enquiry(self):
        UpdateEnquiryUI()


    def open_delete_enquiry(self):
        DeleteEnquiryUI()


    def run(self):
        self.root.mainloop()

