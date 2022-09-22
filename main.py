# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint,shuffle,choice
def gen_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters+password_numbers+password_symbols
    password_list1 = shuffle(password_list)
    final_password = "".join(password_list)
    password_entry.insert(0,final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def savepasswords():
    
    email = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    if len(website)== 0 or len(password)==0:
        messagebox.showwarning(title='Error',message="Please donot leave any field blank !")
        return
    if len(password)<8:
        messagebox.showinfo(title="Error",message='Your password too short')
        return
    is_okay = messagebox.askquestion(title=website,message=f'the entered details are\nUsername : {email}\nPassword : {password}')
    if is_okay=='yes':
        with open('data.csv',"a") as passwordfile:
            passwordfile.write(f"{website},{email},{password}\n")

        password_entry.delete(0,END)
        website_entry.delete(0,END)
        website_entry.focus()
    else:
        pass


    
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

screen = Tk()
screen.title('Password Manager')
screen.config(padx=40,pady=40)
logo = Canvas(height=200,width=200)
logo.grid(row=1, column=2)

img = PhotoImage(file='logo.png')
logo.create_image(100,100,image= img)

# labels
website = Label(text='website :',font=('comic sans' , 15))
website.grid(row=2,column=1)
website.config(pady=3)

username = Label(text='username :',font=('comic sans' , 15))
username.grid(row=3, column=1)
username.config(pady=3)

password = Label(text='password :',font=('comic sans' , 15))
password.grid(row=4,column=1)
password.config(pady=3)

# entries
website_entry = Entry(width=50)
website_entry.grid(row=2 , column=2 , columnspan=2)
website_entry.focus()

username_entry = Entry(width=50)
username_entry.grid(row=3, column=2, columnspan=2)
username_entry.insert(0,"uak1911@gmail.com")

password_entry = Entry(width= 33)
password_entry.grid(row=4,column=2)

# buttons


generate = Button(text='generate',width=12,command=gen_password)
generate.grid(row=4,column=3)

addbtn = Button(text='ADD',width=14,command=savepasswords)
addbtn.grid(row=5,column=2)


screen.mainloop()