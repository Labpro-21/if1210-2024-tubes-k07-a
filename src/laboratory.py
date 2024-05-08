# PROGRAM F11 - Laboratory
# Writer: Naomi Risaka Sitorus
# Tanggal: 5 Mei 2024

# KAMUS
# monster_amt: integer
# coin_amt : integer 
# price : integer
# monster_id : integer
# upgrade_id : integer 
# level: integer

# ALGORITMA
import login
from monster import csv_to_array

def laboratory(array, user_id):
    print('Kamu telah memasuki area lab monster!')
    print('---------- MONSTERS OWNED ----------')
    inventory_array = csv_to_array (r"E:\NAOMI\University\Sem 2\Programming Fundamentals\Tubes\monster_inventory.csv")
    monster_array = csv_to_array (r"E:\NAOMI\University\Sem 2\Programming Fundamentals\Tubes\monster.csv")
    monster_amt = 0
    for i in range (len(inventory_array)):
        if (inventory_array[i][0] == user_id):
            monster_id = inventory_array[i][1] - 1
            print((i+1) + '.' + monster_array[monster_id][1], '(Level :', inventory_array[i][2] + ')')
            monster_amt += 1
    print('-------- UPGRADE PRICE LIST --------')
    print('1. Level 1 -> Level 2: 250 OC')
    print('2. Level 2 -> Level 3: 500 OC')
    print('3. Level 3 -> Level 4: 800 OC')
    print('4. Level 4 -> Level 5: 1250 OC')
    print('')
    coin_amt = array[user_id][4]
    print('Jumlah koin yang dimliki: ', coin_amt) 
    upgrade_id = int(input('Pilih monster yang ingin diupgrade: ')) 
    if (upgrade_id <= 0) or (upgrade_id > monster_amt):
        print('Monster yang ingin diupgrade tidak ditemukan.')
    else:
        level = inventory_array[upgrade_id - 1][2]
        if (level == 5):
            print('Monster yang dipilih sudah memiliki level maksimum.')
        else:
            if (level + 1 == 2):
                price = 250
            if (level + 1 == 3):
                price = 500
            if (level + 1 == 4):
                price = 800
            else: #level + 1 == 5
                price = 1250
            print((inventory_array[upgrade_id - 1][1]), 'akan diupdate ke level', (level + 1))
            print('Harga upgrade ini adalah', price)
            if (price > coin_amt):
                print('Upgrade gagal! Anda tidak memiliki cukup koin.')
            else:
                print('Upgrade berhasil!')
                inventory_array[upgrade_id - 1][2] += 1 #level ditambah 1
                array[user_id][4] -= price #coin_amt dikurang price
                print((inventory_array[upgrade_id - 1][1]), 'sekarang ada di level', inventory_array[upgrade_id - 1][2] + '.')

laboratory(array, user_id)