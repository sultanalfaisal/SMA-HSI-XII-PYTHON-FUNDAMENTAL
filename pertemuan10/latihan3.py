#3
kalimat = input("Masukkan kalimat: ")
kata_sensor = input("Masukkan kata yang ingin disensor: ")

# Sensor case-insensitive: samakan casing saat mencari, tapi bangun hasilnya dengan replace sederhana
# Jika ingin case-sensitive, cukup pakai: kalimat.replace(kata_sensor, "***")
import re
pola = re.compile(re.escape(kata_sensor), re.IGNORECASE)
hasil = pola.sub("***", kalimat)

print("Hasil sensor:", hasil)