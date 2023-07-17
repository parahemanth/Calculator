from tkinter import *

wind=Tk()
wind.geometry("225x180")
wind.title("Calculator")

frame=Frame(master=wind,bg="orange",padx=15)
frame.pack()

def getNumber(n):
    entry.insert(END,n)

def getOperator(n):
    s=entry.get()
    if(len(s)>=1):
        if(s[-1]=="+" or s[-1]=="-" or s[-1]=="/" or s[-1]=="*"):
            s=s[:len(s)-1]+n
            clear()
            entry.insert(0,s)
        else:
            entry.insert(END,n)
    else:
        entry.insert(END,n)

def Evaluate():
    s=entry.get()
    if(len(s)==0):
        return
    try:
        val=eval(s)
        clear()
        entry.insert(0,str(val))
    except ZeroDivisionError:
        clear()
        entry.insert(0,"Math Error")
    except:
        clear()
        entry.insert(0,"Syntax Error")

def clear():
    entry.delete(0,END)

entry=Entry(master=frame,background="green",cursor="arrow",bd=4)
entry.grid(row=0,column=0,columnspan=4,ipady=4)

button7=Button(master=frame,text="7",relief="raised",command=lambda:getNumber(7))
button7.grid(row=1,column=0,ipadx=6,ipady=2)

button8=Button(master=frame,text="8",relief="raised",command=lambda:getNumber(8))
button8.grid(row=1,column=1,ipadx=6.5,ipady=2)

button9=Button(master=frame,text="9",relief="raised",command=lambda:getNumber(9))
button9.grid(row=1,column=2,ipadx=6,ipady=2)

button_plus=Button(master=frame,text="+",relief="raised",command=lambda:getOperator("+"))
button_plus.grid(row=1,column=3,ipadx=5,ipady=2)

button4=Button(master=frame,text="4",relief="raised",command=lambda:getNumber(4))
button4.grid(row=2,column=0,ipadx=6,ipady=2)

button5=Button(master=frame,text="5",relief="raised",command=lambda:getNumber(5))
button5.grid(row=2,column=1,ipadx=6.5,ipady=2)

button6=Button(master=frame,text="6",relief="raised",command=lambda:getNumber(6))
button6.grid(row=2,column=2,ipadx=6,ipady=2)

button_sub=Button(master=frame,text="-",relief="raised",command=lambda:getOperator("-"))
button_sub.grid(row=2,column=3,ipadx=6,ipady=2)

button1=Button(master=frame,text="1",relief="raised",command=lambda:getNumber(1))
button1.grid(row=3,column=0,ipadx=6,ipady=2)

button2=Button(master=frame,text="2",relief="raised",command=lambda:getNumber(2))
button2.grid(row=3,column=1,ipadx=6.5,ipady=2)

button3=Button(master=frame,text="3",relief="raised",command=lambda:getNumber(3))
button3.grid(row=3,column=2,ipadx=6,ipady=2)

button_mul=Button(master=frame,text="*",relief="raised",command=lambda:getOperator("*"))
button_mul.grid(row=3,column=3,ipadx=6,ipady=2)

button_C=Button(master=frame,text="C",relief="raised",command=lambda:clear())
button_C.grid(row=4,column=0,ipadx=5.35,ipady=2)

button0=Button(master=frame,text="0",relief="raised",command=lambda:getNumber(0))
button0.grid(row=4,column=1,ipadx=6.5,ipady=2)

button_eval=Button(master=frame,text="=",relief="raised",command=lambda:Evaluate())
button_eval.grid(row=4,column=2,ipadx=4.5,ipady=2)

button_div=Button(master=frame,text="/",relief="raised",command=lambda:getOperator("/"))
button_div.grid(row=4,column=3,ipadx=6,ipady=2)

wind.mainloop()