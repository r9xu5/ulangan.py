import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttkb

# Membuat instance TTKbootstrap Style
style = ttkb.Style("flatly")

# Membuat jendela utama
root = ttkb.Window(themename="flatly")
root.title("Aplikasi GUI Sederhana")
root.geometry("400x300")

# Fungsi yang dipanggil saat tombol ditekan
def tombol_ditekan():
    label.config(text="Tombol telah ditekan!")

# Menambahkan label ke jendela
label = ttkb.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=20)

# Menambahkan tombol ke jendela
tombol = ttkb.Button(root, text="Tekan Saya", bootstyle="success", command=tombol_ditekan)
tombol.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()