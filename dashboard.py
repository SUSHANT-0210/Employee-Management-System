from customtkinter import *
from PIL import Image
import pillow_avif
from tkinter import ttk, messagebox
import database as db # Since we are importing database file so our db is being created here

# Functions

def deleteAll():
    result = messagebox.askyesno('Delete All', 'Are you sure you want to delete all data?', icon='warning')
    if result:
        db.deleteAllData()
        treeViewData()
        clear()
        messagebox.showinfo('Success', 'All data deleted successfully')
    

def treeViewData():
    employees = db.fetchEmployees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert('', END, values=employee)

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    roleBox.set(role_options[0])
    salaryEntry.delete(0, END)
    genderBox.set(gender_options[0])


def selection(event):
    selected_item = tree.selection()
    if selected_item:
        clear()
        row =  tree.item(selected_item)['values'] # This will return a list of values of the selected row
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        phoneEntry.insert(0, row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0, row[5])


def updateEmployee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to update')
    else:
        id = idEntry.get()
        name = nameEntry.get()
        phone = phoneEntry.get()
        role = roleBox.get()
        salary = salaryEntry.get()
        gender = genderBox.get()
        db.update(id, name, phone,role,salary,gender)
        treeViewData()
        clear()
        messagebox.showinfo('Success', 'Employee Updated Successfully')

def deleteEmployee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Select data to delete')
    else:
        id = idEntry.get()
        db.delete(id)
        treeViewData()
        clear()
        messagebox.showinfo('Success', 'Employee Deleted Successfully')


def search_employee():
    if searchEntry.get() == '':
        messagebox.showerror('Error', 'Enter value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error', 'Select a search option')
    else:
        searched_data = db.search_employee(searchBox.get(), searchEntry.get())
        tree.delete(*tree.get_children())
        print(searched_data)
        if not searched_data:
            messagebox.showerror('Error', 'No data found')
        else:
            for data in searched_data:
                tree.insert('', END, values=data)


def showAll():
    treeViewData()
    searchEntry.delete(0, END)
    searchBox.set('Search By')


def addEmployee():
    if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or salaryEntry.get() == '' :
        messagebox.showerror('Error', 'All fields are required')
    elif db.idExists(idEntry.get()):
        messagebox.showerror('Error', 'ID already exists')
    elif not idEntry.get().isdigit():
        messagebox.showerror('Error', 'ID must be a number')
    else:
        id = idEntry.get()
        name = nameEntry.get()
        phone = phoneEntry.get()
        role = roleBox.get()
        salary = salaryEntry.get()
        gender = genderBox.get()
        db.insert(id,name,phone,role,gender,salary)
        treeViewData()
        clear()
        messagebox.showinfo('Success', 'Employee Added Successfully')


  

window = CTk()

window.title('Employee Management System')
window.geometry('1000x500+100+100') # + because to check x,y coordinates when window is opened
window.resizable(0,0)

image  = CTkImage(Image.open('D:\Projects\EmployeeManagementSystem\image\logo.jpg'),size = (1000,158))
imageLabel = CTkLabel(window, image=image, text='')
imageLabel.grid(row=0,column=0, columnspan=2)


# Creating Frames
leftFrame = CTkFrame(window)
leftFrame.grid(row=1,column=0)

idLabel = CTkLabel(leftFrame, text='ID:', font=('Arial', 18, 'bold'))
idLabel.grid(row=0,column=0, padx=10, pady=10)
idEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180)
idEntry.grid(row=0,column=1, padx=10, pady=10)

nameLabel = CTkLabel(leftFrame, text='Name:', font=('Arial', 18, 'bold'))
nameLabel.grid(row=1,column=0, padx=10, pady=10)
nameEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180)
nameEntry.grid(row=1,column=1, padx=10, pady=10)

phoneLabel = CTkLabel(leftFrame, text='Phone:', font=('Arial', 18, 'bold'))
phoneLabel.grid(row=2,column=0, padx=10, pady=10)
phoneEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180)
phoneEntry.grid(row=2,column=1, padx=10, pady=10)

