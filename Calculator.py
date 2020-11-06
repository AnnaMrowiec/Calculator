from tkinter import *

# Creation of a function that makes described below buttons clickable
def buttonClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

# Creation of a function that clears calculator's screen
def buttonClearDisplay():
    global operator
    operator = ''
    text_input.set('')

# Creation of a function that gives an outcome of all operations
def buttonEqualsInput():
    global operator
    calculationOutcome = str(eval(operator))
    text_input.set(calculationOutcome)

# Main settings
cal = Tk()
cal.title("Calculator")
operator = ''
text_input = StringVar()

# Creation of the calculator's output screen
text_display = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                            bg='light steel blue3', justify='right').grid(columnspan=4)

# Creation of calculator's number buttons
btn0 = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='0', command=lambda: buttonClick(0), bg='light steel blue3').grid(row=4, column=0)
btn1 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='1', command=lambda: buttonClick(1), bg='light steel blue3').grid(row=3, column=0)
btn2 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='2', command=lambda: buttonClick(2), bg='light steel blue3').grid(row=3, column=1)
btn3 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='3', command=lambda: buttonClick(3), bg='light steel blue3').grid(row=3, column=2)
btn4 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='4', command=lambda: buttonClick(4), bg='light steel blue3').grid(row=2, column=0)
btn5 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='5', command=lambda: buttonClick(5), bg='light steel blue3').grid(row=2, column=1)
btn6 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='6', command=lambda: buttonClick(6), bg='light steel blue3').grid(row=2, column=2)
btn7 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='7', command=lambda: buttonClick(7), bg='light steel blue3').grid(row=1, column=0)
btn8 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='8', command=lambda: buttonClick(8), bg='light steel blue3').grid(row=1, column=1)
btn9 = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='9', command=lambda: buttonClick(9), bg='light steel blue3').grid(row=1, column=2)

#Creation of calculator's function buttons
add     = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='+', command=lambda: buttonClick('+'), bg='light steel blue3').grid(row=1, column=3)
minus   = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='-', command=lambda: buttonClick('-'), bg='light steel blue3').grid(row=2, column=3)
times   = Button(cal, padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='*', command=lambda: buttonClick('*'), bg='light steel blue3').grid(row=3, column=3)
divide  = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='/', command=lambda: buttonClick('/'), bg='light steel blue3').grid(row=4, column=3)
clear   = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='C', command=lambda: buttonClearDisplay(), bg='light steel blue3').grid(row=4, column=1)
equals  = Button(cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'), text='=', command=lambda: buttonEqualsInput(), bg='light steel blue3').grid(row=4, column=2)

# Starts program
cal.mainloop()