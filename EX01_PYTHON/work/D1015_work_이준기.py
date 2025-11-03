import tkinter as tkinter

window = tkinter.Tk()
window.title("Calculator")
window.geometry("320x420")
window.resizable(False, False)

for r in range(6):
    window.grid_rowconfigure(r, weight=1, uniform="row")
for c in range(4):
    window.grid_columnconfigure(c, weight=1, uniform="col")

display = tkinter.Entry(window)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=8, pady=8)

def append_char(ch):
    display.insert(tkinter.END, ch)

def clear_all():
    display.delete(0, tkinter.END)

def calculate():
        v = eval(display.get())
        display.delete(0, tkinter.END)
        display.insert(tkinter.END, str(v))

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for text, r, c in buttons:
    if text == "C":
        btn = tkinter.Button(window, text=text, command=clear_all)
    elif text == "=":
        btn = tkinter.Button(window, text=text, command=calculate)
    else:
        btn = tkinter.Button(window, text=text, command=lambda t=text: append_char(t))
    btn.grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

window.mainloop()