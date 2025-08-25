s = "Belajar Python itu Menyenangkan"

# a. Karakter pertama
print("Karakter pertama:", s[0])  # B

# b. Karakter terakhir (menggunakan indexing negatif)
print("Karakter terakhir:", s[-1])  # n

# c. Karakter spasi pertama (di indeks 7)
print("Spasi pertama:", s[7])  # ' '

s = "Belajar Python itu Menyenangkan"

# a. "Python"
print("Substring 'Python':", s[8:14])

# b. "Menyenangkan"
print("Substring 'Menyenangkan':", s[19:])

# c. "Belajar"
print("Substring 'Belajar':", s[:7])

kata = input("Masukkan sebuah kata: ")

# Membalik kata dengan slicing
dibalik = kata[::-1]
print("Kata dibalik:", dibalik)

# Cek palindrom (abaikan huruf besar/kecil & spasi)
kata_bersih = kata.replace(" ", "").lower()
dibalik_bersih = dibalik.replace(" ", "").lower()

if kata_bersih == dibalik_bersih:
    print("Kata ini adalah palindrom ✅")
else:
    print("Kata ini bukan palindrom ❌")

kalimat = "BPrOaGikRtoAdMiItMuINtuGhpPyYcThHoOnN"

# Ambil setiap karakter ke-3 (mulai indeks 0, step=3)
kode_rahasia = kalimat[::3]

print("Kode rahasia:", kode_rahasia)

nama_salah = "dUDI sANTOSO"

# Ambil huruf pertama, jadikan 'B'
nama_bener = "B" + nama_salah[1:3].lower() + "i"  # Budi
nama_bener += " " + nama_salah[5].upper() + nama_salah[6:].lower()  # Santoso

print("Nama yang benar:", nama_bener)
