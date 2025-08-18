# Latihan 1: Membuat Log Sederhana

# Membuka file dalam mode append ('a') → data baru akan ditambahkan di akhir
with open("log_kegiatan.txt", "a", encoding="utf-8") as file:
    kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
    file.write(kegiatan + "\n")  # Menulis kegiatan di baris baru

print("Kegiatan berhasil dicatat di log_kegiatan.txt")

# Latihan 2: Salin File

# Membaca isi dari file sumber.txt
with open("sumber.txt", "r", encoding="utf-8") as sumber:
    isi = sumber.read()

# Menulis isi ke file salinan.txt
with open("salinan.txt", "w", encoding="utf-8") as salinan:
    salinan.write(isi)

print("Isi file berhasil disalin ke salinan.txt")

# Latihan 3: Hapus File dengan Aman
import os

nama_file = input("Masukkan nama file yang ingin dihapus: ")

if os.path.exists(nama_file):
    konfirmasi = input(f"Anda yakin ingin menghapus '{nama_file}'? (y/n): ").lower()
    if konfirmasi == "y":
        os.remove(nama_file)
        print(f"File '{nama_file}' berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
else:
    print(f"File '{nama_file}' tidak ditemukan.")
