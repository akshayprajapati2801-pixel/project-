from tkinter import *
from tkinter import messagebox
from ui.dashboard.dashboard_ui import DashboardUI


class LoginUI:

    def __init__(self):

        self.root = Tk()
        self.root.title("ERP Login")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        Label(self.root,text="ERP SYSTEM LOGIN",
              font=("Arial",16,"bold")).pack(pady=20)

        Label(self.root,text="Username").pack()

        self.username = Entry(self.root,width=30)
        self.username.pack(pady=5)

        Label(self.root,text="Password").pack()

        self.password = Entry(self.root,show="*",width=30)
        self.password.pack(pady=5)

        Button(self.root,
               text="Login",
               width=20,
               command=self.login).pack(pady=20)


    def login(self):

        uname = self.username.get()
        pwd = self.password.get()

        # temporary login logic
        if uname == "admin" and pwd == "1234":

            messagebox.showinfo("Success","Login Successful")

            self.root.destroy()

            dashboard = DashboardUI()
            dashboard.run()

        else:
            messagebox.showerror("Error","Invalid Login")


    def run(self):
        self.root.mainloop()
