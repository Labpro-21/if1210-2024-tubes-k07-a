#reading csv file, arusnya bukan di modul ini
import csv                         
user_file = open('user.csv', 'r')
reader = csv.reader(user_file, delimiter = ';')

def Login():
# Membuat user masuk (log in) ke dalam akun sesuai input yang dimasukkan apabila akun ada dan password sesuai
# KAMUS LOKAL
# username, password: string
# username_found: boolean
# ALGORITMA
    logged_in = False #harusnya bukan di modul ini tapi logged_in dan username var global
    username_found = False
    if not(logged_in):
        username = input('Username: ')
        password = input('Password: ')
        print()
        for row in reader:
            if (row[1] == username and row[2] == password):
                print('Login berhasil!')
                print('Selamat datang Agent', username + '!')
                print('Ketik "help" untuk melihat list command yang dapat kamu gunakan.')
                logged_in = True
                username_found = True
                break
            elif (row[1] == username):
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

Login() #hanya untuk coba run di subprogram ini