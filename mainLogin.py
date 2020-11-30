from tkinter import *
from tkinter import ttk

import login

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Login")

        self.login= login.Login(self)
        self.login.pack(side=TOP)






if __name__=="__main__":
    app= MainApp()
    app.mainloop()