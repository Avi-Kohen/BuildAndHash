import os
import shutil
import hashlib
import stat
from zipfile import ZipFile
from tkinter import *

def submitButtonClick():
    submitButton.config(state="disabled")
    entered_text = repository.get()
    repository_name = entered_text.split('/')[1]
    os.system('git clone https://github.com/' + entered_text)
    os.chdir(repository_name)
    os.system("git log --pretty=format:'%h,%an,%ar,%s' > commit_log.txt" )
    os.chdir("..")
    shutil.move(repository_name + "/" + "commit_log.txt" ,os.getcwd() + "/" + "commit_log.txt")
    texteula= open("commit_log.txt").read()
    log_found_label = Label(root,text= "A log file found and opened",bg = "white")
    log_found_label.grid(row=1,column = 0)
    # define master
    Eula = Toplevel(root)
    Eula.title('Commit Log')

    # Vertical (y) Scroll Bar
    scroll = Scrollbar(Eula)
    scroll.pack(side=RIGHT, fill=Y)

    def declined():
        Eula.destroy()
        exit_label = Label(root,text= "Commit declined you can exit the program",bg = "white")
        exit_label.grid(row=2,column = 0)

    def accepted():
        Eula.destroy()
        accept_label = Label(root,text= "Commit accepted creating zip file",bg = "white")
        accept_label.grid(row=2,column = 0)

        shutil.make_archive("Build", 'zip', repository_name)
        def del_rw(action, name, exc):
            os.chmod(name, stat.S_IWRITE)
            os.remove(name)
        shutil.rmtree(repository_name, onerror=del_rw)
        os.remove('commit_log.txt')
        
        def submit_pass():
            pass_button.config(state = "disabled")
            hash_result = hashlib.md5(pass_text.get().encode())
            with open('hash.txt', 'w') as f:
                f.write(str(hash_result))
            zipObj = ZipFile('Build_with_Hash.zip', 'w')
            zipObj.write('Build.zip')
            zipObj.write('hash.txt')
            zipObj.close()
            os.remove("Build.zip")
            os.remove('hash.txt')
            done_label = Label(root,text="zip file created, Operation ended you can exit the program",bg="white")
            done_label.grid(row=4)
        pass_label = Label(root,text= "Enter hash password",bg = "white")
        pass_label.grid(row=3,column = 0)
        pass_text = Entry(root,width = 40)
        pass_text.grid(row=3,column = 1)
        pass_button = Button(root,text="Submit",padx = 40,command = submit_pass)
        pass_button.grid(row=3,column = 2)
    # Text Widget
    eula = Text(Eula, wrap=NONE, yscrollcommand=scroll.set)
    eula.insert("1.0", texteula)
    eula.pack()
    button= Button(Eula,text='Accept',command=accepted )
    button.pack(side=LEFT)
    button2= Button(Eula,text='Decline',command = declined)
    button2.pack(side=RIGHT)

    # Configure the scrollbars
    scroll.config(command=eula.yview)



root = Tk()
root.title("Avi & Yuval Defence Systems")
root.configure(background = "white")

firstLabel = Label(root,text = "Enter github repository name:",bg="white")
firstLabel.grid(row=0,column = 0)

repository = Entry(root,width = 40)
repository.grid(row=0,column = 1)
try:
    submitButton = Button(root,text="Submit",padx = 40,command = submitButtonClick)
    submitButton.grid(row=0,column=2)
except:
    fail_label = Label(root,text = "Something went wrong please exit")
    fail_label.grid()
root.mainloop()



# repository = input("Enter github repository\n")
# repository_name = repository.split('/')[1]
# os.system('git clone https://github.com/' + repository)
# os.chdir(repository_name)
# os.system("git log --pretty=format:'%h,%an,%ar,%s' > commit_log.txt" )
# os.chdir("..")
# shutil.move(repository_name + "/" + "commit_log.txt" ,os.getcwd() + "/" + "commit_log.txt")
# os.startfile("commit_log.txt")
# print("A log file found and opened")
# answers = ["yes","no"]
# answer = input("Do you confirm the commits printed?(yes/no)\n")
# while answer not in answers:
#     answer = input("Not a valid answer, try again\n")
# if answer == "no":
#     exit("ERROR, User found out an unrecognised commit exiting build")
# shutil.make_archive("Build", 'zip', repository_name)
# def del_rw(action, name, exc):
#     os.chmod(name, stat.S_IWRITE)
#     os.remove(name)
# shutil.rmtree(repository_name, onerror=del_rw)
# os.remove('commit_log.txt')
# hash_result = hashlib.md5(input("Enter special password\n").encode())
# with open('hash.txt', 'w') as f:
#     f.write(str(hash_result))
# zipObj = ZipFile('Build_with_Hash.zip', 'w')
# zipObj.write('Build.zip')
# zipObj.write('hash.txt')
# zipObj.close()
# os.remove("Build.zip")
# os.remove('hash.txt')
