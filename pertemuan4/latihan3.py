# LATIHAN 3
try:
    skor = float(input("Masukkan skor (0.0 - 1.0): "))
    
    if skor < 0.0 or skor > 1.0:
        print("Bad score")
    else:
        if skor >= 0.9:
            grade = 'A'
        elif skor >= 0.8:
            grade = 'B'
        elif skor >= 0.7:
            grade = 'C'
        elif skor >= 0.6:
            grade = 'D'
        else:
            grade = 'F'
        print(f"Grade: {grade}")
except ValueError:
    print("Error, please enter numeric input")