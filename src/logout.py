# PROGRAM F03 - Logout
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 1 Mei 2024
# Note: logout dilakukan saat login sudah dilaksanakan

# Algoritma
def logout(logged_in: bool) -> bool:
    if logged_in:
        log_out = input("Apakah anda ingin keluar dari permainan? (Y/N): ").upper()
        while True:
            if log_out == "Y":
                print("User berhasil melakukan logout!")
                return False # sudah tidak login
            elif log_out == "N":
                print("Logout dibatalkan! Silahkan melanjutkan misi kembali.")
                return True # masih login
            else:
                print("Input tidak valid. Masukkan antara Y/N.")
                log_out = input("Apakah anda ingin keluar dari permainan? (Y/N): ").upper()
    else:
        print("User belum login!") 
        return False # memang belum login

