# Latihan 2: Salin File

# Membaca isi dari file sumber.txt
with open("sumber.txt", "r", encoding="utf-8") as sumber:
    isi = sumber.read()

# Menulis isi ke file salinan.txt
with open("salinan.txt", "w", encoding="utf-8") as salinan:
    salinan.write(isi)

print("Isi file berhasil disalin ke salinan.txt")