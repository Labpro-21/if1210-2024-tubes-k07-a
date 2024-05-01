# PROGRAM Logout
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 28 April 2024
# Note: logout bisa dilakukan saat login sudah dilakukan

import os
def login():
    return True
# memastikan user sudah melakukan log in

def logout():
    if login():
        logout = input ("Apakah anda ingin keluar dari permainan? (iya / tidak):")
        if logout == "tidak":
            exit()
        else:
            os.system("logout")
    else:
        print("User sudah keluar dari permainan.")

logout()