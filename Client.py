import tkinter as tk
import datetime as dt
import requests as req
import time 

#Config
SizeX = str(500)
SizeY = str(100)

PosOffsetX = str(300)
PosOffsetY = str(300)

#Functions
def Format(n):
   return time.strftime('%H:%M:%S', time.gmtime(n))

class Interface:
    def __init__(self):
        self.Mode = None

        self.LoginEmail = ""
        self.LoginPassword = ""
        self.CreateEmail = ""
        self.CreatePassword = ""

        self.Root = tk.Tk()
        self.Root.geometry(f"{SizeX}x{SizeY}+{PosOffsetX}+{PosOffsetY}")
        self.Root.title("Verification")

        self.Frame = tk.Frame(self.Root, width = 50)
        self.Frame.pack()


        #Interface
        

        self.Ok = tk.Button(self.Frame, text = "Ok", command = self.OkClick, width = 10)
        self.CreateAccount = tk.Button(self.Frame, text = "Create", command = self.OnCreateAccount, width = 10)
        self.Login = tk.Button(self.Frame, text = "Login", command = self.OnLogin, width = 10)

        self.CounterLabel = tk.Label(self.Frame, text = "hi", height = 3)
        self.CounterLabel.config(fg = "Red")
        self.Entry = tk.Entry(self.Frame, width = 40)
        
        #Pack
        self.CounterLabel.pack()
        self.Entry.pack()
        self.Ok.pack(side = tk.RIGHT)
        self.CreateAccount.pack(side = tk.RIGHT)
        self.Login.pack(side = tk.LEFT)

    #Callbacks
    def OkClick(self):
        if self.Mode == "Login":
            if self.SequenceOrder == 1:
                self.IncrementSequence()
                self.LoginCredentialsEmail(self.Entry.get())
                self.ClearEntry()
                self.PasswordMode(True)
                self.CounterLabel.config(text = "Please enter your password")
            elif self.SequenceOrder == 2:
                self.LoginCredentialsPassword(self.Entry.get())
                self.ClearEntry()
                self.PasswordMode(False)
            else:
                return self.OnLogin()

        elif self.Mode == "Create":
            if self.SequenceOrder == 1:
                self.IncrementSequence()
                self.CreateCredentialsEmail(self.Entry.get())
                self.ClearEntry()
                self.PasswordMode(True)
                self.CounterLabel.config(text = "Please enter the new password")
            elif self.SequenceOrder == 2:
                self.CreateCredentialsPassword(self.Entry.get())
                self.ClearEntry()
                self.PasswordMode(False)
                
            else:
                return self.OnCreateAccount()

    def OnCreateAccount(self):
       self.PasswordMode(False)
       self.Mode = "Create"
       self.SequenceOrder = 1
       self.CounterLabel.config(text = "Please enter the Email ID you want to \nregister with")

    def OnLogin(self):
        self.PasswordMode(False)
        self.Mode = "Login"
        self.SequenceOrder = 1
        self.CounterLabel.config(text = "Please enter your Email ID to Login")

    #Other
    def ClearEntry(self):
        self.Entry.delete(0, len(self.Entry.get()))

    def IncrementSequence(self):
        self.SequenceOrder += 1

    def PasswordMode(self, bool):
        if bool:
            self.Entry.config(show = "*")
        else:
            self.Entry.config(show = "")

    def InactiveMode(self, bool):
        if bool:
            self.Entry.config(state = tk.DISABLED)
        else:
            self.Entry.config(state = tk.NORMAL)

    #Credentials
    def LoginCredentialsEmail(self, email):
        self.LoginEmail = email
    def LoginCredentialsPassword(self, password):
        self.LoginPassword = password

    def CreateCredentialsEmail(self, email):
        self.CreateEmail = email
    def CreateCredentialsPassword(self, password):
        self.CreatePassword = password

    #Main
    def execute(self):
        self.OnLogin()
        return self.Root

Root = Interface().execute()
Root.mainloop()