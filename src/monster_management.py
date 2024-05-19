# PROGRAM F13 - Monster Management
# Writer: Naomi Risaka Sitorus
# Tanggal: 8 Mei 2024

# FUNGSI & PROSEDUR
def is_integer(user_input: str) -> bool:
# Menerima sebuah masukan berupa string dan mengembalikan True jika input tersebut merupakan sebuah integer serta False jika tidak
# KAMUS LOKAL
# -
# ALGORITMA
    for char in user_input:
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def monster_management(array_monster: list) -> list:
# Menampilkan semua monster yang ada dalam game serta menambahkan monster baru ke dalam game berdasarkan masukan user
# KAMUS LOKAL
# i: integer
# new_monster: array of string
# unique_type: boolean
# action, monster_type, monster_def_power, monster_atk_power, monster_hp, confirm : string
# ALGORITMA
    while True:
        print('\nSelamat datang di database monster!')
        print('1. Tampilkan semua monster')
        print('2. Tambahkan monster baru')
        print('3. Keluar\n')
        action = input('>>> Pilih aksi yang ingin dilakukan: ')
        
        while (action != '1') and (action != '2') and (action != '3'):
            print('Aksi yang dipilih tidak ditemukan.\n')
            action = input('>>> Pilih aksi yang ingin dilakukan: ')
        
        print()
        if (action == '1'):
            print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<10} | {'DEF Power':<10} | {'HP':<5}")
            for i in range (1, len(array_monster)):
                print(f"{array_monster[i][0]:<3} | {array_monster[i][1]:<15} | {array_monster[i][2]:<10} | {array_monster[i][3]:<10} | {array_monster[i][4]:<5}")
        
        elif (action == '2'): #action == 2
            print('Saatnya membuat monster baru!')
            monster_type = input('>>> Masukkan tipe atau nama: ') 
            unique_type = True
            i = 0
            while (i < len(array_monster)) and (unique_type):
                if (array_monster [i] == monster_type):
                    unique_type = False
                i += 1
            while not(unique_type) or monster_type == "":
                print('Input tidak valid!')
                monster_type = input('>>> Masukkan tipe atau nama: ') 

            monster_atk_power = input('>>> Masukkan ATK Power: ')
            while not(is_integer(monster_atk_power)) or monster_atk_power == "":
                print('Input tidak valid!')
                monster_atk_power = input('>>> Masukkan ATK Power: ')

            monster_def_power = (input('>>> Masukkan DEF Power (0-50): '))
            while monster_def_power == "" or not(is_integer(monster_def_power)) or (is_integer (monster_def_power) and (int(monster_def_power) < 0 or (int(monster_def_power) > 50))):
                print('Input tidak valid!')
                monster_def_power = (input('>>> Masukkan DEF Power: '))

            monster_hp = input('>>> Masukkan HP: ')
            while not(is_integer(monster_hp)) or monster_hp == "":
                print('Input tidak valid!')
                monster_hp = input('>>> Masukkan HP: ')
            print()
        
            print('Monser baru berhasil dibuat!\n')
            print('Type:', monster_type)
            print('ATK Power:', monster_atk_power)
            print('DEF Power:', monster_def_power)
            print('HP:', monster_hp)

            print()
            confirm = input('>>> Tambahkan monster ke database (Y/N): ').upper()
            while (confirm != 'Y')  and (confirm != 'N') and (confirm == ""):
                print('Input tidak valid!')
                confirm = input('>>> Tambahkan monster ke database (Y/N): ').upper()
            if (confirm == 'Y'):
                #add new monster details
                new_monster = [
                    str((int(array_monster [len(array_monster) - 1][0]) + 1)), monster_type, monster_atk_power, monster_def_power, monster_hp] 
                array_monster.append(new_monster)
                print('\nMonster berhasil ditambahkan ke database!')
            else: #(confirm == 'N'):
                print('\nMonster gagal ditambahkan ke database!')
        elif (action == '3'):
            print("Anda keluar dari database monster!")
            break
    return array_monster
