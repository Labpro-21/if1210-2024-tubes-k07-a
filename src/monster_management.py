# PROGRAM F13 - Monster Management
# Writer: Naomi Risaka Sitorus
# Tanggal: 8 Mei 2024

# KAMUS
# action: integer
# printing_array, temporary_array: array of array of string
# max_length_per_column: array of integer
# i: integer
# unique_type: boolean
# monster_type: string
# monster_def_power, monster_atk_power, monster_hp: integer
# confirm: string

# ALGORITMA
from monster import csv_to_array

def monster_management():
    print('Selamat datang di database monster!')
    print('1. Tampilkan semua monster')
    print('2. Tambahkan monster baru')
    action = int(input('Pilih aksi yang ingin dilakukan: '))
    while (action != 1) and (action != 2):
        print('Aksi yang dipilih tidak ditemukan.')
        action = int(input('Pilih aksi yang ingin dilakukan: '))
    if (action == 1):
        monster_array = csv_to_array (r"E:\NAOMI\University\Sem 2\Programming Fundamentals\Tubes\monster.csv")
        printing_array = [['a','b','c','d','e'] for i in range (len(monster_array) + 1)]
        printing_array [0] = ['ID', 'Type', 'ATK Power', 'DEF Power', 'HP'] #header line
        for i in range(1, len(printing_array)):
            printing_array [i] = monster_array [i-1]

        #print array in form of a structured table
        max_length_per_column = [max(map(len, column)) for column in zip(*printing_array)]
        for row in printing_array:
            print(" | ".join("{:{}}".format(element, length) for element, length in zip(row, max_length_per_column)))
    
    else: #action == 2
        print('Saatnya membuat monster baru!')
        monster_type = input('Masukkan tipe atau nama: ') 
        unique_type = True
        i = 0
        while (i < len(monster_array)) and (unique_type):
            if (monster_array [i] == monster_type):
                unique_type = False
            i += 1
        while not(unique_type):
            monster_type = input('Masukkan tipe atau nama: ') 

        monster_atk_power = int(input('Masukkan ATK Power: '))
        while not(monster_atk_power.isdigit()):
            monster_atk_power = int(input('Masukkan ATK Power: '))

        monster_def_power = int(input('Masukkan DEF Power (0-50): ')) 
        while (not(monster_def_power.isdigit())) or (monster_def_power.isdigit() and ((monster_def_power < 0) or (monster_def_power > 50))):
            monster_def_power = int(input('Masukkan DEF Power: '))

        monster_hp = int(input('Masukkan HP: '))
        while not(monster_hp.isdigit()):
            monster_hp = int(input('Masukkan HP: '))
        print()
    
        print('Monser baru berhasil dibuat!')
        print('Type:', monster_type)
        print('ATK Power:', monster_atk_power)
        print('DEF Power:', monster_def_power)
        print('HP:', monster_hp)

        confirm = input('Tambahkan monster ke database (Y/N): ')
        while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
            print('Input tidak valid!')
            confirm = input('Lanjutkan upgrade (Y/N): ')
        if (confirm == 'Y') or (confirm == 'y'):
            #add new monster details
            temporary_array = [['a','b','c','d','e'] for i in range (len(monster_array) + 1)]
            temporary_array [0] = [
                (monster_array [len(monster_array) - 1][0] + 1), monster_type, monster_atk_power, monster_def_power, monster_hp] 
            for i in range(1, len(temporary_array)):
                temporary_array [i] = monster_array [i-1]
            monster_array = temporary_array
            print('Monster berhasil ditambahkan ke database!')
        else: #(confirm == 'N') or (confirm == 'n'):
            print('Monster gagal ditambahkan ke database!')

    return monster_array

monster_management()
