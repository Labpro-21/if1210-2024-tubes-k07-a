# PROGRAM F02 - Login
# Writer: Naomi Risaka Sitorus
# Tanggal: 30 April 2024

# KAMUS
# username, password: string
# username_found: boolean

# ALGORITMA
from monster import csv_to_array
def login():
    username_found = False
    if not(logged_in):
        username = input('Username: ')
        password = input('Password: ')
        print()
        for i in range (len(array[0])):
            if (array[0][i] == username and array[1][i] == password):
                print('Login berhasil!')
                print('Selamat datang Agent', username + '!')
                print('Ketik "help" untuk melihat list command yang dapat kamu gunakan.')
                logged_in = True
                username_found = True
                break
            elif (array[0][i] == username):
                print('Password kamu salah!')
                username_found = True
                break
        if not(username_found):
            print('Username kamu belum terdaftar!')
            print('Lakukan registrasi terlebih dahulu sebelum melakukan login.')
    else: #logged_in = True
        print('Login gagal!')
        username = 'udahlogin123' #nanti remove, nanti data username harus disimpan from prev
        print('Kamu sudah login dengan akun', username + ', lakukan logout terlebih dahulu sebelum melakukan login kembali.')

login()