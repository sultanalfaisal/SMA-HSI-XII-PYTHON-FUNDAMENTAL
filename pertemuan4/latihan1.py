# LATIHAN 1
def hitung_upah(jam_kerja, tarif_per_jam):
    if jam_kerja > 40:
        upah_normal = 40 * tarif_per_jam
        jam_lembur = jam_kerja - 40
        upah_lembur = jam_lembur * tarif_per_jam * 1.5
        total_upah = upah_normal + upah_lembur
    else:
        total_upah = jam_kerja * tarif_per_jam
    return total_upah

# Input dari pengguna
jam = float(input("Masukkan jam kerja: "))
tarif = float(input("Masukkan tarif per jam: "))

# Hitung dan tampilkan total upah
total = hitung_upah(jam, tarif)
print(f"Pay: {total}")
