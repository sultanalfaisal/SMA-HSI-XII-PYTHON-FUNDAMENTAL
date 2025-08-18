# Countdown dari 10 sampai 1
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1  # Mengurangi nilai countdown
print("Blastoff!")

# Game Tebak Angka
angka_rahasia = 7
while True:  # Loop tak terbatas
    try:
        tebakan = int(input("Tebak angka (antara 1-10): "))  # Minta input pengguna
        if tebakan == angka_rahasia:
            print("Selamat, tebakan Anda benar!")
            break  # Keluar dari loop jika tebakan benar
        else:
            print("Salah, coba lagi!")
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")
print("Terima kasih sudah bermain!")

# Input Angka Cerdas
total = 0
count = 0

while True:
    user_input = input("Masukkan angka (atau ketik 'done' untuk berhenti): ")
    if user_input.lower() == "done":
        break  # Keluar dari loop jika pengguna mengetik 'done'
    try:
        angka = float(user_input)  # Konversi input ke float
        total += angka  # Menjumlahkan angka
        count += 1  # Menghitung jumlah angka yang dimasukkan
    except ValueError:
        print("Input tidak valid, silakan masukkan angka.")

# Menghitung rata-rata
if count > 0:
    rata_rata = total / count
    print(f"Total: {total}, Jumlah angka: {count}, Rata-rata: {rata_rata}")
else:
    print("Tidak ada angka yang dimasukkan.")
