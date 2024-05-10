# PROGRAM F11 - Laboratory
# Writer: Naomi Risaka Sitorus
# Tanggal: 5 Mei 2024

# KAMUS
# monster_amt, coin_amt, price, monster_id, upgrade_id, level: integer
# confirm: string

# ALGORITMA
def laboratory(array_user, array_monster_inventory, user_id):
    print('Kamu telah memasuki area lab monster!')
    print('---------- MONSTERS OWNED ----------')
    monster_amt = 0
    for i in range (len(array_monster_inventory)):
        if (array_monster_inventory[i][0] == user_id):
            monster_id = array_monster_inventory[i][1] - 1
            print((i+1) + '.' + array_monster_inventory[monster_id][1], '(Level :', array_monster_inventory[i][2] + ')')
            monster_amt += 1
    print('-------- UPGRADE PRICE LIST --------')
    print('1. Level 1 -> Level 2: 250 OC')
    print('2. Level 2 -> Level 3: 500 OC')
    print('3. Level 3 -> Level 4: 800 OC')
    print('4. Level 4 -> Level 5: 1250 OC')
    print('')
    coin_amt = array_user[user_id][4]
    print('Jumlah koin yang dimliki: ', coin_amt) 
    upgrade_id = int(input('Pilih monster yang ingin diupgrade: ')) 
    if (upgrade_id <= 0) or (upgrade_id > monster_amt):
        print('Monster yang ingin diupgrade tidak ditemukan.')
    else:
        level = array_monster_inventory[upgrade_id - 1][2]
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
            print((array_monster_inventory[upgrade_id - 1][1]), 'akan diupdate ke level', (level + 1))
            print('Harga upgrade ini adalah', price)
            confirm = input('Lanjutkan upgrade (Y/N): ')
            while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
                print('Input tidak valid!')
                confirm = input('Lanjutkan upgrade (Y/N): ')
            if (confirm == 'Y') or (confirm == 'y'):
                if (price > coin_amt):
                    print('Upgrade gagal! Anda tidak memiliki cukup koin.')
                else:
                    print('Upgrade berhasil!')
                    array_monster_inventory[upgrade_id - 1][2] += 1 #level ditambah 1
                    array_user[user_id][4] -= price #coin_amt dikurang price
                    print((array_monster_inventory[upgrade_id - 1][1]), 'sekarang ada di level', array_monster_inventory[upgrade_id - 1][2] + '.')
            else: #(confirm == 'N') or (confirm == 'n')
                print('Upgrade dibatalkan.')
    return (array_monster_inventory, array_user)
