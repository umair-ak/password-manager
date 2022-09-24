# import statements

from tkinter import *
from tkinter import messagebox
from random import randint,shuffle,choice
import json
from json.decoder import JSONDecodeError


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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

def savepasswords():
    
    email = username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    data= {
        website:
            {
            "email":email,
            "password":password
            }
        }

    if len(website)== 0 or len(password)==0:
        messagebox.showwarning(title='Error',message="Please donot leave any field blank !")
        return
    if len(password)<8:
        messagebox.showinfo(title="Error",message='Your password too short')
        return
    is_okay = messagebox.askquestion(title=website,message=f'Please check the details \nUsername : {email}\nPassword : {password}')
    
    def addingdata():
        with open('data.json','w') as data_file:
            json.dump(data,data_file , indent=4)

    if is_okay=='yes':
        
        try:
            with open('data.json','r') as data_file:
                final_data = json.load(data_file)
                if website in final_data:
                    update_or_not = messagebox.askquestion(title=website,message=f'There is already an entry for {website} website do you want to update it')
                    if update_or_not == 'no':
                        return

        except FileNotFoundError :
            addingdata()
            
        except JSONDecodeError:
            addingdata()
            
        else:
            final_data.update(data)
            with open('data.json','w') as data_file:
                json.dump(final_data,data_file , indent=4)

        finally:
            password_entry.delete(0,END)
            website_entry.delete(0,END)
            website_entry.focus()
    else:
        pass

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #

def search():
    website = website_entry.get()
    try :
        with open('data.json','r') as data_file :
            data_dict = json.load(data_file)
            
            if website in data_dict :
                messagebox.showinfo(title=website , message=f"email : { data_dict[website]['email'] } \n password : {data_dict[website]['password']}")
            else:
                messagebox.showinfo(title='Error', message = f'There no such entry for the {website} website !')
    except FileNotFoundError:
        messagebox.showinfo(title='Error' , message=f'NO password have been stored ')
    
    except JSONDecodeError:
        messagebox.showinfo(title='Error' , message=f'There are no passwords stored !')

    
# ---------------------------- UI SETUP ------------------------------- #


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
website_entry = Entry(width=33)
website_entry.grid(row=2 , column=2 )
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

search = Button(text = 'search' , width=12,command=search)
search.grid(row = 2 , column = 3)
screen.mainloop()