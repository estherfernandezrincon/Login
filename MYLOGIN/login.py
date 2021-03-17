from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3

from sqlite3 import Error
from configparser import ConfigParser

c= ConfigParser()
c.read('MYLOGIN/config.ini')
config = c ['DEFAULT']
DBFILE = config ['DBFILE']


class Login(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=700, height=500)
        self.pack_propagate(False)       
        
        self.label_usuario= ttk.Label(self,width=20, text="user:",font="Times")
        self.label_usuario.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.usuario=StringVar()
        
        self.entry_usuario=ttk.Entry (self,textvariable=self.usuario, foreground="red", font="Times,10", width=20, state="disable")        
        self.entry_usuario.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.label_contraseña= ttk.Label(self, width=20, text="password:",font="Times")
        self.label_contraseña.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.contraseña=StringVar()  

        self.entry_contraseña=ttk.Entry(self, textvariable=self.contraseña, foreground="blue",font= "Times, 10", width=30, show='*', state="disabled")
        self.entry_contraseña.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.Register= ttk.Button(self, text="New register",command=self.Register)
        self.Register.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15) 

        self.YaEstoyRegistrado= ttk.Button(self, text="Already registered", command=self.AlreadyRegistered)
        self.YaEstoyRegistrado.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15) 

        
        self.botonA = ttk.Button(self, text="Accept",command=self.Validar)
        self.botonA.pack(side=LEFT, fill=BOTH, expand=True, padx=35, pady=35)
        self.botonB= ttk.Button(self,text="Cancel", command=quit)
        self.botonB.pack(side=RIGHT, fill= BOTH, expand=True, padx=35, pady=35)

    def AlreadyRegistered(self):
        self.entry_usuario.config(state="normal")
        self.entry_contraseña.config(state="normal")

        
    def Validar(self):        
        usuario = self.usuario.get()
        contraseña = self.contraseña.get()
      

        conn = sqlite3.connect("MYLOGIN/data/base_de_datos.db")
        c = conn.cursor()

        c.execute( 'SELECT Name, Password FROM REGISTRO;')
        datos_introducidos = c.fetchall()
  
        conn.commit()
        conn.close()
   

        a=[]
        b=[]
        
        for usuario in datos_introducidos:
            if usuario in datos_introducidos :
                a.append(usuario[0])             


        for contraseña in datos_introducidos:
            if contraseña in datos_introducidos:
                b.append(contraseña[1])

      
 

    
        if self.usuario.get() in a and self.contraseña.get() in b: 
                
            label= ttk.Label( text="acceso correcto ", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)


        elif self.usuario.get()in a or self.contraseña.get() in b:
            label= ttk.Label( text="usuario o contraseña incorrectos", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)

        else:
            label= ttk.Label( text="Debes registrarte primero", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)
                
        if self.usuario != "" and self.contraseña != "":
            self.usuario.set("")
            self.contraseña.set("")
        
        
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

        self.entry_passw=ttk.Entry (newWindow, textvariable=self.newpass , foreground="red", font="Times,10", width=5, show='*')        
        self.entry_passw.pack(side=TOP, fill= X, expand=True, padx=25, pady=25)
        
        self.button_nuevo=ttk.Button(newWindow, text= "Create Account", command= self.Datos)
        self.button_nuevo.pack(side=TOP)

        


    def Datos(self):

        okRegistro= Toplevel()
        okRegistro.geometry("450x150")
        okRegistro.grab_set()

        NewUser = self.newuser.get()
        NewPass = self.newpass.get()

        longitud = len(NewPass)
        upper = NewPass.upper()
      
        if longitud <= 8 and NewPass != upper:
            self.label= ttk.Label(okRegistro, text="La contraseña debe contener al menos 9 caracteres y una mayuscula ", background="light grey",foreground="red", font="Times, 13", anchor=CENTER)
            self.label.pack(side=BOTTOM, fill= BOTH, expand= True)                   
        else:
            self.label= ttk.Label(okRegistro,  text="registro correcto ", background="light grey",foreground="green", font="Times, 13", anchor=CENTER)
            self.label.pack(side=BOTTOM, fill= BOTH, expand= True)

        conn = sqlite3.connect("MYLOGIN/data/base_de_datos.db")
        c = conn.cursor()

        c.execute('INSERT INTO REGISTRO ( Name, Password ) VALUES (?,?) ;' , 
                (NewUser, NewPass))

        print(NewUser)

        conn.commit()
        conn.close()
        

        if self.newuser != "" and self.newpass != "":
            self.newuser.set("")
            self.newpass.set("")

        
               
            

            

        
         
        

        
  





        


