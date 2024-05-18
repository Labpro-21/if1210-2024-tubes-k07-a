# PROGRAM F02 - Login
# Writer: Naomi Risaka Sitorus
# Tanggal: 30 April 2024

# KAMUS
# username, password: string
# username_found: boolean
# user_id: integer

# ALGORITMA
def login(logged_in: bool, user_id: int, array_user: list) -> (bool, str):
    print("Selamat datang Agent! Silahkan melakukan login terlebih dahulu!")
    if not logged_in:
        while True:
            print("Pilih aksi dibawah ini:")
            print("1. Login\n2. Keluar\n")
            aksi = input("Masukkan angka dari aksi yang ingin kamu lakukan: ")
            if aksi == "1":
                username_found = False
                username = input('Masukkan Username: ')
                password = input('Masukkan Password: ')
                print()
                for i in range(1, len(array_user)):
                    if array_user[i][1] == username and array_user[i][2] == password:
                        print('Login berhasil!')
                        print('Selamat datang', array_user[i][3], username + '!')
                        user_id = i
                        return True, user_id  # return login status dan user_id
                    elif array_user[i][1] == username and array_user[i][2] != password:
                        print('Password kamu salah!\n')
                        username_found = True
                        break
                if not username_found:
                    print('Username kamu belum terdaftar!')
                    print('Lakukan registrasi terlebih dahulu sebelum melakukan login atau input username dengan benar.\n')
            elif aksi == "2":
                print('Anda keluar dari aksi "LOGIN"!')
                break
            else:
                print("Input tidak valid! Silahkan melakukan input ulang.\n")

    else:  # logged_in = True
        print('Login gagal!')
        print('Kamu sudah login dengan akun', array_user[user_id][1] + ', lakukan logout terlebih dahulu sebelum melakukan login kembali.')
    return logged_in, user_id
