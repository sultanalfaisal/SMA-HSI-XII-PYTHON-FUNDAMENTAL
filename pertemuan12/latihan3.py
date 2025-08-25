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