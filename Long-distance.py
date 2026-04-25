#Josiah Hendley
#4/24/2026
#Long Distance calls

import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    minutes = float(minutes_entry.get())
    rate = rate_var.get()
    cost = minutes * rate
    messagebox.showinfo("Call Cost", f"Total Charge: ${cost:.2f}")

window = tk.Tk()
window.title("Call Calculator")

rate_var = tk.DoubleVar()

tk.Radiobutton(window, text="Daytime ($0.02)", variable=rate_var, value=0.02).pack()
tk.Radiobutton(window, text="Evening ($0.12)", variable=rate_var, value=0.12).pack()
tk.Radiobutton(window, text="Off-Peak ($0.05)", variable=rate_var, value=0.05).pack()

tk.Label(window, text="Minutes:").pack()
minutes_entry = tk.Entry(window)
minutes_entry.pack()

tk.Button(window, text="Calculate", command=calculate_cost).pack()

window.mainloop()
