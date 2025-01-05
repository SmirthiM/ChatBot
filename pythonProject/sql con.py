import tkinter as tk
import pyodbc
server = 'LAPTOP-QV5LPL6T\SQLEXPRESS'
database ='smirthi'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};')
cursor = conn.cursor()
conn.commit()
def insert_user():
    username = username_entry.get()
    password = password_entry.get()
    cursor.execute("INSERT INTO update_delete (username,password) VALUES (?, ?)", (username, password))
    conn.commit()
    refresh_user_list()
def update_user():
    selected_user = user_listbox.get(tk.ACTIVE)
    new_password = new_password_entry.get()
    cursor.execute("UPDATE update_delete SET Password = ? WHEREUsername = ?", (new_password, selected_user))
    conn.commit()
    refresh_user_list()
def delete_user():
    selected_user = user_listbox.get(tk.ACTIVE)
    cursor.execute("DELETE FROM update_delete WHERE Username =?", (selected_user,))
    conn.commit()
    refresh_user_list()
def refresh_user_list():
    user_listbox.delete(0, tk.END)
    cursor.execute(" SELECT Username FROM update_delete")
    for row in cursor.fetchall():
        user_listbox.insert(tk.END, row.Username)

root = tk.Tk()
root.title("User Registration Form")
root.geometry("400x450")
username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
register_button = tk.Button(root, text="Register",command=insert_user)
register_button.pack()

update_label = tk.Label(root, text="Update Password")
update_label.pack()
user_listbox = tk.Listbox(root)
user_listbox.pack()
new_password_label = tk.Label(root, text="New Password")
new_password_label.pack()
new_password_entry = tk.Entry(root, show="*")
new_password_entry.pack()
update_button = tk.Button(root, text="Update",command=update_user)
update_button.pack()


delete_label = tk.Label(root, text="Delete User")
delete_label.pack()
delete_button = tk.Button(root, text="Delete",command=delete_user)
delete_button.pack()

refresh_user_list()
root.mainloop()

cursor.close()
conn.close()