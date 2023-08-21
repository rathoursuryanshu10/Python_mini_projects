from tkinter import *
import speedtest

def speed_check():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+" Mbps"
    up=str(round(sp.upload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp=Tk()
sp.title("Internet speed test :  ")
sp.geometry("500x600")
sp.config(bg="aqua")
lab=Label(sp,text="Internet Speed Test :: ",font=("Time New Roman",27,"bold"),bg="aqua",fg="White")
lab.place(x=60,y=40,height=50,width=380)

lab=Label(sp,text="Downloading Speed :: ",font=("Time New Roman",27,"bold"),bg="aqua",fg="White")
lab.place(x=60,y=130,height=50,width=380)

lab_down=Label(sp,text=" 00 ",font=("Time New Roman",27,"bold"),bg="aqua",fg="White")
lab_down.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Uploading Speed :: ",font=("Time New Roman",27,"bold"),bg="aqua",fg="White")
lab.place(x=60,y=290,height=50,width=380)

lab_up=Label(sp,text=" 00 ",font=("Time New Roman",27,"bold"),bg="aqua",fg="White")
lab_up.place(x=60,y=360,height=50,width=380)
button=Button(sp,text="Run Speed Test ",font=("Time New Roman",27,"bold"),relief=RAISED,bg="Blue",fg="white",command=speed_check)
button.place(x=60,y=460,height=50,width=380)


sp.mainloop()
