# PROGRAM F13 - Monster Management
# Writer: Naomi Risaka Sitorus
# Tanggal: 8 Mei 2024
# Note : print array masih pakai fungsi map

# KAMUS
# action, i: integer
# printing_array, temporary_array: array of array of string
# max_length_per_column: array of integer
# unique_type: boolean
# monster_type, monster_def_power, monster_atk_power, monster_hp, confirm : string

# ALGORITMA
def is_integer(user_input):
    for char in user_input:
        if (ord(char) <= ord('0')) or (ord(char) >= ord('9')):
            return False
    return True

def monster_management(array_monster):
    print('Selamat datang di database monster!')
    print('1. Tampilkan semua monster')
    print('2. Tambahkan monster baru')
    action = int(input('Pilih aksi yang ingin dilakukan: '))
    while (action != 1) and (action != 2):
        print('Aksi yang dipilih tidak ditemukan.')
        action = int(input('Pilih aksi yang ingin dilakukan: '))
    if (action == 1):
        printing_array = [['a','b','c','d','e'] for i in range (len(array_monster))]
        for i in range(len(printing_array)):
            printing_array [i] = array_monster [i]
        printing_array [0] = ['ID', 'Type', 'ATK Power', 'DEF Power', 'HP'] #header line

        #print array in form of a structured table
        max_length_per_column = [max(map(len, column)) for column in zip(*printing_array)]
        for row in printing_array:
            print(" | ".join("{:{}}".format(element, length) for element, length in zip(row, max_length_per_column)))
    
    else: #action == 2
        print('Saatnya membuat monster baru!')
        monster_type = input('Masukkan tipe atau nama: ') 
        unique_type = False
        while not(unique_type):
            i = 0   
            while (i < len(array_monster)):
                if (array_monster [i][1] == monster_type):
                    break
                i += 1
            if(i==len(array_monster)): # tidak ada yang sama, nama monster sudah unik
                break
            monster_type = input('Masukkan tipe atau nama: ') 

        monster_atk_power = input('Masukkan ATK Power: ')
        while True:
            if(is_integer(monster_atk_power)):
                monster_atk_power = int(monster_atk_power) # ubah ke int
                break
            monster_atk_power = int(input('Masukkan ATK Power: '))

        monster_def_power = input('Masukkan DEF Power (0-50): ') 
        while True:
            if(is_integer(monster_def_power)):
                if(int(monster_def_power) >= 0 and (int(monster_def_power) <= 50)):
                    monster_def_power = int(monster_def_power)
                    break
            monster_def_power = input('Masukkan DEF Power: ')

        monster_hp = input('Masukkan HP: ')
        while True: 
            if(is_integer(monster_hp)):
                monster_hp = int(monster_hp)
                break
            monster_hp = input('Masukkan HP: ')
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
            temporary_array = [(array_monster [len(array_monster) - 1][0] + 1), monster_type, int(monster_atk_power), int(monster_def_power), int(monster_hp)] 
            array_monster.append(temporary_array)
            print('Monster berhasil ditambahkan ke database!')
        else: #(confirm == 'N') or (confirm == 'n'):
            print('Monster gagal ditambahkan ke database!')
    return array_monster
