#2
email = input("Masukkan alamat email: ").strip()

valid = ("@" in email) and email.endswith((".com", ".co.id"))

if valid:
    print("Email valid")
else:
    print("Email tidak valid")