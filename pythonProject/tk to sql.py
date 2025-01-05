import tkinter as tk
import pyodbc
# Replace these variables with your own database connection
server ='LAPTOP-QV5LPL6T\SQLEXPRESS'
database ='smirthi'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};')
cursor = conn.cursor()

def register():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("INSERT INTO login(username,password) VALUES(?,?)", (username, password))
    conn.commit()
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    result_label.config(text="Registration successful")
    cursor.close()
    conn.close()
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x450")
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_label = tk.Label(root, text="Password")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()
register_button = tk.Button(root, text="Register",command=register)
register_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()
