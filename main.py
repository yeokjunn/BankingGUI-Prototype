from tkinter import *
import os
from PIL import Image, ImageTk

#Main Window Stuff
main_window = Tk() #instantiate window
main_window.title('Banking App')

#Image stuff
icon = Image.open('icon.png')
icon = icon.resize((225,225))
icon = ImageTk.PhotoImage(icon)
main_window.iconphoto(True,icon)


#Register Function
def register():
    #Globalise TextVariables
    global enter_name
    global enter_age
    global enter_gender
    global enter_password
    global fields_msg
    global registration_window

    registration_window = Toplevel(main_window) #create new registration window
    registration_window.title('Registration Page')

    #StringVar Initialisations
    enter_name = StringVar()
    enter_age = StringVar()
    enter_gender = StringVar()
    enter_password = StringVar()

    #Registraion Labels
    Label(registration_window,
          text='Key in your details below to register:',
          font=('Arial',14,'bold')
          ).grid(sticky=N,row=0,pady=20,padx=10)
    Label(registration_window,
          text='Username:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=1)
    Label(registration_window,
          text='Age:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=2)
    Label(registration_window,
          text='Gender:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=3)
    Label(registration_window,
          text='Password:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=4)
    fields_msg = Label(registration_window,
                       font=('Arial',11))
    fields_msg.grid(sticky=N,pady=7,row=6)

    #Registration Entry Boxes
    Entry(registration_window,
          textvariable=enter_name).grid(row=1)
    Entry(registration_window,
          textvariable=enter_age).grid(row=2)
    Entry(registration_window,
          textvariable=enter_gender).grid(row=3)
    Entry(registration_window,
          textvariable=enter_password,
          show='*').grid(row=4)

    #Finish Registration Button
    Button(registration_window,
           text='Finish Registration',
           command=finish_registration
           ).grid(sticky=N,pady=15,row=5)

#After 'Finish Registration' Function'
def finish_registration():
    name = enter_name.get()
    age = enter_age.get()
    gender = enter_gender.get()
    password = enter_password.get()

    #All fields cannot be empty
    if name == '' or age == '' or gender == '' or password == '':
        fields_msg.config(text='All fields required!',
                          fg='red',font=('Arial',11))
        return

    #create new file in directory
    path = r'C:\Users\kejun\PycharmProjects\BankingGui\account_names'
    file_path = os.path.join(path, name)
    all_accounts = os.listdir(path)
    if name in all_accounts:
        fields_msg.config(text='Account already EXISTS!', font=('Arial', 11), fg='red')
        return
    else:
        fields_msg.config(text='Account successfully created! Page will close.', font=('Arial', 11), fg='green')
        with open(file_path, 'w') as create_file:
            create_file.write(name + '\n' + age + '\n' + gender + '\n' + password)
            create_file.write('\n' + '0')
            create_file.close()
        lol = open(file_path, 'r')
        hi = lol.read()
        xd = hi.split('\n')
        print(xd)
        registration_window.after(1500, lambda : registration_window.destroy())

#Login Function
def login():
    #Globalise Variables
    global login_window
    global login_msg
    global login_name
    global login_password

    login_window = Toplevel(main_window) #create new log in window
    login_window.title('App Login Page')

    #StringVar() Initialisations
    login_name = StringVar()
    login_password = StringVar()

    #Login Labels
    Label(login_window,
          text='Key in your details below to login:',
          font=('Arial',14,'bold')
          ).grid(sticky=N,row=0,pady=20,padx=10)
    Label(login_window,
          text='Username:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=1)
    Label(login_window,
          text='Password:',
          font=('Arial',11,'underline')
          ).grid(sticky=W,pady=7,row=2)
    login_msg = Label(login_window,
                       font=('Arial',11))
    login_msg.grid(sticky=N,pady=7,row=3)

    #Login Entry Boxes
    Entry(login_window,textvariable=login_name).grid(row=1)
    Entry(login_window,textvariable=login_password,show='*').grid(row=2)

    #Login Button
    Button(login_window,
           text='Login',
           command=after_login
           ).grid(sticky=N,pady=15,row=5)

#After pressing Login Button
def after_login():
    global name
    global path
    global file_path
    name = login_name.get()
    password = login_password.get()

    path = r'C:\Users\kejun\PycharmProjects\BankingGui\account_names'
    file_path = os.path.join(path, name)
    all_accounts = os.listdir(path)
    #Checking correct username/ password
    if name in all_accounts:
        with open(file_path,'r') as correct_pw:
            lol = correct_pw.read()
            check_pw = lol.split('\n')
            if check_pw[3] == password:
                login_msg.config(text='Login Successful! Please wait...',fg='green')
                login_window.after(1000, lambda : login_window.destroy())
                main_window.after(1000, lambda : account()) #sends user to account page (successful login)
            else:
                login_msg.config(text='Incorrect Username/ Password! Try Again.',
                                 font=('Arial', 11), fg='red')
    else:
        login_msg.config(text='Incorrect Username/ Password! Try Again.',
                         font=('Arial',11),fg='red')

def account():
    global account_window

    account_window = Toplevel(main_window)
    account_window.title(f'Banking Account: {name}')
    account_window.config(background='yellow')

    #Account Labels
    Label(account_window,
          text='Welcome to your account!',
          font=('Calibri',18,'bold'),
          bg='yellow'
          ).grid(sticky=N,pady=12,padx=10,row=0)

    #Account Buttons
    Button(account_window,
           text='Deposit',
           font=('Calibri',12,'bold'),
           command=deposit
           ).grid(sticky=N, pady=15, row=1)
    Button(account_window,
           text='Withdraw',
           font=('Calibri', 12, 'bold'),
           command=withdraw
           ).grid(sticky=N, pady=15, row=2)
    Button(account_window,
           text='Account Info',
           font=('Calibri', 12, 'bold'),
           command=personal_info
           ).grid(sticky=N, pady=15, row=3)
    Button(account_window,
           text='Exit App',
           font=('Calibri', 12, 'bold'),
           command=exit
           ).grid(sticky=N, pady=15, row=4)

def isfloat(num): #Function to check if number entered in deposit/ withdraw is a number
    try:
        float(num)
        return True
    except ValueError:
        return False

#Deposit Function
def deposit():
    #Declarations
    global deposit_amount
    global deposit_msg
    global balance_msg
    #global current_balance
    deposit_amount = StringVar()

    #Open File to get current balance
    opening = open(file_path,'r')
    read = opening.readlines()
    current_balance = read[4]
    opening.close()

    deposit_window = Toplevel(account_window)
    deposit_window.title('Deposit Page')

    #Deposit Screen Labels
    Label(deposit_window,
          text='Deposit Page',
          font=('Calibri',15,'bold'), fg='dark green',
          ).grid(sticky=N,pady=10,padx=10,row=0)
    Label(deposit_window,
          text='Deposit Amount ($): ',
          font=('Calibri',11)
          ).grid(sticky=W,pady=10,row=1)
    balance_msg = Label(deposit_window,
          text=f'Account Balance: ${current_balance}',
          font=('Calibri',11)
          )
    balance_msg.grid(sticky=W,pady=10,row=2)
    deposit_msg = Label(deposit_window,
                        font=('Calibri',12),fg='red')
    deposit_msg.grid(sticky=N,pady=7,row=3)

    #Deposit Screen Entry
    Entry(deposit_window,
          textvariable=deposit_amount
          ).grid(row=1,column=1,padx=7)

    #Deposit Button
    Button(deposit_window,
           text='Confirm Deposit',
           font=('Calibri',12),
           command=after_deposit
           ).grid(sticky=N,pady=10,row=4)

def after_deposit():
    #Check if amount keyed in is valid
    if isfloat(deposit_amount.get()) == False:
        deposit_msg.config(text='Error! Key in a valid amount.', fg='red')
        return
    if deposit_amount.get()=='' or float(deposit_amount.get())<=0:
        deposit_msg.config(text='Error! Key in a valid amount.',fg='red')
        return

    #Updating Current Balance in File
    opening = open(file_path,'r')
    read = opening.read()
    file_data = read.split('\n')
    current_balance = file_data[4]
    new_balance = float(current_balance) + float(deposit_amount.get())
    file_data = read.replace(str(current_balance), str(new_balance))
    opening.close()
    opening = open(file_path,'w')
    opening.write(file_data)
    opening.close()

    #Update new balance on deposit screen
    balance_msg.config(text=f'Account Balance: ${str(new_balance)}',
                       font=('Calibri',11))
    deposit_msg.config(text='Balanced Updated!',
                       font=('Calibri',11),fg='green')

#Withdraw Function
def withdraw():
    #Declarations
    global withdraw_amount
    global withdraw_msg
    global balance_msg
    withdraw_amount = StringVar()

    #Open File to get current balance
    opening = open(file_path,'r')
    read = opening.readlines()
    current_balance = read[4]
    opening.close()

    withdraw_window = Toplevel(account_window)
    withdraw_window.title('Withdraw Page')

    #Withdraw Screen Labels
    Label(withdraw_window,
          text='Withdrawal Page',
          font=('Calibri',15,'bold'), fg='dark green',
          ).grid(sticky=N,pady=10,padx=10,row=0)
    Label(withdraw_window,
          text='Withdraw Amount ($): ',
          font=('Calibri',11)
          ).grid(sticky=W,pady=10,row=1)
    balance_msg = Label(withdraw_window,
          text=f'Account Balance: ${current_balance}',
          font=('Calibri',11)
          )
    balance_msg.grid(sticky=W,pady=10,row=2)
    withdraw_msg = Label(withdraw_window,
                        font=('Calibri',12),fg='red')
    withdraw_msg.grid(sticky=N,pady=7,row=3)

    #Withdraw Screen Entry
    Entry(withdraw_window,
          textvariable=withdraw_amount
          ).grid(row=1,column=1,padx=7)

    #Withdraw Button
    Button(withdraw_window,
           text='Confirm Withdrawal',
           font=('Calibri',12),
           command=after_withdraw
           ).grid(sticky=N,pady=10,row=4)

def after_withdraw():
    opening = open(file_path, 'r')
    read = opening.read()
    file_data = read.split('\n')
    current_balance = file_data[4]
    opening.close()
    # Check if amount keyed in is valid
    if isfloat(withdraw_amount.get()) == False:
        withdraw_msg.config(text='Error! Key in a valid amount.', fg='red')
        return
    if withdraw_amount.get() == '' or float(withdraw_amount.get()) <= 0:
        withdraw_msg.config(text='Error! Key in a valid amount.', fg='red')
        return
    if float(withdraw_amount.get()) > float(current_balance):
        withdraw_msg.config(text='Error! Not enough balance you poor dog.', fg='red')
        return

    # Updating Current Balance in File
    opening = open(file_path, 'r')
    read = opening.read()
    file_data = read.split('\n')
    current_balance = file_data[4]
    new_balance = float(current_balance) - float(withdraw_amount.get())
    file_data = read.replace(str(current_balance), str(new_balance))
    opening.close()
    opening = open(file_path, 'w')
    opening.write(file_data)
    opening.close()

    # Update new balance on deposit screen
    balance_msg.config(text=f'Account Balance: ${str(new_balance)}',
                       font=('Calibri', 11))
    withdraw_msg.config(text='Balanced Updated!',
                       font=('Calibri', 11), fg='green')

#Personal Details Function
def personal_info():
    info_page = Toplevel(account_window)
    info_page.title('Personal Details')

    #Opening file to get user info
    file_path = os.path.join(path, name)
    opening = open(file_path,'r')
    read = opening.readlines()
    age = read[1]
    gender = read[2]
    balance = read[4]

    #Labels
    Label(info_page,
          text='Your Account Details:',
          font=('Calibri',15,'bold','underline')
          ).grid(sticky=W,padx=7,pady=5,row=0)
    Label(info_page,
          text=f'Name: {name}'
          ).grid(sticky=W, padx=7, pady=5, row=1)
    Label(info_page,
          text=f'Age: {age}'
          ).grid(sticky=W, padx=7, pady=5, row=2)
    Label(info_page,
          text=f'Gender: {gender}'
          ).grid(sticky=W, padx=7, pady=5, row=3)
    Label(info_page,
          text=f'Balance ($): {balance}'
          ).grid(sticky=W, padx=7, pady=10, row=4)

#Exit App Function
def exit():
    main_window.destroy()

#Main Window Labels
main_window_label = Label(main_window,
                          text='Welcome to the Test Banking App',
                          font=('Arial',18,'bold'),
                          compound='bottom',
                          ).grid(sticky=N,row=0,pady=15,padx=20)
image_label = Label(main_window,
                    image=icon).grid(sticky=N,row=1,pady=5)
assurance_label = Label(main_window,
                        text='Test App #1',
                        font=('Arial',12),
                        ).grid(sticky=N,row=2,pady=5)

#Main Window Buttons
register_button = Button(main_window,
                         text='Register',
                         font=('Arial',10),
                         relief=RAISED,
                         command=register
                         ).grid(sticky=N,row=3,pady=10)
login_button = Button(main_window,
                      text='Login',
                      font=('Arial',10),
                      relief=RAISED,
                      command=login
                      ).grid(sticky=N,row=4,pady=10)

main_window.mainloop() #place window on computer screen