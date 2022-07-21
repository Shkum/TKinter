import tkinter as tk

count = 0

def button_click():
    print('Hello')


def add_label():
    global label
    label = tk.Label(win, text="new", )
    label.pack()


def change_label_text():
    global label
    label.config(text='Новый текст')


def counter():
    global count
    count += 1
    button4['text'] = f'Counter: {count}'


win = tk.Tk()
win.title("sex-sex-sex")
win.geometry('300x400+100+200')  # size XXXxXXX and pos +X+X of the window

button1 = tk.Button(win,
                    text='Hallo',
                    command=button_click)

button2 = tk.Button(win,
                    command=add_label,
                    text='Add label')

button3 = tk.Button(win,
                    text='Add new label LAMBDA',
                    command=lambda: tk.Label(win, text='new lambda').pack()
                    )


button4 = tk.Button(win,
                    text=f'Counter: {count}',
                    command=counter,
                    bg='green',
                    activebackground='blue',
                    state=tk.NORMAL  # DISABLED
                    )

button5 = tk.Button(win,
                    command=change_label_text,
                    text='Change label text')

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

win.mainloop()
