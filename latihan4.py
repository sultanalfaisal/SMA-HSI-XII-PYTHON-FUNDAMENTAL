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

# LATIHAN 2
def hitung_upah(jam_kerja, tarif_per_jam):
    if jam_kerja > 40:
        upah_normal = 40 * tarif_per_jam
        jam_lembur = jam_kerja - 40
        upah_lembur = jam_lembur * tarif_per_jam * 1.5
        total_upah = upah_normal + upah_lembur
    else:
        total_upah = jam_kerja * tarif_per_jam
    return total_upah

try:
    jam = float(input("Masukkan jam kerja: "))
    tarif = float(input("Masukkan tarif per jam: "))
    total = hitung_upah(jam, tarif)
    print(f"Pay: {total}")
except ValueError:
    print("Error, please enter numeric input")


# LATIHAN 3
try:
    skor = float(input("Masukkan skor (0.0 - 1.0): "))
    
    if skor < 0.0 or skor > 1.0:
        print("Bad score")
    else:
        if skor >= 0.9:
            grade = 'A'
        elif skor >= 0.8:
            grade = 'B'
        elif skor >= 0.7:
            grade = 'C'
        elif skor >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Grade: {grade}")
except ValueError:
    print("Error, please enter numeric input")


# LATIHAN 4
# Variabel untuk pengujian
tinggi_cm = 160  # contoh tinggi
usia = 10        # contoh usia
didampingi_ortu = True  # contoh status didampingi orang tua

# Logika untuk menentukan apakah boleh masuk
if tinggi_cm >= 150 and (usia > 12 or didampingi_ortu):
    print("Boleh Masuk")
else:
    print("Tidak Boleh Masuk")
