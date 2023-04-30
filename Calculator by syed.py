from tkinter import *
root=Tk()
root.config(background="green")

def click(event):
    global screenvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if screenvalue.get().isdigit():
            value = int(screenvalue.get())
        else:
            value = eval(screenshow.get())

        screenvalue.set(value)
        screenshow.update()


    elif text == "C":
        screenvalue.set("")
        screenshow.update()

    else:
        screenvalue.set(screenvalue.get() + text)
        screenshow.update()


root.title("Calculator by SYED")
root.geometry("560x780")
root.wm_iconbitmap("calculator.ico")

screenvalue = StringVar()
screenvalue.set("")

screenshow = Entry(root,textvar=screenvalue,font="lucida 40 bold")
screenshow .pack(fill=X,ipadx=10,padx=8,pady=10)

#--------------------------------------frame for first row of button----------------------------------------------------

frame = Frame(root,bg="grey",)
onebutton = Button(frame,text="1",font="lucida 30 bold",padx=20,pady=20,bg="orange")
onebutton.pack(side=LEFT,padx=20,pady=5)
onebutton.bind("<Button-1>", click)

twobutton = Button(frame,text="2",font="lucida 30 bold",padx=20,pady=18,bg="orange")
twobutton.pack(side=LEFT,padx=20,pady=5)
twobutton.bind("<Button-1>", click)

threebutton = Button(frame,text="3",font="lucida 30 bold",padx=20,pady=18,bg="orange")
threebutton.pack(side=LEFT,padx=20,pady=5)
threebutton.bind("<Button-1>", click)

#------------------------------------------frame for second row of button-----------------------------------------------

frame1 = Frame(root,bg="grey")
fourbutton = Button(frame1,text="4",font="lucida 30 bold",padx=20,pady=18,bg="orange")
fourbutton.pack(side=LEFT,padx=20,pady=5)
fourbutton.bind("<Button-1>", click)

fivebutton = Button(frame1,text="5",font="lucida 30 bold",padx=20,pady=18,bg="orange")
fivebutton.pack(side=LEFT,padx=20,pady=5)
fivebutton.bind("<Button-1>", click)

sixbutton = Button(frame1,text="6",font="lucida 30 bold",padx=20,pady=18,bg="orange")
sixbutton.pack(side=LEFT,padx=20,pady=5)
sixbutton.bind("<Button-1>", click)


#-------------------------------------frame for third row of button-----------------------------------------------------


frame2 = Frame(root,bg="grey")

sevenbutton = Button(frame2,text="7",font="lucida 30 bold",padx=20,pady=18,bg="orange")
sevenbutton.pack(side=LEFT,padx=20,pady=5)
sevenbutton.bind("<Button-1>", click)

eightbutton = Button(frame2,text="8",font="lucida 30 bold",padx=20,pady=18,bg="orange")
eightbutton.pack(side=LEFT,padx=20,pady=5)
eightbutton.bind("<Button-1>", click)

ninebutton = Button(frame2,text="9",font="lucida 30 bold",padx=20,pady=18,bg="orange")
ninebutton.pack(side=LEFT,padx=20,pady=5)
ninebutton.bind("<Button-1>", click)

#-----------------------------------------frame for fourth row of button------------------------------------------------


frame3 = Frame(root,bg="grey")

zerobutton = Button(frame3,text="0",font="lucida 30 bold",padx=20,pady=18,bg="orange")
zerobutton.pack(side=LEFT,padx=19,pady=5)
zerobutton.bind("<Button-1>", click)


cancelbutton = Button(frame3,text="C",font="lucida 30 bold",padx=20,pady=18,bg="red",fg="white")
cancelbutton.pack(side=LEFT,padx=18,pady=5)
cancelbutton.bind("<Button-1>", click)

Equalsbutton = Button(frame3,text="=",font="lucida 30 bold",padx=20,pady=18,)
Equalsbutton.pack(side=LEFT,padx=19,pady=5)
Equalsbutton.bind("<Button-1>", click)

#----------------------------------------frame for fifth row of button--------------------------------------------------


frame4 = Frame(root,bg="grey")

addbutton = Button(frame4,text="+",font="lucida 30 bold",padx=11,pady=18,bg="black",fg="white")
addbutton.pack(side=LEFT,padx=17,pady=5)
addbutton.bind("<Button-1>", click)


subbutton = Button(frame4,text="-",font="lucida 30 bold",padx=10,pady=18,bg="black",fg="white")
subbutton.pack(side=LEFT,padx=14,pady=5)
subbutton.bind("<Button-1>", click)

mulbutton = Button(frame4,text="*",font="lucida 30 bold",padx=10,pady=18,bg="black",fg="white")
mulbutton.pack(side=LEFT,padx=14,pady=5)
mulbutton.bind("<Button-1>", click)

divbutton = Button(frame4,text="/",font="lucida 30 bold",padx=11,pady=18,bg="black",fg="white")
divbutton.pack(side=LEFT,padx=17,pady=5)
divbutton.bind("<Button-1>", click)


#---------------------------------------------packed all the frames-----------------------------------------------------


frame.pack()
frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()




root.mainloop()