import os
import shutil
import hashlib
import stat
from zipfile import ZipFile
from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.title("Decrypt Build and Hash")
root.configure(background = "white")

def SelectFile():

    def submit_pass():
        pass_text = pass_entry.get()
        hash_pass = hashlib.md5(pass_text.encode()).hexdigest()
        next_text = StringVar()
        next_label = Label(root,textvariable = next_text,bg="white")
        next_label.grid(row = 4,column = 0)
        if hash_text == hash_pass:
            pass_button.config(state = "disabled")
            next_text.set( "Password is correct ")
            with ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall(directory_name + '/decrypt')
            with ZipFile(directory_name + '/decrypt/build.zip', 'r') as zip_ref:
                zip_ref.extractall(directory_name + '/decrypt')
            os.remove('hash.txt')
            os.remove('build.zip')
            final_label = Label(root,text= "Operation ended you can exit",bg="white")
            final_label.grid(row = 5, column = 0)
        else:
            next_text.set("Try again")
        

    filename = askopenfilename()
    repository_name = filename.split('/')[-1]
    directory_name = filename.split('/')[:-1:1]
    directory_name = '/'.join(directory_name)
    print(directory_name)

    select_button.config(state = "disabled")
    with ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall(directory_name + '/decrypt')
    os.chdir(directory_name + '/decrypt')

    hash_text = ""
    with open('hash.txt') as f:
        hash_text = f.readlines()[0]
    os.remove('hash.txt')
    os.remove('build.zip')
    pass_label = Label(root,text="Enter the hib file password:",bg="white")
    pass_label.grid(row = 1,column = 0)
    pass_entry = Entry(root,width = 50)
    pass_entry.grid(row = 2,column = 0)
    pass_button = Button(root,text ="Submit",bg="white",padx = 50,command = submit_pass)
    pass_button.grid(row = 3,column = 0)
    
    

select_button = Button(root,padx = 140,text ="Select File",bg="white",command = SelectFile )
select_button.grid(row = 0,column = 0)

root.mainloop()