from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False,False)

def Save_file():
    # print("")
    Open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if Open_file is None:
        return 
    text=str(entry.get(1.0,END))
    Open_file.write(text)
    Open_file.close()


def Open_file():
    # print("")
    file=filedialog.askopenfile(mode='r',filetype=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

b1=Button(root,width='20',height='2',bg='#fff',text='Save_file',command=Save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg='#fff',text='open_file',command=Open_file).place(x=300,y=5)


entry=Text(root,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)
root.mainloop()
