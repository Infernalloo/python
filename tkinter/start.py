import tkinter as tk
from tkinter import ttk

def convert():
    print(entryInt.get())

# window
window = tk.Tk()
window.title("Demo")
window.geometry("350x175")

# title
title_label = ttk.Label(master = window, text = "Miles to kilometer", font = "Monospace 24")
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady= 10)

# output
output_label = ttk.Label(master = window, text = "Output", font = "Monospace 24")
output_label.pack(pady = 5)

# run
window.mainloop()