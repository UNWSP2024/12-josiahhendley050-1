#Josiah Hendley
#Joes Automotive
#4/24/2026

import tkinter as tk

def calculate_total():
    total = 0
    if oil_var.get(): total += 30
    if lube_var.get(): total += 20
    if radiator_var.get(): total += 40
    if trans_var.get(): total += 100
    if inspect_var.get(): total += 35
    if muffler_var.get(): total += 200
    if tire_var.get(): total += 20

    result_label.config(text=f"Total: ${total}")

window = tk.Tk()
window.title("Joe's Automotive")

oil_var = tk.IntVar()
lube_var = tk.IntVar()
radiator_var = tk.IntVar()
trans_var = tk.IntVar()
inspect_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_var = tk.IntVar()

tk.Checkbutton(window, text="Oil Change ($30)", variable=oil_var).pack()
tk.Checkbutton(window, text="Lube Job ($20)", variable=lube_var).pack()
tk.Checkbutton(window, text="Radiator Flush ($40)", variable=radiator_var).pack()
tk.Checkbutton(window, text="Transmission Fluid ($100)", variable=trans_var).pack()
tk.Checkbutton(window, text="Inspection ($35)", variable=inspect_var).pack()
tk.Checkbutton(window, text="Muffler ($200)", variable=muffler_var).pack()
tk.Checkbutton(window, text="Tire Rotation ($20)", variable=tire_var).pack()

tk.Button(window, text="Calculate Total", command=calculate_total).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
