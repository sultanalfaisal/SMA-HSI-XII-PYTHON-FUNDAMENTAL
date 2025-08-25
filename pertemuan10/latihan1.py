#1
# Standarisasi Judul ke Title Case (dengan pengabaian kata pendek umum)
judul = input("Masukkan judul buku: ").strip()

# bersihkan spasi berlebih di tengah
while "  " in judul:
    judul = judul.replace("  ", " ")

kata_kecil = {"dan", "di", "ke", "yang", "atau", "dari", "untuk", "pada"}
kata = judul.lower().split()

hasil = []
for i, k in enumerate(kata):
    if i == 0 or k not in kata_kecil:
        hasil.append(k.capitalize())
    else:
        hasil.append(k)

judul_baru = " ".join(hasil)
print("Judul terstandarisasi:", judul_baru)
