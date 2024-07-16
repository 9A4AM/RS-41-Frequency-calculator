#-------------------------------------------------------------------------------
# Name:        RS41_freq_reg_calc
# Purpose:
#
# Author:      mario.ancic
#
# Created:     16.07.2024
# Copyright:   (c) mario.ancic 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math
import tkinter as tk
from tkinter import messagebox

def calculate_registers():
    try:
        f = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")
        return

    fref = 26.0 / 3.0

    if f >= 416.0:
        hbsel = 1
    else:
        hbsel = 0

    fb = math.floor(f / (hbsel + 1) * 30.0 / 260 - 24)
    fc = round(64000.0 * f / (fref * (hbsel + 1)) - 64000.0 * fb - 64000.0 * 24)

    reg75 = f"{fb + hbsel * 32:02X}"
    reg76 = f"{fc // 256:02X}"
    reg77 = f"{fc % 256:02X}"

    result_text.set(f"frequency: {f}\n"
                    f"hbsel: {hbsel}\n"
                    f"fb: {fb}\n"
                    f"fc: {fc}\n"
                    f"reg75: {reg75}\n"
                    f"reg76: {reg76}\n"
                    f"reg77: {reg77}")

# Kreiranje glavnog prozora
root = tk.Tk()
root.title("Frequency Calculator by 9A4AM")

# Kreiranje unosa za frekvenciju
tk.Label(root, text="Enter frequency:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Kreiranje gumba za pokretanje izračuna
tk.Button(root, text="Calculate", command=calculate_registers).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Kreiranje tekstualnog okvira za prikaz rezultata
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify='left')
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Pokretanje glavne petlje
root.mainloop()

