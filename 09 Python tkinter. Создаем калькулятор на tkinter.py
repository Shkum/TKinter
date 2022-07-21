# Python tkinter. Создаем калькулятор на tkinter
import tkinter as tk
from tkinter import messagebox


def add_digit(digit):
    value = calc.get()
    if value == '0':
        calc.delete(0, 'end')
    calc.insert(tk.END, digit)


def clear():
    calc.delete(0, 'end')
    calc.insert(0, '0')


def add_ops(operation):
    value = calc.get()
    if len(value) > 0:
        if value[-1] in '-+/*':
            value = value[:-1]
        elif '+' in value or '-' in value or '*' in value or '/' in value:
            calculate()
            value = calc.get()

    calc.delete(0, 'end')
    calc.insert(tk.END, value + operation)


def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc.delete(0, 'end')
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Error', 'Only digits accepted...')
        calc.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'Zero division error...')
        calc.insert(0, '0')


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_ops_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_ops(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear)


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit() and str(event.widget).split(".")[-1] != '!entry':
        add_digit(event.char)
    elif event.char in '+-*/':
        add_ops(event.char)
    elif event.char == '\r':
        calculate()


def press_key_calc(event):
    print(repr(event.char))
    if event.char not in '1234567890/*-+\r':
        return 'break'
    elif event.char in '1234567890':
        add_digit(event.char)
        return 'break'
    elif event.char in '/*-+':
        add_ops(event.char)
        return 'break'

win = tk.Tk()
win.title("Calculator")
win.geometry('240x270+100+200')  # size XXXxXXX and pos +X+X of the window
# win.configure(bg='#33ffe6')
win['bg'] = '#33ffe6'

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)

calc.bind('<Key>', press_key_calc)

calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=5, pady=3)

make_digit_button('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, sticky='ewns', padx=5, pady=5)

make_ops_button('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_ops_button('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_ops_button('/').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_ops_button('*').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)

make_clear_button('C').grid(row=4, column=1, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
