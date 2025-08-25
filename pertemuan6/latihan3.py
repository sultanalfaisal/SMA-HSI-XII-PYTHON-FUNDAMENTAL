#3
def analisis_daftar(daftar_angka):
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

angka = [10, 20, 30, 40, 50]
total, jumlah, rata2 = analisis_daftar(angka)

print("Total:", total)
print("Jumlah elemen:", jumlah)
print("Rata-rata:", rata2)