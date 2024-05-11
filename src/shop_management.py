# Program: Shop management
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 11 Mei 2024
# Note: -

# ALGORITMA
# import
from monster import csv_to_array

# manual append
def create_shop(name):
    return {'name': name, 'items': []}

def manual_append(shop, item):
    shop['items'].append(item)

# baca file
def baca_csv(nama_file):
    return csv_to_array(nama_file)

print("<<<SHOP MANAGEMENT>>>")
print("Selamat datang di TOKO!!")

baca_csv("item_inventory.csv")
baca_csv("item_shop.csv")
baca_csv("monster_shop.csv")
baca_csv("monster.csv")

item_Shop = baca_csv("item_shop.csv")
mons = baca_csv("monster.csv")
item_inv = baca_csv("item_inventory.csv")
mons_shop = baca_csv("monster_shop.csv")

x = 0

def tampilkan_border(data):
    # Mencari len terpanjang kolom id, type, atk_power, dan def_power agar tampilan rapi
    longest = []

    # Mengecek panjang elemtn setiap baris terlebih dahulu dari setiap kolom
    for i in range(len(data[0])):
        maks = 0
        for j in range(len(data)):
            if len(str(data[j][i])) > maks:
                maks = len(str(data[j][i]))
        longest.manual_append(maks)

    # Melakukan print setiap baris dengan dekorasi border
    for i in range(len(data)):
        for j in range(len(data[0])):
            if j != (len(data[0]) - 1):
                # Print data
                print(data[i][j], end="")
                # Print spasi
                print((longest[j] - len(str(data[i][j]))) * " ", end="")
                # Print border
                print(" | ", end="")
            else: # kolom terakhir tidak menggunakan border
                print(data[i][j])

def show_id_mons():
    print("ID | Type          | ATK Power | DEF Power | HP   | Stok | Harga")
    for i in range(len(mons)):
        id = mons[i][0]
        type = mons[i][1]
        atk = mons[i][2]
        defence = mons[i][3]
        hp = mons[i][4]
        stok = mons_shop[i][1]
        price = mons_shop[i][2]
        print(f"{id}  | {type}          | {atk}        | {defence}      | {hp}   | {stok}    | {price}")
        
def show_id_pot():
    print("ID | Type          | Stok | Harga")
    for j in range (1, len(item_Shop)):
        id_1 = j
        type_1 = item_Shop[j][0]
        stok_1 = item_Shop[j][1]
        harga_1 = item_Shop[j][2]
        print(f"{id_1} |{type_1} potion         |{stok_1}   |{harga_1}")

# function untuk menambah, update, menghapus
def add_monster(shop):
    id_ = int(input("Masukkan ID monster: "))
    stock = int(input("Masukkan stok monster: "))
    price = int(input("Masukkan harga monster: "))
    monster = {'id': id_, 'type': 'monster', 'atk_power': 0, 'def_power': 0, 'hp': 0, 'stock': stock, 'price': price}
    manual_append(shop, monster)
    print(f"Monster baru berhasil ditambahkan ke toko {shop}!")

def add_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    stock = int(input("Masukkan stok potion: "))
    price = int(input("Masukkan harga potion: "))
    potion = {'id': id_, 'type': 'potion', 'stock': stock, 'price': price}
    manual_append(shop, potion)
    print(f"Potion baru berhasil ditambahkan ke toko {shop}!")

def update_monster(shop):
    id_ = input("Masukkan ID monster: ")
    file_csv = show_id_mons()
    data = baca_csv(file_csv)
    print("Data:", data)
    for item in data:
        if item['type'] == 'monster' and str(item['id']) == id_:
            stock = input("Masukkan stok baru dari monster (tekan enter apabila tidak ingin diubah): ")
            if stock:
                item['stock'] = int(stock)
            price = input("Masukkan harga baru dari monster (tekan enter apabila tidak ingin diubah): ")
            if price:
                item['price'] = int(price)
            print(f"Monster dengan ID {id_} di toko {shop['name']} berhasil diperbaharui!")
            return
    print("Monster tidak ditemukan, cek ID monster!")

def update_potion(shop):
    id_ = input("Masukkan ID potion: ")
    file_csv = show_id_pot()
    data = baca_csv(file_csv)
    print("Data:", data)
    for item in data:
        if item['type'] == 'potion' and str(item['id']) == id_:
            stock = input("Masukkan stok baru dari potion (tekan enter apabila tidak ingin diubah): ")
            if stock:
                item['stock'] = int(stock)
            price = input("Masukkan harga baru dari potion (tekan enter apabila tidak ingin diubah): ")
            if price:
                item['price'] = int(price)
            print(f"Potion dengan ID {id_} di toko {shop['name']} berhasil diperbaharui!")
            return
    print("Potion tidak ditemukan, cek ID potion!")


def delete_monster(shop):
    id_ = int(input("Masukkan ID monster: "))
    for i, monster in enumerate(shop['items']):
        if monster['type'] == 'monster' and monster['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus monster ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop['items'][i]
                print(f"Monster berhasil dihapus dari toko {shop}!")
                return
            else:
                print(f"Penghapusan monster dari toko {shop} tidak jadi dilaksanakan.")
                return
    print("Monster tidak ditemukan, cek ID monster!")

def delete_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    for i, potion in enumerate(shop['items']):
        if potion['type'] == 'potion' and potion['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus potion ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop['items'][i]
                print(f"Potion berhasil dihapus dari toko {shop}!")
                return
            else:
                print(f"Penghapusan potion dari toko {shop} tidak jadi dilaksanakan.")
                return
    print("Potion tidak ditemukan, cek ID potion!")
    
# tampilan yang akan keluar
def shop_management(shop):
    while True:
        print("Shop Management System (Admin)")
        print("1. Lihat")
        print("2. Tambah")
        print("3. Update")
        print("4. Hapus")
        print("5. Keluar")
        choice = input("Masukkan pilihan anda: ")

        if choice == '1':
            print("Apa yang ingin anda lihat?")
            print("1. Monster")
            print("2. Potion")
            view_choice = input("Masukkan pilihan angka anda: ")
            if view_choice == '1':
                show_id_mons()
            elif view_choice == '2':
                show_id_pot()
            else:
                print("Pilihan tidak valid, masukkan angka kembali!")

        elif choice == '2':
            print("Komponen apa yang ingin anda tambahkan?")
            print("1. Monster")
            print("2. Potion")
            add_choice = input("Masukkan pilihan angka anda: ")
            if add_choice == '1':
                add_monster(shop)
            elif add_choice == '2':
                add_potion(shop)

        elif choice == '3':
            print("Komponen apa yang ingin anda perbaharui?")
            print("1. Monster")
            print("2. Potion")
            update_choice = input("Masukkan pilihan angka anda: ")
            if update_choice == '1':
                update_monster(shop)
            elif update_choice == '2':
                update_potion(shop)

        elif choice == '4':
            print("Komponen apa yang ingin anda hapus?")
            print("1. Monster")
            print("2. Potion")
            delete_choice = input("Masukkan pilihan angka anda: ")
            if delete_choice == '1':
                delete_monster(shop)
            elif delete_choice == '2':
                delete_potion(shop)

        elif choice == '5':
            print(f"Anda sudah keluar dari toko {shop}. Terima kasih!")
            print("Terima kasih! Progress terakhir telah disimpan.")
            break

        else:
            print("Pilihan tidak valid, masukkan angka kembali!.")

shop = create_shop("Phineas")
shop_management(shop)
