# PROGRAM F01 - Register
# Writer: Bertha Soliany Frandi
# Tanggal: 1 Mei 2024

# ALGORITMA
def is_integer(user_input: str):
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def register(logged_in: bool, array_user: list, array_monster: list, array_monster_inventory: list ):
    # KAMUS LOKAL
    # username, password: string
    # valid, ada : bool
    # maks, batas_awal, batas_akhir : integer
    # monster_pilihan, nama_monster_pilihan : string
    # list_usn: array of character
    # list_ascii: array of integer
    # data_user, data_monster_inventory : array of string

    # ALGORITMA
    print("Selamat datang di register!\n")
    while True:
        print("Pilih aksi dibawah ini:")
        print("1. Register\n2. Keluar\n")
        aksi = input("Masukkan angka dari aksi yang ingin kamu lakukan: ")

        if aksi == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")

            print()
            # syarat dimana user tidak boleh dalam keadaan sedang login
            if logged_in == True:
                print("Register gagal")
                print(f"Anda masih login dengan username {username}. Silahkan logout terlebih dahulu sebelum melakukan register.")
            else:
                # syarat username yang hanya boleh berisi alfabet, angka, undescore, dan strip
                # convert to ASCII
                list_usn = []   # inisialisasi list of character dari username
                for letter in username:
                    list_usn.append(letter) 
                # mengubah username menjadi ASCII
                list_ascii = [0 for i in range(len(username))] # inisialisasi array ASCII
                for i in range(len(username)): 
                    list_ascii[i] = ord(username[i])

                # pengecekan input username
                valid = False
                for i in list_ascii: 
                    if i==45 or i==95 or (i>=48 and i<=57) or (i>=65 and i<=90) or (i>=97 and i<=122): # kondisi adalah nilai ASCII yang diperbolehkan untuk username
                        valid = True
                    else:
                        valid = False
                if valid == False:
                    print("Username hanya boleh berisi alfabet, angka, undescore, dan strip.\n")
                else:
                    # syarat username yang tidak boleh sama seperti agent lain yang sudah ada
                    ada = False
                    for i in range(len(array_user)):
                        if array_user[i][1] == username:
                            print(f"Username sudah terpakai, silahkan gunakan username lain.\n")
                            ada = True
                        else: 
                            ada = False

                    if ada == False:
                        # melakukan pengecekan terhadap password
                        cekPassword(password)

                        # menyimpan data user baru
                        data_user = [0 for i in range(5)]
                        maks = -1
                        for i in range(1, len(array_user)):
                            if int(array_user[i][0]) < maks:
                                    maks = int(array_user[i][0])
                        data_user = [str(int(array_user[maks][0]) + 1), username, password, 'agent', '0']
                        array_user.append(data_user) # menyimpan user baru ke baris paling bawah di array_user
                        print()

                        # untuk memilih monster awal
                        print("Silahkan pilih salah satu monster sebagai monster awalmu.")
                        batas_awal = 9999
                        batas_akhir = -1
                        for i in range(len(array_monster)):
                            if i != 0 and i <= 3:
                                print(f"{i}"+".",end=" ")
                                print(array_monster[i][1])
                                if i <= batas_awal:
                                    batas_awal = i
                                if i >= batas_akhir:
                                    batas_akhir = i 
                        print()
                        print("Masukkan angka dari monster yang dipilih.")
                        monster_pilihan = input("Monster pilihanmu: ")
                        while True:
                            if monster_pilihan == '':
                                print("Monster harus dipilih dan tidak boleh kosong. Masukkan angka untuk monster yang ingin pilih.\n")
                            elif(is_integer(monster_pilihan)) and (int(monster_pilihan) <= 3 and int(monster_pilihan) >= 1):
                                monster_pilihan = int(monster_pilihan)
                                break
                            else:
                                print("Input tidak valid. Coba pilih ulang.\n")
                            monster_pilihan = input("Monster pilihanmu: ")

                        nama_monster_pilihan = array_monster[monster_pilihan][1]
                        print()
                        print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {nama_monster_pilihan}!")
                        # menyimpan monster pilihan ke array csv monster_inventory
                        data_monster_inventory = [data_user[0], str(monster_pilihan), '1']
                        array_monster_inventory.append(data_monster_inventory)
                        break
        elif aksi == "2":
            print("Anda keluar dari register!")
            break
        else:
            print("Aksi tidak valid! Pilih ulang aksi yang ingin dilakukan!\n")

def cekPassword(password: str) -> str:
    # KAMUS LOKAL
    # pw : bool
    # count : integer
    # list_pw : array of character
    # list_pw_ascii : array of integer

    # ALGORITMA
    pw = True
    while pw:
        list_pw = []   # inisialisasi array of character dari password
        for letter in password: # mengubah password dari string ["halo"] menjadi list of character ['h','a','l','o']
            list_pw.append(letter)
        list_pw_ascii = [0 for i in range(len(password))] # inisialisasi array ASCII
        for i in range(len(password)): # mengubah username menjadi ASCII 
            list_pw_ascii[i] = ord(password[i])
        count = 0
        for i in list_pw_ascii:
            if i == 32:
                count+=1
        if count == 0:
            pw = False
        else:
            print("Password tidak boleh menggunakan spasi. Masukkan kembali password baru.\n")
            password = input("Masukkan password: ")
        if password == '':
            print("Password tidak boleh kosong. Masukkan kembali password baru.\n")
            password = input("Masukkan password: ")
    return password