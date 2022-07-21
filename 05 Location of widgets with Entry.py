# Widgets loacation with ENTRY()

import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('No enrty...')


def delete_entry():
    # name.delete(1, 'end')
    # name.delete(1, 3)
    name.delete(1, tk.END)


def insert_entry():
    name.insert('end', 'sex')


win = tk.Tk()
win.title("sex-sex-sex")
win.geometry('400x500+100+200')  # size XXXxXXX and pos +X+X of the window
# win.configure(bg='yellow')
win['bg'] = 'yellow'

tk.Label(win, text='Name').grid(row=0, column=0, sticky='w')

tk.Label(win, text='Pass').grid(row=1, column=0, sticky='w')

name = tk.Entry(win)
name.grid(row=0, column=1)
name.insert(0, 'sex')

pas = tk.Entry(win, show='#')
pas.grid(row=1, column=1)

tk.Button(win, text='get', command=get_entry).grid(row=2, column=0, sticky='we')

tk.Button(win, text='delete', command=delete_entry).grid(row=2, column=1, sticky='we')

tk.Button(win, text='get pass', command=lambda: print(pas.get() if pas.get() else 'No pass entered...')).grid(row=2, column=3, sticky='we')

# tk.Button(win, text='insert', command=insert_entry).grid(row=1, column=2, sticky='we')
tk.Button(win, text='insert', command=lambda: name.insert(0, 'hello_')). \
    grid(row=2, column=2, sticky='we')



win.grid_columnconfigure(0, minsize=100)  # минимальная ширина колонок
win.grid_columnconfigure(1, minsize=100)  # минимальная ширина колонок

win.mainloop()
