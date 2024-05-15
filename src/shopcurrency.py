# Program: Shop and Currency
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 14 Mei 2024
# Note: potionnya belum bisa ke print


def csv_to_array (path):
    lines = []
    with open(path, 'r') as file:
        for row in file:
            lines.append(row) # Mengubah csv menjadi array per baris 
    array = []
    for line in lines:
        row = []
        kata = ''
        for elmt in line:
            if elmt != ';' and elmt != '\n':
                kata += elmt
            elif elmt == ';':
                row.append(kata)
                kata = ''
        row.append(kata)
        array.append(row)
    return array

def show_list(data):
    # Mencari len terpanjang kolom id, type, atk_power, dan def_power agar tampilan rapi
    # Urutan indeks akan sesuai urutan item
    longest = []

    # Mengecek panjang elemen
    for i in range(len(data[0])-1):
        maks = 0
        for j in range(len(data)):
            if len(data[j][i]) > maks:
                maks = len(data[j][i])
        longest.append(maks)

    # Keluaran
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j != (len(data[0]) - 1):
                # Print data
                print(data[i][j], end="")
                # Print spasi
                print((longest[j] - len(data[i][j])) * " ", end="")
                # Print border
                print(" | ", end="")
            else: # kolom terakhir tidak menggunakan border
                print(data[i][j])

def display():
    # validasi aksi yang akan dilakukan
    item_type = input("Anda ingin melihat Potion/Monster: ")
    if item_type.lower() == 'monster':
        print(show_list(read_filemonster()))
    elif item_type.lower() == 'potion':
        print(show_list(read_filepotion()))
    else:
        print("Masukkan anda tidak valid. Masukkan lagi!")
        
# fungsi untuk membaca file dari monster dan dari potion
def read_filemonster():
    data_monsternew = []
    data_monstershop = csv_to_array('data/monster_shop.csv')
    data_monster = csv_to_array('data/monster.csv')
    
    data_monsternew.append (["id", "type", "atk_power", "def_power", "hp", "stok", "harga"])
    for i in range (1, len(data_monstershop)):
        for j in range (1, len(data_monster)):
            if data_monster [j][0] == data_monstershop[i][0]:
                data_monsternew.append(
                    [data_monster[j][0], data_monster[j][1], 
                     data_monster[j][2], data_monster[j][3],
                     data_monster[j][4], data_monstershop[i][1],
                     data_monstershop[i][2]])
    return data_monsternew

def read_filepotion():
    data_potionshop = csv_to_array('data/item_shop.csv')
    data_potion = csv_to_array('data/item_inventory.csv')
    
    data_potionnew = []
    data_potionnew.append (["id", "type", "stok", "harga"])   
    for i in range (1, len(data_potionshop)):
        for j in range (1, len(data_potion)):
            if data_potion [j][0] == data_potionshop[i][0]:
                data_potionnew.append(
                    [data_potion[j][0], data_potion[j][1],
                    data_potion[j][2], data_potion[j][3],
                    data_potion[j][4], data_potionshop[i][1],
                    data_potionshop[i][2]
                    ])
    return data_potionnew

def has_monsterinven():
    data_inventory = csv_to_array('data/monster_inventory.csv')
    for m in data_inventory:
        if m[0] == id:
            return True
    return False

# fungsi untuk membeli monster dan potion
def buy_monster():
    if has_monsterinven():
        True
        int(input("Anda sudah memiliki monster ini, masukkan ID lain!"))
    else:
        data_monstershop = csv_to_array("data/monster_shop.csv")
        data_monster = csv_to_array("data/monster.csv")
        data_owca = csv_to_array("data/user.csv")         

    item_id = int(input("Masukkan ID monster: "))
    quantity = int(input("Masukkan kuantitas: "))
                
    for i in range (1, len(data_monstershop)):
        id = data_monstershop [i][0]
        type = data_monster [i][1]
        atk_power = data_monster [i][2]
        def_power = data_monster [i][3]
        hp = data_monster [i][4]
        stok = data_monstershop [i][1]
        price = data_monstershop [i][2]
        owca =  data_owca[user_id][4]
    
        if item_id == id:
            owca = int(owca)
            price = int(price)
            if owca >= price:
                print(f"kamu berhasil membeli {type}")
                print(f"Sisa O.W.C.A kamu {owca-price}")
                owca = owca - price
                data_owca[user_id][4] = owca
            elif owca < price:
                print("O.W.C.A kamu kurang")
                
def buy_potion():
    data_potionshop = csv_to_array("data/item_inventory.csv")
    data_potion = csv_to_array("data/item_shop.csv")
    data_owca = csv_to_array("data/user.csv")         
    
    item_id = int(input("Masukkan ID potion: "))
    quantity = int(input("Masukkan kuantitas: "))
    for j in range (1, len(read_filepotion)):
        id_1 = j
        type_1 = data_potion[j][0]
        stok_1 = data_potion[j][1]
        harga_1 = data_potion[j][2]
    if item_id == id_1:
        owca = int(owca)
        harga_1 = int(harga_1)
        jumlah = quantity * harga_1
        if owca >= harga_1:
            print(f"kamu berhasil membeli {type_1}")
            print(f"Sisa O.W.C.A kamu {owca-jumlah}")
            owca = owca - jumlah
            data_owca[user_id][4] = owca
        elif owca < harga_1:
            print("O.W.C.A kamu kurang")

# cek dulu user ke berapa untuk mengetahui currency nya 
user_id = int(input("Masukkan user id anda: "))

# contoh penggunaan dan tampilan akan seperti apa
def main():
    currency = 0
        
    # pilihan aksi
    while True:
        print("SHOP MENU:")
        print("1. Lihat")
        print("2. Beli")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        if choice == '1':
            display()
        elif choice == '2':
            item_type = input("Anda ingin membeli Potion/Monster: ")
            # validasi aksi yang akan dilakukan
            if item_type.lower() == 'monster':
                buy_monster()
            elif item_type.lower() == 'potion':
                buy_potion()
            else:
                print("Pilihan tidak valid. Silakan masukkan kembali!")
        elif choice == '3':
            print(f"Anda sudah keluar dari toko. Terima kasih sudah datang!")
            break
        else:
            print("Pilihan tidak valid. Masukkan kembali!")
            
            
main()
            
