# Widgets loacation with GRID()

import tkinter as tk

win = tk.Tk()
win.title("sex-sex-sex")
win.geometry('300x400+100+200')  # size XXXxXXX and pos +X+X of the window
# win.configure(bg='yellow')
win['bg'] = 'yellow'

button1 = tk.Button(win, text='Hello1')
button2 = tk.Button(win, text='Hello2')
button3 = tk.Button(win, text='Hello3')
button4 = tk.Button(win, text='Hello world 4')
button5 = tk.Button(win, text='Hello5')
button6 = tk.Button(win, text='Hello6')
button7 = tk.Button(win, text='Hello7')
button8 = tk.Button(win, text='Hello8')

# button1.pack()
# button2.pack()

# button1.grid()
# button2.grid()


button1.grid(row=0, column=0)
button2.grid(row=0, column=1, sticky='e')
button3.grid(row=1, column=0, sticky='we')
button4.grid(row=1, column=1)
button5.grid(row=2, column=0)
button6.grid(row=2, column=1, sticky='we')
button7.grid(row=3, column=0, columnspan=2, stick='we')
button8.grid(row=0, column=2, rowspan=3, stick='sn')

for i in range(5):
    for j in range(2):
        tk.Button(win,text=f'Hello {i} {j}').grid(row=i+6, column=j, sticky='ew')


win.grid_columnconfigure(0, minsize=70)  # минимальная ширина колонок
win.grid_columnconfigure(1, minsize=120)  # минимальная ширина колонок

win.mainloop()
