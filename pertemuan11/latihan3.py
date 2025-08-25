# Latihan 3: Easter Egg File

nama_file = input("Masukkan nama file: ")

if nama_file.lower() == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
else:
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            for baris in file:
                print(baris.upper().strip())
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
