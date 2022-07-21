# Python tkinter. Виджет CheckButton

import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def toggle_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


win = tk.Tk()
win.geometry(f'300x400+100+200')
win.title('My app')


over_18_value=tk.StringVar()
commercial_value=tk.IntVar()

over_18 = tk.Checkbutton(win, text='more then 18 years old?',
                         textvariable=over_18_value,
                         offvalue='No',
                         onvalue='Yes'
                         )
commercial = tk.Checkbutton(win, text='Do you like advertising?')
follow = tk.Checkbutton(win, text='Subscribe to chanel?', indicatoron=False)

over_18.pack()
commercial.pack()
follow.pack()

tk.Button(win, text='Select all', command=select_all).pack()

tk.Button(win, text='DeSelect all', command=deselect_all).pack()

tk.Button(win, text='Switch/Toggle', command=toggle_all).pack()

win.mainloop()