roleLabel = CTkLabel(leftFrame, text='Role:', font=('Arial', 18, 'bold'))
roleLabel.grid(row=3,column=0, padx=10, pady=10)
role_options = ['Web Developer', 'Cloud Architect', 'UX/UI Designer', 'Data Scientist', 'Software Engineer', 'Network Engineer', 'Cyber Security Analyst', 'DevOps Engineer', 'Database Administrator', 'IT Support Specialist'] 
roleBox = CTkComboBox(leftFrame,values=role_options, font=('Arial', 15, 'bold'),width=180, state='readonly')
roleBox.grid(row=3,column=1, padx=10, pady=10 )
roleBox.set(role_options[0])

genderLabel = CTkLabel(leftFrame, text='Gender:', font=('Arial', 18, 'bold'))
genderLabel.grid(row=4,column=0, padx=10, pady=10)
gender_options = ['Male', 'Female', 'Other']
genderBox = CTkComboBox(leftFrame,values=gender_options, font=('Arial', 15, 'bold'),width=180, state='readonly')
genderBox.grid(row=4,column=1, padx=10, pady=10 )
genderBox.set(gender_options[0])

salaryLabel = CTkLabel(leftFrame, text='Salary:', font=('Arial', 18, 'bold'))
salaryLabel.grid(row=5,column=0, padx=10, pady=10)
salaryEntry = CTkEntry(leftFrame, font=('Arial', 15, 'bold'), width=180)
salaryEntry.grid(row=5,column=1, padx=10, pady=10)



rightFrame = CTkFrame(window) 
rightFrame.grid(row=1,column=1)

search_options = ['ID', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchBox = CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0 )
searchBox.set('Search By')
searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton = CTkButton(rightFrame, text='Search',width = 100, cursor='hand2', command = search_employee)
searchButton.grid(row=0,column=2)

showAllButton = CTkButton(rightFrame, text='Show All',width = 100, cursor='hand2', command = showAll)
showAllButton.grid(row=0,column=3, pady=5)


tree = ttk.Treeview(rightFrame, height=13)
tree.grid(row=1,column=0, columnspan=4)
tree['columns'] = ('Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary')
tree.heading('Id', text='Id')
tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Role', text='Role')
tree.heading('Gender', text='Gender')
tree.heading('Salary', text='Salary')

tree.config(show='headings')
tree.column('Id', width=100)
tree.column('Name', width=160)
tree.column('Phone', width=160)
tree.column('Role', width=200)
tree.column('Gender', width=100)
tree.column('Salary', width=140)    

style = ttk.Style() 
style.configure('Treeview.Heading', font=('Arial', 18, 'bold'))
style.configure('Treeview', font=('Arial', 13, 'bold'), rowheight=20, background='#161C30', foreground='white')

scrollBar = CTkScrollbar(rightFrame,orientation="vertical", command=tree.yview) # yview because we want to scroll vertically
scrollBar.grid(row=1,column=4, sticky='ns')

tree.config(yscrollcommand=scrollBar.set)

buttonFrame = CTkFrame(window)  
buttonFrame.grid(row=2,column=0, columnspan=2, pady = 10)

newButton = CTkButton(buttonFrame, text='New Employee',cursor='hand2', font=('Arial', 18, 'bold'), width=160, corner_radius=15, command = lambda: clear(True))
newButton.grid(row=0,column=0,pady = 5)

addButton = CTkButton(buttonFrame, text='Add Employee',cursor='hand2', font=('Arial', 18, 'bold'), width=160, corner_radius=15, command=addEmployee)
addButton.grid(row=0,column=1,pady = 5, padx = 5)

updateButton = CTkButton(buttonFrame, text='Update Employee',cursor='hand2', font=('Arial', 18, 'bold'), width=160, corner_radius=15, command = updateEmployee)
updateButton.grid(row=0,column=2,pady = 5, padx = 5)

deleteButton = CTkButton(buttonFrame, text='Delete Employee',cursor='hand2', font=('Arial', 18, 'bold'), width=160, corner_radius=15, command = deleteEmployee)
deleteButton.grid(row=0,column=3,pady = 5, padx = 5)

deleteAllButton = CTkButton(buttonFrame, text='Delete All',cursor='hand2', font=('Arial', 18, 'bold'), width=160, corner_radius=15, command = deleteAll)
deleteAllButton.grid(row=0,column=4,pady = 5, padx = 5)

treeViewData()

window.bind('<ButtonRelease>', selection)
window.mainloop()

