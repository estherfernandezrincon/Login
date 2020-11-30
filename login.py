from tkinter import *
from tkinter import ttk

import login


class Login(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=500, height=700)
        self.pack_propagate(False)
        s = ttk.Style()
        s.theme_use('alt')

      

        self.Forgot = ttk.Button(self, text="Forgot my password" )
        self.Forgot.pack(side= BOTTOM, fill=BOTH, expand=True, padx=30, pady=30)        
        
        self.label_usuario= ttk.Label(self,text="user:",font="Times")
        self.label_usuario.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.user=StringVar()
        

        self.entry_usuario=ttk.Entry (self,textvariable=self.user,cursor="pencil", foreground="red", font="Times,10", width=20)        
        self.entry_usuario.pack(side=TOP, fill= X, expand=True, padx=0, pady=2)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
           

        self.label_contraseña= ttk.Label(self, width=20, text="password:",font="Times")
        self.label_contraseña.pack(side=TOP, fill=BOTH, expand = True, padx=5, pady=5)
        self.password=StringVar()  

        self.entry_contraseña=ttk.Entry(self, textvariable=self.password,cursor="star", foreground="blue",font= "Times, 10", width=34, show='*')
        self.entry_contraseña.pack(side=TOP, fill= X, expand=True, padx=0, pady=2)
        self.separar=ttk.Separator(self, orient=HORIZONTAL)
        self.separar.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)

        self.Register= ttk.Button(self, text="New register")
        self.Register.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15) 
        
        self.Fb= ttk.Button(self, text="Inicial con Fb")
        self.Fb.pack(side=TOP, fill= BOTH, expand= True, padx=15, pady=15)

        self.Robot= ttk.Checkbutton(self, text="no soy un robot")
        self.Robot.pack(side=TOP, fill=BOTH, expand=False, padx=30, pady=30)
        
        self.botonA = ttk.Button(self, text="Aceptar", command=self.Validar)
        self.botonA.pack(side=LEFT, fill=BOTH, expand=True, padx=35, pady=35)
        self.botonB= ttk.Button(self,text="Cancelar", command=quit)
        self.botonB.pack(side=RIGHT, fill= BOTH, expand=True, padx=35, pady=35)
        
    def Validar(self):        

        if self.user.get() == "esther" and self.password.get() == "fer":
            label= ttk.Label( text="access successful ", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)

        elif self.user.get() != "esther" and self.password.get() != "fer":    
            label= ttk.Label( text=" wrong access", background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)
            
        else:
            label=ttk.Label( text="are you registered?",background="light grey",foreground="red", font="Times, 13", anchor=S)
            label.pack(side=BOTTOM, fill= BOTH, expand= True)


'''
    login = Tk()
    lbl = Label(login, text='Soy la ventana principal')
    login.pack_propagate(0)
    lbl.pack(side=TOP,pady=8)
    btn= Button(login, text='Clic para crear una ventana nueva')
    btn.pack(side=TOP, pady=8)

    def nuevaVentana():
        mw= Toplevel(login)
        mw.title= "REgistrate"
        mw.pack_propagate(0)
        #mw.grab-set_global()
        Label(mw, text="Haz tu registro").pack()
        btn.config(command=nuevaVentana)
         
'''

        


