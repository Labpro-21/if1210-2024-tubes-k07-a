# PROGRAM F02 - Login
# Writer: Naomi Risaka Sitorus
# Tanggal: 30 April 2024

# KAMUS
# username, password: string
# username_found: boolean
# user_id: integer

# ALGORITMA
def login(logged_in: bool, user_id: int, array_user: list) -> (bool, str):
    if not logged_in:
        username_found = False
        username = input('Username: ')
        password = input('Password: ')
        print()
        for i in range(1, len(array_user)):
            if array_user[i][1] == username and array_user[i][2] == password:
                print('Login berhasil!')
                print('Selamat datang', array_user[i][3], username + '!')
                print('Ketik "help" untuk melihat list command yang dapat kamu gunakan.')
                user_id = i
                return True, user_id  # return login status dan user_id
            elif array_user[i][1] == username and array_user[i][2] != password:
                print('Password kamu salah!')
                username_found = True
                break
        if not username_found:
            print('Username kamu belum terdaftar!')
            print('Lakukan registrasi terlebih dahulu sebelum melakukan login.')
    else:  # logged_in = True
        print('Login gagal!')
        print('Kamu sudah login dengan akun', array_user[user_id][1] + ', lakukan logout terlebih dahulu sebelum melakukan login kembali.')
    return logged_in, user_id
