from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import requests
from sqlite3 import Error
from configparser import ConfigParser



#DBFILE= config ['DBFILE']


class Login(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=500, height=700)
        self.pack_propagate(False)


        self.Forgot = ttk.Button(self, text="Forgot my password" )
        self.Forgot.pack(side= BOTTOM, fill=BOTH, expand=True, padx=30, pady=30)        
        
        self.label_usuario= ttk.Label(self,width=20, text="user:",font="Times")
        self.label_usuario.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.user=StringVar()
        
        self.entry_usuario=ttk.Entry (self,textvariable=self.user, foreground="red", font="Times,10", width=20, state="disable")        
        self.entry_usuario.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.label_contraseña= ttk.Label(self, width=20, text="password:",font="Times")
        self.label_contraseña.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.password=StringVar()  

        self.entry_contraseña=ttk.Entry(self, textvariable=self.password,foreground="blue",font= "Times, 10", width=30, show='*', state="disabled")
        self.entry_contraseña.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.Register= ttk.Button(self, text="New register",command=self.Register)
        self.Register.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15) 

        self.YaEstoyRegistrado= ttk.Button(self, text="Already registered", command=self.AlreadyRegistered)
        self.YaEstoyRegistrado.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15) 

        self.Robot= ttk.Checkbutton(self, text="I'm not a robot")
        self.Robot.pack(side=TOP, fill=BOTH, expand=False, padx=30, pady=30)
        
        self.botonA = ttk.Button(self, text="Accept",command=self.Validar)
        self.botonA.pack(side=LEFT, fill=BOTH, expand=True, padx=35, pady=35)
        self.botonB= ttk.Button(self,text="Cancel", command=quit)
        self.botonB.pack(side=RIGHT, fill= BOTH, expand=True, padx=35, pady=35)

    def AlreadyRegistered(self):
        self.entry_usuario.config(state="normal")
        self.entry_contraseña.config(state="normal")

        
    def Validar(self):        
        usuario = self.user.get()
        contraseña = self.password.get()

        conn = sqlite3.connect("MYLOGIN/data/base_de_datos.db")
        c = conn.cursor()

        c.execute( 'SELECT Name, password from REGISTRO;')
        datos_introducidos = c.fetchall()

        if usuario in datos_introducidos[0] and contraseña in datos_introducidos[0]:           
            label= ttk.Label( text="access successful ", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)

        elif usuario in datos_introducidos[0] or contraseña in datos_introducidos[0]:
            label= ttk.Label( text="usuario o contraseña incorrectos ", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)    

        else:
            label= ttk.Label( text="¿¿estás registrado??", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)


        
    def Register(self):
        newWindow= Toplevel()
        newWindow.geometry("350x450")
        newWindow.grab_set()
        
        self.label_nuevo= ttk.Label(newWindow, text= "New Register")
        self.label_nuevo.pack()

        self.lbl_usuario= ttk.Label(newWindow,text="username:",font="Times")
        self.lbl_usuario.pack(side=TOP, fill=BOTH, expand = True, padx=1, pady=1)
        self.newuser=StringVar() 

        self.entry_user=ttk.Entry (newWindow,textvariable=self.newuser , foreground="red", font="Times,10", width=5)        
        self.entry_user.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        
        self.lbl_pass= ttk.Label(newWindow,text="password :",font="Times")
        self.lbl_pass.pack(side=TOP, fill=BOTH, expand = True, ipadx=1, ipady=1)
        self.newpass=StringVar() 

        self.entry_passw=ttk.Entry (newWindow,textvariable=self.newpass , foreground="red", font="Times,10", width=5, show='*')        
        self.entry_passw.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        
        self.button_nuevo=ttk.Button(newWindow, text= "Create Account", command= self.Datos)
        self.button_nuevo.pack(side=TOP)


    def Datos(self):
        NewUser = self.newuser.get()
        NewPass = self.newpass.get()

        conn = sqlite3.connect("MYLOGIN/data/base_de_datos.db")
        c = conn.cursor()

        c.execute('INSERT INTO REGISTRO ( Name, Password ) VALUES (?,?) ;' , 
                (NewUser, NewPass))

        conn.commit()
        conn.close()
    
        

        
  





        


