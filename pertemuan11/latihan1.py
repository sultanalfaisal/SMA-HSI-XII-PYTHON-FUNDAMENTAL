# Latihan 1: Tampilkan Semua Uppercase

# Meminta input nama file
nama_file = input("Masukkan nama file: ")

try:
    # Membuka file
    with open(nama_file, 'r', encoding='utf-8') as file:
        # Membaca setiap baris
        for baris in file:
            print(baris.upper().strip())  # Ubah ke uppercase dan hapus spasi
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file benar.")
