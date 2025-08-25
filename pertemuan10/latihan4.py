#4
nama_org = input("Masukkan nama organisasi: ").strip()

# pisah berdasarkan spasi, abaikan entri kosong
kata = [k for k in nama_org.split() if k]
akronim = "".join(k[0] for k in kata).upper()

print("Akronim:", akronim)
