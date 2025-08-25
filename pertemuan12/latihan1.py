# Latihan 1: Membuat Log Sederhana

# Membuka file dalam mode append ('a') → data baru akan ditambahkan di akhir
with open("log_kegiatan.txt", "a", encoding="utf-8") as file:
    kegiatan = input("Masukkan kegiatan yang baru saja dilakukan: ")
    file.write(kegiatan + "\n")  # Menulis kegiatan di baris baru

print("Kegiatan berhasil dicatat di log_kegiatan.txt")
