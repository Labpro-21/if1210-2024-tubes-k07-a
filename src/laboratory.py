# PROGRAM F11 - Laboratory
# Writer: Naomi Risaka Sitorus
# Tanggal: 5 Mei 2024

# KAMUS
# monster_amt, coin_amt, price, monster_id, upgrade_id, level: integer
# confirm: string

# ALGORITMA
def is_integer(user_input: str) -> bool:
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def laboratory(array_user: list, array_monster_inventory: list, array_monster: list, user_id: int) -> (list, list):
    print('Kamu telah memasuki area lab monster!')
    print('---------- MONSTERS OWNED ----------')
    monster_amt = 0
    idx = []
    for i in range (len(array_monster_inventory)):
        if (str(array_monster_inventory[i][0]) == str(user_id)):
            idx.append(i)
            monster_id = int(array_monster_inventory[i][1]) 
            print(str(monster_amt+1) + '.' + str(array_monster[monster_id][1]), '(Level :', str(array_monster_inventory[i][2]) + ')')
            monster_amt += 1
    print('-------- UPGRADE PRICE LIST --------')
    print('1. Level 1 -> Level 2: 250 OC')
    print('2. Level 2 -> Level 3: 500 OC')
    print('3. Level 3 -> Level 4: 800 OC')
    print('4. Level 4 -> Level 5: 1250 OC')
    print('')
    coin_amt = int(array_user[user_id][4])
    print('Jumlah koin yang dimliki: ', str(coin_amt)) 
    upgrade_id = input('Pilih monster yang ingin diupgrade: ')
    while True:
        if(is_integer(upgrade_id)):
            upgrade_id = int(upgrade_id) # ubah ke int
            break
        print('Monster yang ingin diupgrade tidak ditemukan.')
        upgrade_id = input('Pilih monster yang ingin diupgrade: ')
    while (upgrade_id <= 0) or (upgrade_id > monster_amt):
        print('Monster yang ingin diupgrade tidak ditemukan.')
        upgrade_id = input('Pilih monster yang ingin diupgrade: ')
        while True:
            if(is_integer(upgrade_id)):
                upgrade_id = int(upgrade_id) # ubah ke int
                break
            print('Monster yang ingin diupgrade tidak ditemukan.')
            upgrade_id = input('Pilih monster yang ingin diupgrade: ')
    level = int(array_monster_inventory[idx[upgrade_id - 1]][2])
    if (level == 5):
        print('Monster yang dipilih sudah memiliki level maksimum.')
    else:
        if (level == 1):
            price = 250
        elif (level == 2):
            price = 500
        elif (level == 3):
            price = 800
        else: #level == 4
            price = 1250
        print(str(array_monster[int(array_monster_inventory[idx[upgrade_id - 1]][1])][1]), 'akan diupdate ke level', str(level + 1))
        print('Harga upgrade ini adalah', str(price))
        confirm = input('Lanjutkan upgrade (Y/N): ')
        while (confirm != 'Y') and (confirm != 'y') and (confirm != 'N') and (confirm != 'n'):
            print('Input tidak valid!')
            confirm = input('Lanjutkan upgrade (Y/N): ')
        if (confirm == 'Y') or (confirm == 'y'):
            if (price > coin_amt):
                print('Upgrade gagal! Anda tidak memiliki cukup koin.')
            else:
                print('Upgrade berhasil!')
                level += 1 #level ditambah 1
                array_monster_inventory[idx[upgrade_id - 1]][2] = level
                coin_amt -= price #coin_amt dikurang price
                array_user[user_id][4] = coin_amt
                print(str(array_monster[(array_monster_inventory[idx[upgrade_id - 1]][1])][1]), 'sekarang ada di level', str(array_monster_inventory[idx[upgrade_id - 1]][2]) + '.')
        else: #(confirm == 'N') or (confirm == 'n')
            print('Upgrade dibatalkan.')
    return (array_monster_inventory, array_user)
