# PROGRAM F03 - Logout
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 1 Mei 2024
# Note: logout bisa dilakukan saat login sudah dilakukan

# Algoritma
from monster import csv_to_array

def check_login():
    return False

def logout():
    if check_login():
        logout = input("Apakah anda ingin keluar dari permainan? (iya / tidak): ")
        if logout() == "iya":
            print("User berhasil melakukan logout.")
        else:
            print("Logout dibatalkan.")
    else:
        print("User belum login.")

logout()
