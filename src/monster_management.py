# PROGRAM F13 - Monster Management
# Writer: Naomi Risaka Sitorus
# Tanggal: 8 Mei 2024

# KAMUS

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
        max_length_per_column = [max(map(len, column)) for column in zip(*monster_array)]
        for row in monster_array:
            print(" | ".join("{:{}}".format(element, length) for element, length in zip(row, max_length_per_column))) #HEADER NOT YET MADE
    else: #action == 2
        print('Saatnya membuat monster baru!')
        monster_type = input('Masukkan tipe atau nama: ') #VALIDATION NOT YET MADE
        monster_atk_power = int(input('Masukkan ATK Power: '))
        monster_def_power = int(input('Masukkan DEF Power (0-50): ')) 
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
            print('Monster berhasil ditambahkan ke database!')
            #PENAMBAHAN MONSTER KE ARRAY NOT YET DONE
        else:
            print('Monster gagal ditambahkan ke database!')

monster_management()