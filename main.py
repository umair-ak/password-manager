# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def savepasswords():
    
    pass
    # website_entry.
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

screen = Tk()
screen.title('Password Manager')
screen.config(padx=40,pady=40)
logo = Canvas(height=200,width=200)
logo.grid(row=1, column=2)

img = PhotoImage(file='logo.png')
logo.create_image(100,100,image= img)


website = Label(text='website :',font=('comic sans' , 15))
website.grid(row=2,column=1)
website.config(pady=3)
website_entry = Entry(width=50)
website_entry.grid(row=2 , column=2 , columnspan=2)
website_entry.focus()

username = Label(text='username :',font=('comic sans' , 15))
username.grid(row=3, column=1)
username.config(pady=3)
username_entry = Entry(width=50,show='uak1911@gmail.com')
username_entry.grid(row=3, column=2, columnspan=2)

password = Label(text='password :',font=('comic sans' , 15))
password.grid(row=4,column=1)
password.config(pady=3)
password_entry = Entry(width= 33,textvariable='password',show = '*')
password_entry.grid(row=4,column=2)
show = Button(text='show' , width=12)
show.grid(row=4,column=3)
show.config(pady=3)

generate = Button(text='generate',width=12)
generate.grid(row=5,column=3)
addbtn = Button(text='ADD',width=14,command=savepasswords)
addbtn.grid(row=5,column=2)


screen.mainloop()