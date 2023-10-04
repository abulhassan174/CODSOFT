from tkinter import *
import string
import random

#Function to generate password
def password_generate():
    password = ''

    try:
        pas_len = int(pas_len_entry.get())
        if pas_len < 8:
            res_label.config(text='Password length must be greater than 8. Please try again')
            return
    except ValueError:
        res_label.config(text='Please enter valid length.')
        return

    pas_complexity = pas_complexity_var.get()

    #if password complexity is Low then generated password has only English letters
    if pas_complexity == 'Low':
        for i in range(pas_len):
            password += random.choice(string.ascii_letters)

    # if password complexity is Medium then generated password has English letters and 2 digits
    elif pas_complexity == 'Medium':
        for i in range(pas_len - 2):
            password += random.choice(string.ascii_letters)
        for i in range(2):
            password += random.choice(string.digits)

    # if password complexity is High then generated password has English letters, 1 digit and 2 special characters
    elif pas_complexity == 'High':
        for i in range(pas_len - 3):
            password += random.choice(string.ascii_letters)
        for i in range(2):
            password += random.choice(string.punctuation)
        password += random.choice(string.digits)


    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)


    res_label.config(text="Generated Password: "+password)


#creating main window
root = Tk()
root.geometry('600x300')

root.title('Password Generator')
root.wm_iconbitmap('password.ico')

#Password length input
pas_len_label = Label(root, text='Enter the length of your password:', bg='grey', font='10')
pas_len_label.pack()

pas_len_entry = Entry(root, font=10, )
pas_len_entry.pack()

#password complexity input
pas_complexity_label = Label(root, text='Enter your password complexity:', bg='grey', font='10')
pas_complexity_label.pack()

pas_complexity_var = StringVar()
pas_complexity_var.set('Low')

#Choosing password complexity buttons
complexity_low = Radiobutton(root, text='Low', variable=pas_complexity_var, value='Low', font=7)
complexity_low.pack()
complexity_medium = Radiobutton(root, text='Medium', variable=pas_complexity_var, value='Medium', font=7)
complexity_medium.pack()
complexity_high = Radiobutton(root, text='High', variable=pas_complexity_var, value='High', font=7)
complexity_high.pack()

#Password generate button
pas_generate_butt = Button(root, text='Generate Password', command= password_generate, bg='orange', font=10)
pas_generate_butt.pack()

#Generated password label
res_label = Label(root, text='', font=10, bg='grey', padx=700)
res_label.pack()

root.mainloop()


