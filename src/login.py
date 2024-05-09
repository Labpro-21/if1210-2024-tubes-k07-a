# PROGRAM F02 - Login
# Writer: Naomi Risaka Sitorus
# Tanggal: 30 April 2024

# KAMUS
# username, password: string
# username_found: boolean
# user_id: integer

# ALGORITMA
from monster import csv_to_array

user_id = 0
user_id = []
def login(logged_in, user_id, array):
    if not logged_in:
        array = csv_to_array (r"E:\NAOMI\University\Sem 2\Programming Fundamentals\Tubes\user.csv")
        username_found = False
        username = input('Username: ')
        password = input('Password: ')
        print()
        for i in range(1, len(array)):
            if array[i][1] == username and array[i][2] == password:
                print('Login berhasil!')
                print('Selamat datang Agent', username + '!')
                print('Ketik "help" untuk melihat list command yang dapat kamu gunakan.')
                user_id = i
                return True  # return login status
            elif array[i][1] == username and array[i][2] != password:
                print('Password kamu salah!')
                username_found = True
                break
        if not username_found:
            print('Username kamu belum terdaftar!')
            print('Lakukan registrasi terlebih dahulu sebelum melakukan login.')
    else:  # logged_in = True
        print('Login gagal!')
        print('Kamu sudah login dengan akun', username + ', lakukan logout terlebih dahulu sebelum melakukan login kembali.')
    return logged_in, user_id, array
