from tkinter import *
calc=Tk()
calc.title("calculator")
operator=""
text_input=StringVar()

def btnClick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator=""
    text_input.set(operator)

def btnEqualsInput():
    global operator
    ans= str(eval(operator))
    text_input.set(ans)

txtDisplay= Entry(calc,font=("arail",15,"bold"),textvariable=text_input, bd= 30,bg="grey",justify="right")
txtDisplay.grid(columnspan=4)
btn0=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="0",command=lambda:btnClick(0)).grid(row=4,column=1)
btn1=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="1",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="2",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="3",command=lambda:btnClick(3)).grid(row=3,column=2)
btn4=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="4",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="5",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="6",command=lambda:btnClick(6)).grid(row=2,column=2)
btn7=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="7",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="8",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="9",command=lambda:btnClick(9)).grid(row=1,column=2)

Equal=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="=",command=btnEqualsInput).grid(row=4,column=2)
addition=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="+",command=lambda:btnClick("+")).grid(row=1,column=3)
subtraction=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="-",command=lambda:btnClick("-")).grid(row=2,column=3)
multiplication=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="x",command=lambda:btnClick("*")).grid(row=3,column=3)
division=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="/",command=lambda:btnClick("/")).grid(row=4,column=3)
Clear=Button(calc,padx=16,bd=8,fg="black",font=("arail",15,"bold"),text="C",command=btnClearDisplay).grid(row=4,column=0)

calc.mainloop()
