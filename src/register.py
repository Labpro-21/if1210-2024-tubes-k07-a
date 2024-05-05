# PROGRAM F01 - Register
# Writer: Bertha Soliany Frandi
# Tanggal: 1 Mei 2024

# KAMUS

# ALGORITMA
from monster import csv_to_array

# array ini hanya untuk contoh karena sebelumnya sudah dipanggil di main
array_csv_user = csv_to_array(r"c:\Data lain\BERTHA\Python\TUBES\user.csv")
array_csv_monster = csv_to_array(r"c:\Data lain\BERTHA\Python\TUBES\monster.csv")
array_csv_monster_inventory = csv_to_array(r"c:\Data lain\BERTHA\Python\TUBES\testmonster_inventory.csv")

logged_in = False # delete setelah sudah di main (berarti di login harus ada return logged_in)

def register():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if logged_in:
        print("Register gagal")
        print(f"Anda masih login dengan username {username}. Silahkan logout terlebih dahulu sebelum melakukan register.")
    else:
        cekValid(username, password)
            
def cekValid(username, password):
    # convert to ASCII
    list_usn = []   # inisialisasi list of character dari username
    for letter in username: # mengubah username dari string ["halo"] menjadi list of character ['h','a','l','o']
        list_usn.append(letter) 
    list_ascii = [0 for i in range(len(username))] # inisialisasi list ASCII
    for i in range(len(username)): # mengubah username menjadi ASCII 
        list_ascii[i] = ord(username[i])
    # pengecekan input username
    valid = False
    for i in list_ascii: 
        if i==45 or i==95 or (i>=48 and i<=57) or (i>=65 and i<=90) or (i>=97 and i<=122): # kondisi adalah nilai ASCII yang diperbolehkan untuk username
            valid = True
        else:
            valid = False
            break
    if valid == False:
        print("Username hanya boleh berisi alfabet, angka, undescore, dan strip.")
    else:
        ada = False
        for i in range(len(array_csv_user)):
            if array_csv_user[i][1] == username:
                print(f"Username sudah terpakai, silahkan gunakan username lain.")
                ada = True
                break
        if not(ada):
            cekPassword(password)
            # menyimpan data user baru
            data_user = [0 for i in range(5)]
            maks = -1
            for i in range(1, len(array_csv_user)):
                if int(array_csv_user[i][0]) < maks:
                        maks = int(array_csv_user[i][0])
            data_user = [str(int(array_csv_user[maks][0]) + 1), username, password, 'agent', '0']
            array_csv_user.append(data_user) # menyimpan user baru ke array csv user
            # untuk pilih monster awal
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            batas_awal = 9999
            batas_akhir = -1
            for i in range(len(array_csv_monster)):
                if i != 0:
                    print(array_csv_monster[i][0],".",end=" ")
                    print(array_csv_monster[i][1])
                    if i <= batas_awal:
                        batas_awal = i
                    if i >= batas_akhir:
                        batas_akhir = i 
            print()
            monster_pilihan = int(input("Monster pilihanmu: "))
            while monster_pilihan < batas_awal or monster_pilihan > batas_akhir:
                print("input tidak valid. Coba pilih ulang.")
                monster_pilihan = int(input("Monster pilihanmu: "))
            nama_monster_pilihan = array_csv_monster[monster_pilihan][1]
            print()
            print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {nama_monster_pilihan}!")
            # menyimpan monster pilihan ke array csv monster_inventory
            data_monster_inventory = [data_user[0], str(monster_pilihan), '1']
            array_csv_monster_inventory.append(data_monster_inventory)

def cekPassword(password):
    pw = True
    while pw:
        list_pw = []   # inisialisasi list of character dari password
        for letter in password: # mengubah password dari string ["halo"] menjadi list of character ['h','a','l','o']
            list_pw.append(letter)
        list_pw_ascii = [0 for i in range(len(password))] # inisialisasi list ASCII
        for i in range(len(password)): # mengubah username menjadi ASCII 
            list_pw_ascii[i] = ord(password[i])
        count = 0
        for i in list_pw_ascii:
            if i == 32:
                count+=1
        if count == 0:
            pw = False
        else:
            print("Password tidak boleh menggunakan spasi. Masukkan kembali password baru.")
            password = input("Masukkan password: ")
        if password == '':
            print("Password tidak boleh kosong. Masukkan kembali password baru")
            password = input("Masukkan password: ")
    return password

register()
