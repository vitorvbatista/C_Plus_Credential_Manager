# import libraries
import sqlite3
import pyperclip
import pandas as pd
import tkinter as tk
import os

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cryptography.fernet import Fernet
from datetime import datetime


class Login:
    def __init__(self) -> None:
        pass

    # validate password input in login page
    @staticmethod
    def password_validation(password_sent, login_window):

        # Establish connection with sqlite
        database_connection = sqlite3.connect('CS+')
        connection_cursor = database_connection.cursor()

        connection_cursor.execute(f'''SELECT auth_plain FROM authentication WHERE auth_plain = "{password_sent}"''')
        result = connection_cursor.fetchall()

        if len(result) != 0:
            Main_page(login_window)
        else:
            Error.error()

    # Get sent password and call validation
    @staticmethod
    def sendPassword(pass_input, login_window):
        login_window.deiconify()
        password_input = pass_input.get()
        Login.password_validation(password_input, login_window)

    # load login page
    @staticmethod
    def login_page():

        login_page = Tk()
        login_page.title("Login")
        login_page.geometry("230x120")
        login_page.configure(bg="#0073E6")

        welcome_text = Label(login_page,
                             text="Crypto+  Credential Manager",
                             justify=CENTER, bg="#0073E6", fg="White", font='bold 10')

        welcome_text.grid(column=0, row=0, padx=35, pady=0)

        Input_password = Entry(login_page, show="*")
        Input_password.grid(column=0, row=1, pady=10)

        sign_in_button = Button(login_page,
                                width=10,
                                text="Sign in",
                                bg="#ffffff",
                                borderwidth=1,
                                command=lambda: Login.sendPassword(Input_password, login_page))

        sign_in_button.grid(column=0, row=2, padx=0, pady=15)

        login_page.mainloop()


class Error:
    def __init__(self) -> None:
        pass

    # reload login page
    @staticmethod
    def return_to_login(error_page):
        error_page.destroy()

    # load error page if password is incorrect
    @staticmethod
    def error():
        error_page = Tk()
        error_page.title("Cripto+ Error")
        error_page.geometry("250x100")
        error_page.configure(bg="#0073E6")

        # Display error text label
        error_text = Label(error_page,
                           text="Incorrect password",
                           justify=LEFT, bg="#0073E6", fg="Black", font='bold 10')

        error_text.grid(column=0, row=0, padx=20, pady=0)

        return_button = Button(error_page,
                               width=20,
                               text="Return to Sign In page",
                               bg="#ffffff",
                               borderwidth=1,
                               command=lambda: Error.return_to_login(error_page))

        return_button.grid(column=0, row=2, padx=50, pady=15)

        error_page.mainloop()


# Load main page where all options are displayed
def Main_page(login_window):
    login_window.destroy()

    main_page = Tk()
    main_page.title("C+")
    main_page.geometry("200x270")
    main_page.configure(bg="#0073E6")

    # Display welcome text
    welcome_text = Label(main_page,
                         text="Choose your action!",
                         justify=LEFT, bg="#0073E6", fg="White", font='bold 10')

    welcome_text.grid(column=0, row=1, padx=45, pady=0)

    # Get password button - This button will call select class, it will serve to get password and sent it to clipboard
    button_get = Button(main_page,
                        width=20,
                        text="GET PASSWORD",
                        bg="#ffffff",
                        borderwidth=1,
                        command=lambda: Select.select_screen())
    button_get.grid(column=0, row=2, padx=0, pady=10)

    # Insert button - This button will call insert class, it will serve to insert credential data
    button_insert = Button(main_page,
                           width=20,
                           text="INSERT PASSWORD",
                           bg="#ffffff",
                           borderwidth=1,
                           command=lambda: Insert.insert_screen())
    button_insert.grid(column=0, row=3, padx=0, pady=10)

    # Delete button - This button will call delete class, it will drop inputted credential
    button_delete = Button(main_page,
                           width=20,
                           text="DELETE PASSWORD",
                           bg="#ffffff",
                           borderwidth=1,
                           command=lambda: Delete.delete_screen())
    button_delete.grid(column=0, row=4, padx=0, pady=10)

    # Update button - This button will call update class, it will serve to update credential data
    button_update = Button(main_page,
                           width=20,
                           text="UPDATE PASSWORD",
                           bg="#ffffff",
                           borderwidth=1,
                           command=lambda: Update.update_screen())
    button_update.grid(column=0, row=5, padx=0, pady=10)

    # Expiry date button - This button will call GetExpiryDate class, it will serve to display all expired credentials
    # or all credentials closed to expire (five days close to it)
    button_expiry = Button(main_page,
                           width=20,
                           text="GET EXPIRY DATES",
                           bg="#ffffff",
                           borderwidth=1,
                           command=lambda: GetExpiryDate.get())
    button_expiry.grid(column=0, row=6, padx=0, pady=10)

    main_page.mainloop()


