# Python tkinter. Создаем калькулятор на tkinter
import tkinter as tk


def add_digit(digit):
    value = calc.get()
    if value == '0':
        calc.delete(0, 'end')
    calc.insert(tk.END, digit)


def add_ops(operation):
    value = calc.get()
    if len(value) > 0:
        if value[-1] in '-+/*':
            value = value[:-1]
    calc.delete(0, 'end')
    calc.insert(tk.END, value + operation)


def calculate(expr):
    res = eval(calc.get())
    calc.delete(0, 'end')
    return calc.insert(0, res)


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_ops_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_ops(operation))


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: calculate(calc.get()))


win = tk.Tk()
win.title("Calculator")
win.geometry('240x270+100+200')  # size XXXxXXX and pos +X+X of the window
# win.configure(bg='#33ffe6')
win['bg'] = '#33ffe6'

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)

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

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
