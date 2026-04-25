#Josiah Hendley
#4/24/2026
#MPG Calculator



import tkinter as tk

def calculate_mpg():
    gallons = float(gallons_entry.get())
    miles = float(miles_entry.get())
    mpg = miles / gallons
    result_label.config(text=f"MPG: {mpg:.2f}")

window = tk.Tk()
window.title("MPG Calculator")

tk.Label(window, text="Gallons:").pack()
gallons_entry = tk.Entry(window)
gallons_entry.pack()

tk.Label(window, text="Miles:").pack()
miles_entry = tk.Entry(window)
miles_entry.pack()

tk.Button(window, text="Calculate MPG", command=calculate_mpg).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
