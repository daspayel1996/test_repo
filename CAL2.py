from tkinter import *

def btnclick(number):
    global value
    value=value+str(number)
    data.set(value)

def btnclear():
    global value
    value=""
    data.set("")

def btnEquals():
    global value 
    result=str(eval(value))
    data.set(result)

root= Tk()
root.title("my cal")
root.geometry("361x381+500+200")
value=""
data= StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)

Btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(7))
Btn7.grid(row=1,column=0)

Btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(8))
Btn8.grid(row=1,column=1)

Btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(9))
Btn9.grid(row=1,column=2)

plus=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('+'))
plus.grid(row=1,column=3)

Btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(4))
Btn4.grid(row=2,column=0)

Btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(5))
Btn5.grid(row=2,column=1)

Btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(6))
Btn6.grid(row=2,column=2)

minus=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('-'))
minus.grid(row=2,column=3)

Btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(1))
Btn1.grid(row=3,column=0)

Btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(2))
Btn2.grid(row=3,column=1)

Btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(3))
Btn3.grid(row=3,column=2)

multipl=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('*'))
multipl.grid(row=3,column=3)

clear=Button(root,text="c",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
clear.grid(row=4,column=0)

Btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick(0))
Btn0.grid(row=4,column=1)

equal=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
equal.grid(row=4,column=2)

divide=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda: btnclick('/'))
divide.grid(row=4,column=3)

root.mainloop()