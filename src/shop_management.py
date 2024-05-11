# Program: Shop management
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 11 Mei 2024
# Note: nambahin hapus update monster id nya belum ke detect

# file baru shop management
# import
import csv
# manual append
def create_shop(name):
    return {'name': name, 'items': []}

def manual_append(shop, item):
    shop['items'].append(item)

# save file
def save_data(shop):
    # Save monster data to monster.csv
    with open("monster.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'type', 'stock', 'price'])  # Write header
        for item in shop['items']:
            if item['type'] == 'monster':
                writer.writerow([item['id'], item['type'], item['stock'], item['price']])

    # Save potion data to item_inventory.csv
    with open("item_inventory.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'type', 'stock', 'price'])  # Write header
        for item in shop['items']:
            if item['type'] == 'potion':
                writer.writerow([item['id'], item['type'], item['stock'], item['price']])

    print("Data berhasil disimpan.")

# baca file
def baca_csv(nama_file):
    with open(nama_file, newline='') as file:
        reader = csv.reader(file, delimiter=';')  # Specify the delimiter as ';'
        data = list(reader)
    return data[1:]  # Exclude the header from the data

def tampilkan_border(data):
    # Mencari len terpanjang kolom id, type, atk_power, dan def_power agar tampilan rapi
    longest = []

    # Mengecek panjang elemtn setiap baris terlebih dahulu dari setiap kolom
    for i in range(len(data[0])):
        maks = 0
        for j in range(len(data)):
            if len(data[j][i]) > maks:
                maks = len(data[j][i])
        longest.append(maks)

    # Melakukan print setiap baris dengan dekorasi border
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

def display_monster():
    # Membaca data monster dari file CSV
    file_csv = "monster.csv"
    data = baca_csv(file_csv)

    # Menampilkan data monster dengan border
    tampilkan_border(data)

def display_potion():
    # Membaca data potion dari file CSV
    file_csv = "item_inventory.csv"
    data = baca_csv(file_csv)

    # Menampilkan data potion dengan border
    tampilkan_border(data)

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
    id_ = int(input("Masukkan ID monster: "))
    for item in shop['items']:
        if item['type'] == 'monster' and item['id'] == id_:
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
    id_ = int(input("Masukkan ID potion: "))
    for item in shop['items']:
        if item['type'] == 'potion' and item['id'] == id_:
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
    for i, monster in enumerate(shop.monsters):
        if monster['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus monster ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop.monsters[i]
                print(f"Monster berhasil dihapus dari toko {shop}!")
                return
            else:
                print(f"Penghapusan monster dari toko {shop} tidak jadi dilaksanakan.")
                return
    print("Monster tidak ditemukan, cek ID monster!")

def delete_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    for i, potion in enumerate(shop.potions):
        if potion['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus potion ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop.potions[i]
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
                display_monster()
            elif view_choice == '2':
                display_potion()
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
            shop.save_data()
            print("Terima kasih! Progress terakhir telah disimpan.")
            break

        else:
            print("Pilihan tidak valid, masukkan angka kembali!.")

shop = create_shop("Phineas")
shop_management(shop)