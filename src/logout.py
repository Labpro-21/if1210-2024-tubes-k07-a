# PROGRAM F03 - Logout
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 1 Mei 2024
# Note: logout dilakukan saat login sudah dilaksanakan

# Algoritma
def logout(logged_in: bool) -> bool:
    if logged_in:
        log_out = input("Apakah anda ingin keluar dari permainan? (iya / tidak): ")
        if log_out == "iya":
            print("User berhasil melakukan logout.")
            return False # sudah tidak login
        else:
            print("Logout dibatalkan.")
            return True # masih login
    else:
        print("User belum login.") 
        return False # memang belum login

