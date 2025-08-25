# Latihan 2: Hitung Rata-rata Spam Confidence

nama_file = input("Masukkan nama file (contoh: mbox-short.txt): ")

try:
    with open(nama_file, 'r', encoding='utf-8') as file:
        total = 0
        jumlah = 0
        
        for baris in file:
            if baris.startswith("X-DSPAM-Confidence:"):
                # Ambil bagian angka
                nilai = float(baris.strip().split(":")[1])
                total += nilai
                jumlah += 1
        
        if jumlah > 0:
            rata_rata = total / jumlah
            print("Rata-rata spam confidence:", rata_rata)
        else:
            print("Tidak ada baris 'X-DSPAM-Confidence:' ditemukan.")
except FileNotFoundError:
    print("File tidak ditemukan. Pastikan nama file benar.")