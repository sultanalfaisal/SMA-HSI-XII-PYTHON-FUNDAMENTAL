#1
def buat_email(nama_pengguna, domain="coding.com"):
    return f"{nama_pengguna.lower()}@{domain.lower()}"

print(buat_email("Budi"))              
print(buat_email("Ani", "belajar.id")) 
