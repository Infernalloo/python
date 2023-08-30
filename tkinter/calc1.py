import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Calculator")
window.geometry("350x600")

# title

# input
input_frame = ttk.Frame(master = window)
button_one = ttk.Button(master = input_frame, text="1")
button_one.pack(side="left", pady="65")
button_two = ttk.Button(master = input_frame, text="2")
button_two.pack(side="left")
button_three = ttk.Button(master = input_frame, text="3")
button_three.pack(side="left")

button_four = ttk.Button(master = input_frame, text="4")
button_four.pack(side="bottom", pady="25")
button_five = ttk.Button(master = input_frame, text="5")
button_five.pack(side="bottom")
button_six = ttk.Button(master = input_frame, text="6")
button_six.pack(side="bottom")

button_seven = ttk.Button(master = input_frame, text="7")
button_seven.pack(side="left", pady="25")
button_eight = ttk.Button(master = input_frame, text="8")
button_eight.pack(side="left")
button_nine = ttk.Button(master = input_frame, text="9")
button_nine.pack(side="left")

input_frame.pack()


# run
window.mainloop()
