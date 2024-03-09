import random
import os
import time

# while True:
#     print("-" * 20)
#     print("Game Lubang-lubang")
#     print("\n|__| |__| |__| |__|")
#     print("-" * 20)
#     n = int(input("Pilih lubang 1 Sd. 4 : "))

#     pilihan = random.randint(1, 4)
#     if n == pilihan:
#         print("Anjay Benar")
#     else:
#         print("Cupu Dek")
#     time.sleep(5)
#     os.system('cls')


while True:
    print("Game Gajah semut dan orang")
    print("1. Gajah")
    print("2. Semut")
    print("3. Orang")
    n = int(input("Mau 1/2/3 : "))
    pilihan = random.randint(1, 3)
    print(f"Anda {n} vs Komputer {pilihan}")
    if n == 1:
        if pilihan == 1:
            print("Seri")
        elif pilihan == 2:
            print("Yah Kalah")
        else:
            print("Cie Menang")
    elif n == 2:
        if pilihan == 1:
            print("Cie Menang")
        elif pilihan == 2:
            print("Seri")
        else:
            print("Yah kalah")
    else:
        if pilihan == 1:
            print("Yah Kalah")
        elif pilihan == 2:
            print("Cie Menang")
        else:
            print("Seri")
    time.sleep(10)
    os.system('cls')