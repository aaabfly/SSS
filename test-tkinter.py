import Tkinter
# from login import Login, Register


class MainWindow:
    def __init__(self):
        self.app = Tkinter.Tk()
        self.app.title("Login with Python")
        self.app.geometry("300x250")
        self.label = Tkinter.Label(self.app, text="Welcome To App")
        self.label.place(x=95, y=40)
        self.Login = Tkinter.Button(self.app, text="Login",
                           pady=5, padx=30, command=register)
        self.register.place(x=100, y=150)

    def run(self):
        self.app.mainloop()


# def login():
#     loginTk = Login()
#     loginTk.run()

# def register():
#     registerTk = Register()
#     registerTk.run()


app = MainWindow()
app.run()
