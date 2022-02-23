from tkinter import*
import random
root=Tk()
root.geometry("500x500")
root.title("Dictionary")
dict={'color':["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan"]}
def mutable():
    randomnumber=random.randint(0,7)
    root.configure(background=dict['color'][randomnumber])


button1=Button(root,text="Click Me NOW!!!!",command=mutable)
button1.place(relx=0.5, rely=0.5,anchor=CENTER)

root.mainloop()