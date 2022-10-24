from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(background="#ffffff")
label1 = Label(root)
label2 = Label(root)
label1.configure(font=100)
label1.place(relx = 0.1, rely=0.1)
label4 = Label(root)
label4.configure(font=100)
label4.place(relx = 0.7, rely=0.1)
label2.configure(font=100)
label2.place(relx = 0.3, rely=0.1)
label3 = Label(root)
label3.configure(font=100)
label3.place(relx = 0.5, rely=0.1)
def add():
    label2["text"]="+"
def multiply():
    label2["text"]="X"
def subtract():
    label2["text"]="-"
def divide():
    label2["text"]="÷"
def clear():
    label1["text"]= ""
    label2["text"]= ""
    label3["text"]=""
    label4["text"]=""
def one():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="1"
    else:
        label3["text"]+="1"
def two():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="2"
    else:
        label3["text"]+="2"
def three():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="3"
    else:
        label3["text"]+="3"
def four():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="4"
    else:
        label3["text"]+="4"
def five():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="5"
    else:
        label3["text"]+="5"
def six():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="6"
    else:
        label3["text"]+="6"
def seven():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="7"
    else:
        label3["text"]+="7"
def eight():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="8"
    else:
        label3["text"]+="8"
def nine():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="9"
    else:
        label3["text"]+="9"
def zero():
    op= label2["text"]
    if op != "+" and op != "-" and op != "X" and op != "÷":
        label1["text"]+="0"
    else:
        label3["text"]+="0"
def equal():
    if label2["text"] == "+":
        num1 = label1["text"]
        float_num1 = float(num1)
        num2 = label3["text"]
        float_num2 = float(num2)
        label4["text"]= " = " + str(float_num1 + float_num2)
    if label2["text"] == "-":
        num1 = label1["text"]
        float_num1 = float(num1)
        num2 = label3["text"]
        float_num2 = float(num2)
        label4["text"]= " = " + str(float_num1 - float_num2)
    if label2["text"] == "X":
        num1 = label1["text"]
        float_num1 = float(num1)
        num2 = label3["text"]
        float_num2 = float(num2)
        label4["text"]= " = " + str(float_num1 * float_num2)
    if label2["text"] == "÷":
        num1 = label1["text"]
        float_num1 = float(num1)
        num2 = label3["text"]
        float_num2 = float(num2)
        label4["text"]= " = " + str(float_num1 / float_num2)
button1 = Button(root, text="1", command=one)
button2 = Button(root, text="2", command=two)
button3 = Button(root, text="3", command=three)
button4 = Button(root, text="4", command=four)
button5 = Button(root, text="5", command=five)
button6 = Button(root, text="6", command=six)
button7 = Button(root, text="7", command=seven)
button8 = Button(root, text="8", command=eight)
button9 = Button(root, text="9", command=nine)
button0 = Button(root, text="0", command=zero)
buttonadd = Button(root, text="+", command=add)
buttonsub = Button(root, text="-", command= subtract)
buttonmulti = Button(root, text="X", command=multiply)
buttondiv = Button(root, text="÷", command=divide)
buttonC = Button(root, text="C", command=clear)
buttone = Button(root, text="=", command=equal)
button1.place(relx=0.28, rely=0.4, anchor=E)
button1.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button2.place(relx=0.57, rely=0.4, anchor=E)
button2.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button3.place(relx=0.86, rely=0.4, anchor=E)
button3.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button4.place(relx=0.28, rely=0.57, anchor=E)
button4.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button5.place(relx=0.57, rely=0.57, anchor=E)
button5.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button6.place(relx=0.86, rely=0.57, anchor=E)
button6.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button7.place(relx=0.28, rely=0.73, anchor=E)
button7.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button8.place(relx=0.57, rely=0.73, anchor=E)
button8.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button9.place(relx=0.86, rely=0.73, anchor=E)
button9.config(height=4, width=15, background="#ffffff", highlightcolor="black")
button0.place(relx=0.57, rely=0.905, anchor=E)
button0.config(height=4, width=15, background="#ffffff", highlightcolor="black")
buttonadd.place(relx=0.57, rely=0.905, anchor=W)
buttonadd.config(height=4, width=15, background="#ffffff", highlightcolor="black")
buttonsub.place(relx=0.28, rely=0.905, anchor=E)
buttonsub.config(height=4, width=15, background="#ffffff", highlightcolor="black")
buttonmulti.place(relx=0.86, rely=0.405, anchor=W)
buttonmulti.config(height=4, width=7, background="#ffffff", highlightcolor="black")
buttondiv.place(relx=0.86, rely=0.58, anchor=W)
buttondiv.config(height=4, width=7, background="#ffffff", highlightcolor="black")
buttonC.place(relx=0.86, rely=0.74, anchor=W)
buttonC.config(height=4, width=7, background="#ffffff", highlightcolor="black")
buttone.place(relx=0.86, rely=0.912, anchor=W)
buttone.config(height=4, width=7, background="skyblue", highlightcolor="black")
root.mainloop()