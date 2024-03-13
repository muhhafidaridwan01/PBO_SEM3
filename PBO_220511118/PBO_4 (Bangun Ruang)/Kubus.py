import tkinter as tk

def hitung_luas_dan_volume():
    sisi = float(sisi_entry.get())
    luas = 6 * sisi ** 2
    volume = sisi ** 3
    luas_label.config(text=f"Luas: {luas:.2f} satuan^2")
    volume_label.config(text=f"Volume: {volume:.2f} satuan^3")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Kubus")

# Windows
frame = tk.Frame(root)
frame.pack()

# Label Nama
nama_label = tk.Label(root, text="Muhammad Hafid Aridwan | 220511118")
nama_label.pack()

# Label dan input untuk panjang sisi
sisi_label = tk.Label(root, text="Panjang Sisi Kubus:")
sisi_label.pack()
sisi_entry = tk.Entry(root)
sisi_entry.pack()

# Tombol untuk menghitung
hitung_button = tk.Button(root, text="Hitung", command=hitung_luas_dan_volume)
hitung_button.pack()

# Label untuk menampilkan hasil perhitungan
luas_label = tk.Label(root, text="")
luas_label.pack()
volume_label = tk.Label(root, text="")
volume_label.pack()

root.mainloop()
