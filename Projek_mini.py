
#!/usr/bin/env python

import random

# Aturcara utama/pilihan warna
def main():
    """Mulakan permainan teka warna kereta saya."""
    print()
    print("**** PERMAINAN TEKA WARNA ****")
    print()
    print("Cuba teka warna kereta saya!")
    print("*BIRU")
    print("*MERAH JAMBU")
    print("*HIJAU")
    print("*MERAH")
    print("*PUTIH")
    print("*KELABU")

# Aturcara pilihan
    colour = [
        "BIRU",
        "MERAH JAMBU",
        "HIJAU",
        "MERAH",
        "HITAM",
        "PUTIH",
        "KELABU"
        ]

# Aturcara pilihan random
    x =random.choice(colour)
    max_trials= 6
    trial=0
    guess = None

    # Aturcara memaparkan (x)
    while trial<max_trials: # Aturcara pengulangan percubaan 
        print("Apakah warna yang ada dalam fikiran anda?")
        print()
        guess = str(input("Jawapan anda mesti ditulis dengan huruf besar : "))
        
        if x == guess:
            print(f"Tepat sekali.Anda memang seorang yang teliti".format(guess))
            break
        else:
            print(f"Nampaknya tidak bernasib baik.Boleh cuba lagi".format(guess))
            print(f"Anda ada {max_trials} peluang untuk cuba lagi.")
            max_trials -= 1
        if max_trials == 0:
            print(f"Tekaan anda sudah tamat. Sebenarnya warna kereta saya ialah: {x}.".format(guess))
    print()
    print("**** PERMAINAN TAMAT ****")
        
main()