class Insert:
    def __init__(self) -> None:
        pass

    # Insert all sent input to database (table PASS)
    @staticmethod
    def insert(name, user, password, description, expiry_date, insert_window):
        # Get all entries
        get_name = name.get()
        get_username = user.get()
        get_password = password.get()
        get_description = description.get()
        get_expiry_date = expiry_date.get()

        # Format expiry date to dd/mm/yyyy
        get_expiry_date = datetime.strptime(get_expiry_date, '%d/%m/%Y').date()

        # Establish fixed key and encrypt password
        key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
        fernet = Fernet(key)
        encrypt_password = fernet.encrypt(get_password.encode())
        encrypt_password = encrypt_password.decode("utf8")

        # Establish connection with sqlite database
        connection = sqlite3.connect('CS+')
        connection_cursor = connection.cursor()

        # Insert command, passing all sent data from interface
        connection_cursor.execute(f"""
                      INSERT INTO pass (pass_name, pass_user, pass_plain, pass_observation, pass_expiry_date)
                            VALUES(
                            '{get_name}',
                             '{get_username}',
                              '{encrypt_password}',
                               '{get_description}',
                               '{get_expiry_date}')""")

        connection.commit()

        # Display a message box after command above
        messagebox.showinfo("Message", "Registered")

        # Erase all inputs if user wants to insert another credential
        name.delete(0, "end")
        user.delete(0, "end")
        password.delete(0, "end")
        description.delete(0, "end")

        # Kill insert window to enable previous screen
        insert_window.destroy()

    # load insert screen
    @staticmethod
    def insert_screen():
        Insert_page = Tk()
        Insert_page.title("C+ Insert")
        Insert_page.geometry("400x250")
        Insert_page.configure(bg="#0073E6")

        # Display credential name input and its entry
        Text_name = Label(Insert_page, text="Credential name", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_name.grid(padx=30, pady=15)
        Input_name = Entry(Insert_page, width=25)
        Input_name.grid(column=1, row=0)

        # Display Username input and its entry
        Text_user = Label(Insert_page, text="Username", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_user.grid(padx=.5, pady=.5)
        Input_user = Entry(Insert_page, width=25)
        Input_user.grid(column=1, row=1)

        # Display Password input and its entry
        Text_password = Label(Insert_page, text="Password", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_password.grid(padx=30, pady=15)
        Input_password = Entry(Insert_page, show="*", width=25)
        Input_password.grid(column=1, row=2)

        # Display Expiry date input and its entry
        Text_expiry_date = Label(Insert_page, text="Expiry date",
                                 justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_expiry_date.grid(padx=.5, pady=.5)
        Input_expiry_date = Entry(Insert_page, width=25)
        Input_expiry_date.grid(column=1, row=3)

        # Display Description input and its entry
        Text_description = Label(Insert_page, text="Description",
                                 justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_description.grid(padx=15, pady=15)
        Input_description = Entry(Insert_page, width=25)
        Input_description.grid(column=1, row=4)

        # Insert button that call Insert command
        insert_button = Button(Insert_page,
                               width=10,
                               text="Insert",
                               bg="#ffffff",
                               borderwidth=1,
                               command=lambda: Insert.insert(Input_name,
                                                             Input_user,
                                                             Input_password,
                                                             Input_description,
                                                             Input_expiry_date,
                                                             Insert_page))

        insert_button.grid(column=1, row=5, pady=5)

        Insert_page.mainloop()


class Select:
    def __init__(self) -> None:
        pass

    # Select script that sends password to user clipboard
    @staticmethod
    def select(name, select_window):

        # Get credential name and set sqlite connection
        get_name = name.get()
        connection = sqlite3.connect('CS+')

        # Try to select data. If receives an Index error, show an error message box. On the opposite, send password to
        # user clipboard
        try:
            # Establish connection to sqlite database and select password
            connection_cursor = connection.cursor()

            connection_cursor.execute(f"""
                          SELECT pass_plain FROM pass WHERE pass_name = '{get_name}'""")
            result = connection_cursor.fetchall()
            password_fetched = result[0][0]

            # Set key to decrypt selected password
            key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(password_fetched.encode())
            decrypted_password = decrypted_password.decode("utf8")

        except IndexError:
            messagebox.showinfo("Alert", "Couldn't find this password")
            name.delete(0, "end")
        else:
            messagebox.showinfo("Message", "Sent to clipboard!")
            pyperclip.copy(decrypted_password)
            select_window.destroy()

    @staticmethod
    def select_screen():
        select_page = Tk()
        select_page.title("C+ Select")
        select_page.geometry("400x100")
        select_page.configure(bg="#0073E6")

        # Display a label and credential name entry
        Text_name = Label(select_page, text="Credential name", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_name.grid(padx=30, pady=15)
        Input_name = Entry(select_page, width=25)
        Input_name.grid(column=1, row=0)

        # Select button, that call select function
        select_button = Button(select_page,
                               width=10,
                               text="Get",
                               bg="#ffffff",
                               borderwidth=1,
                               command=lambda: Select.select(Input_name, select_page))

        select_button.grid(column=1, row=3, pady=6)

        select_page.mainloop()


class Delete:
    def __init__(self) -> None:
        pass

    @staticmethod
    def delete(name, password, delete_window):

        # Get credential name and password
        get_name = name.get()
        get_password = password.get()

        # Establish connection to sqlite database
        connection = sqlite3.connect('CS+')

        # Try to select password based on credential name, if raised an Index error, show a specific message box
        # if didn't find anything
        try:
            connection_cursor = connection.cursor()
            connection_cursor.execute(f"""SELECT pass_plain FROM PASS WHERE pass_name = '{get_name}'""")

            result_fetch_password = connection_cursor.fetchall()
            fetched_password = result_fetch_password[0][0]

        except IndexError:
            messagebox.showinfo("Alert", "This credential doesn't not exist")

            name.delete(0, "end")
            password.delete(0, "end")

        else:

            # Set key to decrypt password. At this step, should decrypt to compare the credential inside database and
            # inputted credential
            key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(fetched_password).decode()

            # If inputted password is the same as in database send DELETE command to finish operation. On the opposite
            # show a messagebox because isn't the same password
            if get_password == decrypted_password:
                connection_cursor.execute(
                    f"""DELETE FROM PASS WHERE pass_name = '{get_name}' AND pass_plain = '{fetched_password}'""")
                connection.commit()
                messagebox.showinfo("Message", "Deleted password")
            else:
                messagebox.showinfo("Alert", "Password doesn't not correspond to this credential")
                name.delete(0, "end")
                password.delete(0, "end")

        delete_window.destroy()

    # Load delete screen
    @staticmethod
    def delete_screen():
        Delete_page = Tk()
        Delete_page.title("C+ Delete")
        Delete_page.geometry("400x150")
        Delete_page.configure(bg="#0073E6")

        # Display a label and credential name entry
        Text_name = Label(Delete_page, text="Credential name", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_name.grid(padx=30, pady=15)
        Input_name = Entry(Delete_page, width=25)
        Input_name.grid(column=1, row=0)

        # Display a label and password entry
        Text_password = Label(Delete_page, text="Password", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_password.grid(padx=.5, pady=.5)
        Input_password = Entry(Delete_page, show="*", width=25)
        Input_password.grid(column=1, row=1)

        delete_button = Button(Delete_page,
                               width=10,
                               text="Delete",
                               bg="#ffffff",
                               borderwidth=1,
                               command=lambda: Delete.delete(Input_name, Input_password, Delete_page))

        delete_button.grid(column=1, row=4, pady=20)

        Delete_page.mainloop()


class Update:
    def __init__(self) -> None:
        pass

    # Update all sent input to database (table PASS)
    @staticmethod
    def update(name, password, new_password, expiry_date, update_window):

        # Read all inputs
        get_name = name.get()
        get_password = password.get()
        get_new_password = new_password.get()
        get_expiry_date = expiry_date.get()
        get_expiry_date = datetime.strptime(get_expiry_date, '%d/%m/%Y').date()

        # Set connection with database
        connection = sqlite3.connect('CS+')

        # Try to execute a select pass plain from database, decrypt and compare with inputted password. If both are
        # equal, then will update all credential data inputted
        try:
            connection_cursor = connection.cursor()

            connection_cursor.execute(f"""SELECT pass_plain FROM PASS WHERE pass_name = '{get_name}'""")
            result_fetch = connection_cursor.fetchall()
            password_fetched = result_fetch[0][0]

            key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(password_fetched.encode())
            decrypted_password = decrypted_password.decode("utf8")

        except IndexError:

            # If IndexError is thrown, show an error messagebox
            messagebox.showinfo("Alert", "Couldn't find this password")
            name.delete(0, "end")

        else:

            # Compare both passwords, inputted and selected. If correct, update, on the contrary, show an error message
            if decrypted_password == get_password:

                try:
                    key = b'26XVYFv-85Q_ESbCiY3-ag-LS2TwQBbyKWKxV9YQ-EY='
                    fernet = Fernet(key)
                    encrypt_password = fernet.encrypt(get_new_password.encode())
                    encrypt_password = encrypt_password.decode("utf8")

                    connection = sqlite3.connect('CS+')
                    connection_cursor = connection.cursor()

                    connection_cursor.execute(f"""
                                  UPDATE PASS SET pass_plain = '{encrypt_password}',
                                   pass_expiry_date = '{get_expiry_date}'
                                   WHERE pass_name = '{get_name}'""")
                    connection.commit()

                except IndexError:
                    messagebox.showinfo("Alert", "SQLite error while updating your password")
                else:
                    messagebox.showinfo("Message", "Password updated")
                    name.delete(0, "end")
                    password.delete(0, "end")
                    new_password.delete(0, "end")

                    update_window.destroy()
            else:
                messagebox.showinfo("Alert", "Password input is incorrect")
                name.delete(0, "end")
                password.delete(0, "end")
                new_password.delete(0, "end")

    @staticmethod
    def update_screen():
        update_screen = Tk()
        update_screen.title("C+ Update")
        update_screen.geometry("400x200")
        update_screen.configure(bg="#0073E6")

        Text_name = Label(update_screen, text="Credential name", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_name.grid(padx=30, pady=15)
        Input_name = Entry(update_screen, width=25)
        Input_name.grid(column=1, row=0)

        Text_password = Label(update_screen, text="Password", justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_password.grid(padx=.5, pady=.5)
        Input_password = Entry(update_screen, show="*", width=25)
        Input_password.grid(column=1, row=1)

        Text_description = Label(update_screen, text="New password",
                                 justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_description.grid(padx=30, pady=15)
        Input_new_password = Entry(update_screen, show="*", width=25)
        Input_new_password.grid(column=1, row=2)

        Text_expiry_date = Label(update_screen, text="Expiry Date",
                                 justify=LEFT, bg="#0073E6", fg="White", font='bold 10')
        Text_expiry_date.grid(padx=10, pady=1)
        Input_expiry_date = Entry(update_screen, width=25)
        Input_expiry_date.grid(column=1, row=3)

        update_button = Button(update_screen, width=10, text="Update", bg="#ffffff", borderwidth=1,
                               command=lambda: Update.update(Input_name,
                                                             Input_password,
                                                             Input_new_password,
                                                             Input_expiry_date,
                                                             update_screen))

        update_button.grid(column=1, row=4, pady=15)

        update_screen.mainloop()


class GetExpiryDate:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get():

        # Try to select all expiry dates < 5 days
        try:
            connection = sqlite3.connect('CS+')

            dataframe = pd.read_sql_query(
                "SELECT pass_name AS Name, pass_expiry_date AS Expiry_Date, pass_observation AS Observation"
                " FROM PASS WHERE pass_expiry_date < DATE('now','+5 days')", connection)

            connection.commit()

        # If IndexError is thrown, show a messagebox with SQLite error
        except IndexError:
            messagebox.showinfo("Alert", "SQLite Database Error")

        else:

            # Check if dataframe is empty. It means the above command doesn't return values
            if dataframe.empty:
                messagebox.showinfo("Message", "There are no passwords to expire")
            else:
                GetExpiryDate.get_expiry_date_screen(dataframe)

    # load get expiry date screen
    @staticmethod
    def get_expiry_date_screen(credentials):
        root_screen = tk.Tk()
        root_screen.title('C+ Expiry Dates')
        root_screen.configure(bg="#0073E6")

        # Get dataframe with all credentials with expiry dates < +5 days
        dataframe = pd.DataFrame(credentials)
        cols = list(dataframe.columns)

        # Set style for display dataframe
        style = ttk.Style(root_screen)
        style.theme_use("clam")
        style.configure("Treeview", background="#0073E6", fieldbackground="White", foreground="white")
        # common_auth
        # Pack treeview
        treeview = ttk.Treeview(root_screen, height=15)
        treeview.pack()
        treeview["columns"] = cols

        # Both 'for' loops intends to get and input dataframe on the screen
        for i in cols:
            treeview.column(i, anchor="w", width=150)
            treeview.heading(i, text=i, anchor='w')

        for index, row in dataframe.iterrows():
            treeview.insert("", 0, text=f'nº {index}', values=list(row))

        root_screen.mainloop()


if __name__ == '__main__':
    Login.login_page()
