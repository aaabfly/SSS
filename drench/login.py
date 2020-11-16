import tkinter as tk

class Login:
    """
    Class for Login
    @param username
    @param password
    """

    def __init__(self):
        self.loginWindow = tk.Tk()
        self.loginWindow.title("Account Login")
        self.loginWindow.geometry("300x250")
        self.label = tk.Label(selfloginWindow, text="Login")
        self.label.place(x=95, y=40)

        self.usernameS = tk.Stringvar()
        self.passwordS = tk.StringVar()

        self.usernameE = tk.Entry(
        self.loginWindow, relief=FLAT,textvariable=self.usernameS)
        self.usernameE.place(x=70, y=80)
        self.passwordE = tk.Entry(
        self.loginWindow, show="*", relief=FLAT,
         textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)

        self.username = self.usernameS.get()
        self.username = self.passwordS.get()

        self.submit = tk.Button(self.loginWindow, text="Submit",
         pady=5, padx=20, command=self.validate)
        self.submit.place(x=100, y=150)

    def validate(self):
        # Show Login message and Data validation(mada)
        tk.messagebox.showinfo("Successful", "Login Was Successful!")

class Register:
    """
    Class for Register
    @param username
    @param password
    """

    def __init__(self):

        self.registerWindow = tk.Tk()
        self.registerWindow.title("Account Registration")
        self.registerWindow.geometry("300x250")
        self.label = tk.Label(self.registerWindow, text="Register")
        self.label.place(x=95, y=40)

        self.usernameS = tk.StringVar()
        self.passwordS = tk.StringVar()

        self.usernameE = tk.Entry(self.registerWindow,
         relief=FLAT, textvariable=self,usernameE)
        self.usernameE.place(x=70, y=80)
        self.passwordE = tk.Entry(self.registerWindow, show="*",
         relief=FLAT, textvariable=self.passwordS)
        self.passwordE.place(x=70, y=120)
        self.submit = tk.Button(self.registerWindow,
         text="Submit", pady=5, padx, command=self.add)
        self.submit.place(x=100, y=150)

        self.username = self.usernameS.get()
        self.username = self.passwordS.get()

        def run(self):
            seld.registerWindow.mainloop()

        def add(self):
            # Show Register message and Data validation(mada)
            tk.messagebox.showinfo("Successful", "Username Was Added!")



        
