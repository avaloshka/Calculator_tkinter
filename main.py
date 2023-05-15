import tkinter as tk
from tkinter import *

first_num = None
second_num = None
operator = None


def button_click(item):
    current = entry.get()
    # get rid of '0' so you can enter (read) a new number
    if current == '0':
        current = ''
    # replace the screen with old input + new input as one number
    entry.delete(0, END)
    entry.insert(0, current + str(item))
    global first_num
    # save to first_num, or second_num
    if operator is None:
        # save first_num
        first_num = entry.get()
    elif operator != None:
        global second_num
        # save second_num
        second_num = entry.get().split(operator)[1]


def button_operator(item):
    global operator
    # if previous calculations where done, operator is not empty
    if operator != None:
        # if operator == last character (non-digit) then delete from the screen, so we can re-write the operator later
        if not entry.get().isdigit():
            entry.delete(len(entry.get())-1, tk.END)
        # if button operator is pressed (collect operator when second_num is not specified yet)
        elif second_num is None:
            # collect operator
            operator = item
        # otherwise do calculations, set first_num = result, second_num = None, operator = None
        equal()
    # if this is first calculation of the program, collect the operator to variable operator and to the screen
    operator = item
    entry.insert(END, str(item))


def equal():
    global first_num
    global second_num
    global operator

    if second_num is None:
        # calculations not needed, break out of the function
        return

    elif operator == "+":
        result = float(first_num) + float(second_num)
        entry.delete(0, END)
        entry.insert(0, result)
        first_num = result
        second_num = None
        operator = None
    elif operator == "-":
        result = float(first_num) - float(second_num)
        entry.delete(0, END)
        entry.insert(0, result)
        first_num = result
        second_num = None
        operator = None

    elif operator == "/":
        result = float(first_num) / float(second_num)
        entry.delete(0, END)
        entry.insert(0, result)
        first_num = result
        second_num = None
        operator = None

    elif operator == "*":
        result = float(first_num) * float(second_num)
        entry.delete(0, END)
        entry.insert(0, result)
        first_num = result
        second_num = None
        operator = None


def on_off():
    current = entry.get()
    # if switched off please switch on
    if current == '':
        entry.insert(0, '0')
    # if switched on- switch off, delete first_num, second_num and operator from memory
    elif current != '0' or current == '0':
        entry.delete(0, END)
    global first_num
    global second_num
    global operator
    first_num = None
    second_num = None
    operator = None


def delete():
    # delete last character from display
    entry.delete(len(entry.get())-1, tk.END)


window = tk.Tk()
window.title('Calculator')
window.geometry("321x520")
window.resizable(0, 0)
window.configure(background='black')
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)

# one of the option to operate text in entry is to use textvariable, set it to equation in this case (not used)
equation = StringVar()

# Frame mode
calculator_mode = tk.Frame(master=window, height='10')
mode_label = tk.Label(master=calculator_mode, text='Standard', background='black', foreground='white', font=("Arial", 10))
mode_label.grid(row=0, column=0)

# Entry
entry = tk.Entry(master=window, borderwidth=5, background='white', font=('Arial', 20), justify='right', textvariable=equation)

# Frame buttons
buttons_frame = tk.Frame(master=window)
button_ON_OFF = tk.Button(master=buttons_frame, bg='#A9A9A9', text='ON/OFF', width=6, height=2, font=('Arial', 15), command=on_off)
button_DEL = tk.Button(master=buttons_frame, bg='#A9A9A9', text='DEL', width=6, height=2, font=('Arial', 15), command=delete)
button_c = tk.Button(master=buttons_frame, bg='#A9A9A9', text='C', width=6, height=2, font=('Arial', 15), )
button_divide = tk.Button(master=buttons_frame, bg='#A9A9A9', text='/', width=6, height=2, font=('Arial', 15), command=lambda : button_operator('/'))

