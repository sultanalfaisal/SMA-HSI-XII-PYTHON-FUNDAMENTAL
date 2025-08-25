for i in range(0, 71, 7):
    print(i)

kalimat = "Python"
kalimat_terbalik = ""

for huruf in kalimat:
    kalimat_terbalik = huruf + kalimat_terbalik

print(kalimat_terbalik)
count = 0

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print("Jumlah angka yang habis dibagi 3 dan 5:", count)

for i in range(5, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

n = int(input("Masukkan angka: "))
hasil_faktorial = 1

for i in range(1, n + 1):
    hasil_faktorial *= i

print(f"Faktorial dari {n} adalah {hasil_faktorial}")
