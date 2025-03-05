import pymysql
import tkinter as tk
from tkinter import messagebox

conn = pymysql.connect(host='localhost', user='root', password='1234')

def connectDb():
    global mycursor, conn
    try: 
        mycursor = conn.cursor() # This will help in executing SQL queries
    except:
        messagebox.showerror('Error', 'Something went wrong')
        return
    # This will create a new database if it does not exist
    mycursor.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data (Id VARCHAR(50), Name VARCHAR(255), Phone VARCHAR(255), Role VARCHAR(30), Gender VARCHAR(10), Salary VARCHAR(10))')
    



def idExists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE Id = %s',id)
    result = mycursor.fetchone()
    return result[0] > 0

def fetchEmployees():
    mycursor.execute('SELECT * FROM data')
    result = mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('UPDATE data SET Name = %s, Phone = %s, Role = %s, Gender = %s, Salary = %s WHERE Id = %s',(
        new_name, new_phone, new_role, new_gender, new_salary, id
    ))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE Id = %s',id)
    conn.commit()


def search_employee(option, value):
    mycursor.execute(f'SELECT * FROM data WHERE {option} = %s',value)
    result = mycursor.fetchall()
    return result

def deleteAllData():
    mycursor.execute('DELETE FROM data')
    conn.commit()


def insert(id,name,phone,role,gender,salary):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role, gender, salary))
    conn.commit()



connectDb()