button_seven = tk.Button(master=buttons_frame, bg='gray', text='7', width=6, height=2, font=('Arial', 15), command=lambda : button_click('7'))
button_eight = tk.Button(master=buttons_frame, bg='gray', text='8', width=6, height=2, font=('Arial', 15), command=lambda : button_click('8'))
button_nine = tk.Button(master=buttons_frame, bg='gray', text='9', width=6, height=2, font=('Arial', 15), command=lambda : button_click('9'))
button_multiply = tk.Button(master=buttons_frame, bg='#A9A9A9', text='*', width=6, height=2, font=('Arial', 15),command=lambda : button_operator('*'))

button_four = tk.Button(master=buttons_frame, bg='gray', text='4', width=6, height=2, font=('Arial', 15), command=lambda : button_click('4'))
button_five= tk.Button(master=buttons_frame, bg='gray', text='5', width=6, height=2, font=('Arial', 15), command=lambda : button_click('5'))
button_six = tk.Button(master=buttons_frame, bg='gray', text='6', width=6, height=2, font=('Arial', 15), command=lambda : button_click('6'))
button_minus = tk.Button(master=buttons_frame, bg='#A9A9A9', text='-', width=6, height=2, font=('Arial', 15), command=lambda : button_operator('-'))

button_one = tk.Button(master=buttons_frame, bg='gray', text='1', width=6, height=2, font=('Arial', 15), command=lambda : button_click('1'))
button_two = tk.Button(master=buttons_frame, bg='gray', text='2', width=6, height=2, font=('Arial', 15), command=lambda : button_click('2'))
button_three = tk.Button(master=buttons_frame, bg='gray', text='3', width=6, height=2, font=('Arial', 15), command=lambda : button_click('3'))
button_plus = tk.Button(master=buttons_frame, bg='#A9A9A9', text='+', width=6, height=2, font=('Arial', 15), command=lambda : button_operator('+'))

button_plus_minus = tk.Button(master=buttons_frame, bg='gray', text='+/-', width=6, height=2, font=('Arial', 15),)
button_zero = tk.Button(master=buttons_frame, bg='gray', text='0', width=6, height=2, font=('Arial', 15), command=lambda : button_click('0'))
button_dot = tk.Button(master=buttons_frame, bg='gray', text='.', width=6, height=2, font=('Arial', 15), command=lambda : button_click('.'))
button_equals = tk.Button(master=buttons_frame, bg='#A9A9A9', text='=', width=6, height=2, font=('Arial', 15), command=equal)

# Buttons layout on 'buttons_frame'
button_ON_OFF.grid(row=0, column=0, padx=2, pady=2)
button_DEL.grid(row=0, column=1, padx=2, pady=2)
button_c.grid(row=0, column=2, padx=2, pady=2)
button_divide.grid(row=0, column=3, padx=2, pady=2)

button_seven.grid(row=1, column=0, padx=2, pady=2)
button_eight.grid(row=1, column=1, padx=2, pady=2)
button_nine.grid(row=1, column=2, padx=2, pady=2)
button_multiply.grid(row=1, column=3, padx=2, pady=2)

button_four.grid(row=2, column=0, padx=2, pady=2)
button_five.grid(row=2, column=1, padx=2, pady=2)
button_six.grid(row=2, column=2, padx=2, pady=2)
button_minus.grid(row=2, column=3, padx=2, pady=2)

button_one.grid(row=3, column=0, padx=2, pady=2)
button_two.grid(row=3, column=1, padx=2, pady=2)
button_three.grid(row=3, column=2, padx=2, pady=2)
button_plus.grid(row=3, column=3, padx=2, pady=2)

button_plus_minus.grid(row=4, column=0, padx=2, pady=2)
button_zero.grid(row=4, column=1, padx=2, pady=2)
button_dot.grid(row=4, column=2, padx=2, pady=2)
button_equals.grid(row=4, column=3, padx=2, pady=2)

# Main layout
calculator_mode.grid(column=0, row=0)
entry.grid(row=1, column=0, sticky='nsew')
buttons_frame.grid(row=2, column=0, sticky='nsew')

window.mainloop()