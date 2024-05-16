# PROGRAM F13 - Monster Management
# Writer: Naomi Risaka Sitorus
# Tanggal: 8 Mei 2024

# KAMUS
# i: integer
# new_monster: array of string
# unique_type: boolean
# action, monster_type, monster_def_power, monster_atk_power, monster_hp, confirm : string

# ALGORITMA
def is_integer(user_input: str) -> bool:
    for char in user_input:
        if (ord(char) <= ord('0')) or (ord(char) >= ord('9')):
            return False
    return True

def monster_management(array_monster: list) -> list:
    print('Selamat datang di database monster!')
    print('1. Tampilkan semua monster')
    print('2. Tambahkan monster baru')
    action = input('>>> Pilih aksi yang ingin dilakukan: ')
    while (action != '1') and (action != '2'):
        print('Aksi yang dipilih tidak ditemukan.')
        action = input('Pilih aksi yang ingin dilakukan: ')
    if (action == '1'):
        print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<10} | {'DEF Power':<10} | {'HP':<5}")
        for i in range (1, len(array_monster)):
            print(f"{array_monster[i][0]:<3} | {array_monster[i][1]:<15} | {array_monster[i][2]:<10} | {array_monster[i][3]:<10} | {array_monster[i][4]:<5}")
    
    else: #action == 2
        print('Saatnya membuat monster baru!')
        monster_type = input('>>> Masukkan tipe atau nama: ') 
        unique_type = True
        i = 0
        while (i < len(array_monster)) and (unique_type):
            if (array_monster [i] == monster_type):
                unique_type = False
            i += 1
        while not(unique_type):
            print('Input tidak valid!')
            monster_type = input('>>> Masukkan tipe atau nama: ') 

        monster_atk_power = input('>>> Masukkan ATK Power: ')
        while not(is_integer(monster_atk_power)):
            print('Input tidak valid!')
            monster_atk_power = input('>>> Masukkan ATK Power: ')

        monster_def_power = (input('>>> Masukkan DEF Power (0-50): '))
        while not(is_integer(monster_def_power)) or (is_integer (monster_def_power) and (int(monster_def_power) < 0 or (int(monster_def_power) > 50))):
            print('Input tidak valid!')
            monster_def_power = (input('>>> Masukkan DEF Power: '))

        monster_hp = input('>>> Masukkan HP: ')
        while not(is_integer(monster_hp)):
            print('Input tidak valid!')
            monster_hp = input('>>> Masukkan HP: ')
        print()
    
        print('Monser baru berhasil dibuat!')
        print('Type:', monster_type)
        print('ATK Power:', monster_atk_power)
        print('DEF Power:', monster_def_power)
        print('HP:', monster_hp)

        confirm = input('>>> Tambahkan monster ke database (Y/N): ')
        while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
            print('Input tidak valid!')
            confirm = input('>>> Lanjutkan upgrade (Y/N): ')
        if (confirm == 'Y') or (confirm == 'y'):
            #add new monster details
            new_monster = [
                (int(array_monster [len(array_monster) - 1][0]) + 1), monster_type, monster_atk_power, monster_def_power, monster_hp] 
            array_monster.append(new_monster)
            print('Monster berhasil ditambahkan ke database!')
        else: #(confirm == 'N') or (confirm == 'n'):
            print('Monster gagal ditambahkan ke database!')
    return array_monster
