#5
import re

judul = input("Masukkan judul artikel: ").strip().lower()

# ganti spasi berlebih menjadi satu spasi
judul = re.sub(r"\s+", " ", judul)

# ganti spasi dengan tanda hubung
slug = judul.replace(" ", "-")

# BONUS: hapus semua karakter selain huruf, angka, dan tanda hubung
slug = re.sub(r"[^a-z0-9\-]", "", slug)

# rapikan: hilangkan hubung ganda dan hubung di awal/akhir
slug = re.sub(r"-{2,}", "-", slug).strip("-")

print("Slug:", slug)