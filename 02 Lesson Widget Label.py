import tkinter as tk

win = tk.Tk()
win.title("sex-sex-sex")
photo = tk.PhotoImage(file='ico.png')
win.geometry('300x400+100+200')  # size XXXxXXX and pos +X+X of the window

label1 = tk.Label(win,
                  text='''Hello
                  world world!
                  test!''',
                  bg='red',
                  fg='yellow',
                  font=('Arial', 10, 'bold'),
                  padx=2,  # отступ
                  pady=5,
                  width=20,  # ширина в знаках
                  height=10,
                  anchor='se',
                  relief=tk.RAISED, # включаем границы лэйбла
                  bd=10, # ширина границы лэйбла
                  justify=tk.RIGHT # выравнивание по...


                  )
label1.pack()

win.mainloop()
