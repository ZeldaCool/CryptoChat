import tkinter as tk
from tkinter import ttk, Text
import storageServer
from storageServer import *

root = tk.Tk()
root.title('CryptoChat')
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tabControl.add(tab1, text ='Welcome!')
tabControl.add(tab2, text = 'Get Your SSH Key Here!')
tabControl.add(tab3, text ='Start Your Chat Here!')
tabControl.add(tab4, text ='Create An Account Or Login!')
tabControl.pack(expand = 1, fill ="both")
usernames = []
passwords = []
sshHistory = []
ttk.Label(tab1, text = "Welcome To CryptoChat!")
ttk.Label(tab2, text = "Get Your SSH Key Here!")
ttk.Label(tab3, text = "Start Your Encrypted Chat!")
boxthing =  tk.Label(tab3,text="Insert Your SSH Key Here To Start A Chat! Make Sure You Know This Person.")
something = tk.Label(tab1,text ="Have you ever wanted to be able to talk to people uninterrupted? Without Fear of stolen data? Well... It is here! Welcome to CryptoChat, an SSH based messaging system! ")
description = tk.Label(tab4, text ="Create an account here")
uname2 = tk.Label(tab4, text = "User Name")
userName = tk.Entry(tab4, width=20)
pword = tk.Label(tab4, text = "Password")
password = tk.Entry(tab4, width=20)
Username = tk.Label(tab4, text = "User Name")
Username_ = tk.Entry(tab4, width=20)
Password_ = tk.Label(tab4, text="Password")
Password__= tk.Entry(tab4, width=20)
def checker():
    supposedUsername = Username_.get()
    supposedPassword = Password__.get()
    thing = userName.get()
    thingthing = password.get()
    usernames.append(thing)
    passwords.append(thingthing)
    print('Username: ' + supposedUsername)
    print('Password: ' + supposedPassword)
    if supposedUsername in usernames and supposedPassword in passwords:
        print('Login Found! Welcome ' + supposedUsername)
    else:
      print('Login Not Found. Try Again or create an account!')
registrar = tk.Button(tab4, text = "Submit", command = checker)
supposedUsername = Username_.get()
supposedPassword = Password__.get()
signIn = tk.Label(tab4, text = "Sign In Here")
def store():
    thing = userName.get()
    thingthing = password.get()
    print('Username: ' + thing)
    print('Password: ' + thingthing)

something.pack()
ok = tk.Button(tab4, text="Register", command = store)

signIn.pack()
Username.pack()
Username_.pack()
Password_.pack()
Password__.pack()
registrar.pack()
description.pack()
uname2.pack()
userName.pack()
pword.pack()
password.pack()
boxthing.pack()
ok.pack()
root.mainloop()