from tkinter import *
from tkinter import messagebox


class DeleteEnquiryUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("Delete Enquiry")
        self.root.geometry("350x200")

        Label(self.root,
              text="DELETE ENQUIRY",
              font=("Arial",18,"bold")).pack(pady=20)

        frame = Frame(self.root)
        frame.pack()

        Label(frame,text="Enquiry ID").grid(row=0,column=0,pady=10)

        self.enquiry_id = Entry(frame)
        self.enquiry_id.grid(row=0,column=1)

        Button(self.root,
               text="Delete",
               width=15,
               command=self.delete_enquiry).pack(pady=15)

    def delete_enquiry(self):

        eid = self.enquiry_id.get()

        if eid == "":
            messagebox.showerror("Error","Enter Enquiry ID")
            return

        confirm = messagebox.askyesno("Confirm","Delete this enquiry?")

        if confirm:
            messagebox.showinfo("Deleted","Enquiry Deleted Successfully")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = DeleteEnquiryUI()
    app.run()
