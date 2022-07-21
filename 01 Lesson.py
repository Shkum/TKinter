import tkinter as tk
h=500
w=700
win = tk.Tk()
win.title("sex-sex-sex")
photo = tk.PhotoImage(file='ico.png')
win.iconphoto(False, photo)
win.geometry(f'{h}x{w}+100+100') # size XXXxXXX and pos +X+X of the window
win.resizable(True, False)
win.minsize (200, 300)
win.maxsize (600, 800)
# win.config(bg='green')
win.config(bg='#2dff00')
win.mainloop()
