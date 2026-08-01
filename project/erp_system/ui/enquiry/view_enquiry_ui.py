from tkinter import *
from tkinter import ttk


class ViewEnquiryUI:

    def __init__(self):

        self.root = Toplevel()
        self.root.title("View Enquiries")
        self.root.geometry("900x500")

        Label(self.root,
              text="ENQUIRY LIST",
              font=("Arial",18,"bold")).pack(pady=10)

        table_frame = Frame(self.root)
        table_frame.pack(pady=20)

        scroll_y = Scrollbar(table_frame)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.table = ttk.Treeview(
            table_frame,
            columns=("id","name","phone","course","source","status"),
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.table.yview)
        scroll_x.config(command=self.table.xview)

        self.table.heading("id",text="ID")
        self.table.heading("name",text="Name")
        self.table.heading("phone",text="Phone")
        self.table.heading("course",text="Course")
        self.table.heading("source",text="Source")
        self.table.heading("status",text="Status")

        self.table["show"] = "headings"

        self.table.pack()

        self.load_data()

    def load_data(self):

        enquiries = [
            (1,"Rahul","9876543210","Python","Website","New"),
            (2,"Neha","9876543211","Java","Walk-in","Follow-up"),
            (3,"Amit","9876543212","Data Science","Facebook","Interested")
        ]

        for row in enquiries:
            self.table.insert("",END,values=row)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ViewEnquiryUI()
    app.run()
