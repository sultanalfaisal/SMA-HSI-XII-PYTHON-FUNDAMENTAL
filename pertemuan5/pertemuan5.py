def salam_pembuka():
    print("==============================")
    print("Selamat Datang di Program Saya!")
    print("==============================")

# Memanggil fungsi beberapa kali
salam_pembuka()
salam_pembuka()
salam_pembuka()
def info_cuaca(kota, cuaca):
    print(f"Cuaca di kota {kota} hari ini {cuaca}.")

# Contoh pemanggilan fungsi
info_cuaca("Jakarta", "berawan")
info_cuaca("Bandung", "hujan")
def kubik(angka):
    return angka ** 3

# Memanggil fungsi dengan angka 4
hasil_kubik = kubik(4)
print("Hasil kubik dari 4 adalah:", hasil_kubik)
def hitung_diskon(harga_awal, persen_diskon):
    jumlah_diskon = harga_awal * (persen_diskon / 100)
    harga_akhir = harga_awal - jumlah_diskon
    return harga_akhir

# Input dari pengguna
harga = float(input("Masukkan harga barang: "))
diskon = float(input("Masukkan persen diskon: "))

# Memanggil fungsi dan mencetak hasil
harga_setelah_diskon = hitung_diskon(harga, diskon)
print("Harga yang harus dibayar setelah diskon:", harga_setelah_diskon)
def fahrenheit_ke_celsius(temp_f):
    return (temp_f - 32) * 5/9

# Contoh pemanggilan
hasil_celsius = fahrenheit_ke_celsius(98.6)
print("98.6 derajat Fahrenheit sama dengan", hasil_celsius, "derajat Celsius")