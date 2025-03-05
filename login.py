from customtkinter import *
from PIL import Image
import pillow_avif
from tkinter import messagebox

def login():
    username = usernameEntry.get()
    password = passwordEntry.get()
    if username == '' or password == '':
        messagebox.showerror('Error', 'All fields are required')
    elif username == 'admin' and password == 'admin':
        messagebox.showinfo('Success', 'Login Successful')
        root.destroy()
        import dashboard
    else:
        messagebox.showerror('Error', 'Invalid Username or Password')


# To create the window
root = CTk() 

root.geometry('930x478')
root.resizable(0,0)
root.title('Login Page')
image  = CTkImage(Image.open('image\cover.avif'),size = (930,478))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=0,y=0)
headingLabel = CTkLabel(root, text='Employee Management System', bg_color='#ffffff', font=('Goudy Old Style', 20, 'bold'), text_color='darkblue')

headingLabel.place(x=20,y=100)

usernameEntry = CTkEntry(root, placeholder_text="Enter Your Username", width = 180)
usernameEntry.place(x=50,y=150)
passwordEntry = CTkEntry(root, placeholder_text="Enter Your Password", width = 180, show='*')
passwordEntry.place(x=50,y=200)

loginButton =  CTkButton(root, text='Login', cursor = 'hand2', command=login)
loginButton.place(x=70,y=250)















root.mainloop() # To see the window-

