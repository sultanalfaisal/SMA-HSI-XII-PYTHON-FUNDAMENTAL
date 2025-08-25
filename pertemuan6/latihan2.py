#2
def kirim_paket(barang, tujuan, berat_kg, asuransi=False, express=False):
    print(f"Mengirim {barang} ke {tujuan}, berat {berat_kg}kg, express={express}, asuransi={asuransi}")

kirim_paket(barang="Buku", tujuan="Bandung", berat_kg=2, express=True)