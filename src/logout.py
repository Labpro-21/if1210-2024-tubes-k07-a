# PROGRAM F03 - Logout
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 1 Mei 2024
# Note: logout dilakukan saat login sudah dilaksanakan

# Algoritma
from monster import csv_to_array

def check_login():
    return False

def logout():
    if check_login():
        log_out = input("Apakah anda ingin keluar dari permainan? (iya / tidak): ")
        if log_out() == "iya":
            print("User berhasil melakukan logout.")
        else:
            print("Logout dibatalkan.")
    else:
        print("User belum login.")

logout()
