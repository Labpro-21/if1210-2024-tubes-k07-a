# PROGRAM F01 - Register
# Writer: Bertha Soliany Frandi
# Tanggal: 1 Mei 2024

# KAMUS

# ALGORITMA
from monster import csv_to_array

# sesuaikan filepath
array_csv_user = csv_to_array(r"c:\Data lain\BERTHA\Python\TUBES\test.csv")
array_csv_monster = csv_to_array(r"c:\Data lain\BERTHA\Python\TUBES\monster.csv")

logged_in = False # delete setelah disatuin dengan F02 - Login

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
            # data_user untuk input di csv
            data_user = [0 for i in range(5)]
            maks = -1
            for i in range(1, len(array_csv_user)):
                if int(array_csv_user[i][0]) < maks:
                        maks = int(array_csv_user[i][0])
            for i in range(5):
                data_user[0] = str(int(array_csv_user[maks][0]) + 1) + ";"
                data_user[1] = username + ";"
                data_user[2] = password + ";"
                data_user[3] = "agent;"
                data_user[4] = "0"
            write_csv_user(data_user) # mendaftarkan data user ke csv
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
            write_csv_monster(data_user, monster_pilihan)

def write_csv_user(data_user):
    with open(r"c:\Data lain\BERTHA\Python\TUBES\test.csv", "a", newline="") as file: # filepath nanti diganti
        for i in range(1):
            for line in data_user:
                file.write(line)
            file.write('\n')

def write_csv_monster(data_user, monster_pilihan):
    with open(r"c:\Data lain\BERTHA\Python\TUBES\testmonster_inventory.csv", "a", newline="") as file: # filepath nanti diganti
        data_monster = [0 for i in range(3)]
        for i in range(3):
            data_monster[0] = data_user[0]
            data_monster[1] = str(monster_pilihan) + ";"
            data_monster[2] = "1"
        for i in range(1):
            for line in data_monster:
                file.write(line)
            file.write('\n')

register()