#4
def analisis_daftar(daftar_angka):
    """
    Menganalisis daftar angka dan mengembalikan total, jumlah elemen, dan rata-ratanya.

    Args:
        daftar_angka (list): Daftar angka (int atau float).

    Returns:
        tuple: (total, jumlah elemen, rata-rata)
    """
    total = sum(daftar_angka)
    jumlah_elemen = len(daftar_angka)
    rata_rata = total / jumlah_elemen
    return total, jumlah_elemen, rata_rata

help(analisis_daftar)