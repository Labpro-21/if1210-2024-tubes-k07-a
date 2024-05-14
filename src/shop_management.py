# Program: Shop management
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 14 Mei 2024
# Note: 

monsters = [
    { 'id': 1, 'type': "Pikachow", 'atk_power': 125, 'def_power': 10, 'hp': 600, 'stok': 10, 'harga': 500 },
    { 'id': 2, 'type': "Bulbu", 'atk_power': 50, 'def_power': 50, 'hp': 1200, 'stok': 4, 'harga': 700 },
    { 'id': 3, 'type': "Zeze", 'atk_power': 300, 'def_power': 10, 'hp': 100, 'stok': 3, 'harga': 1000 },
    { 'id': 4, 'type': "Zuko", 'atk_power': 100, 'def_power': 25, 'hp': 800, 'stok': 8, 'harga': 550 },
    { 'id': 5, 'type': "Chacha", 'atk_power': 80, 'def_power': 30, 'hp': 700, 'stok': 8, 'harga': 550 },
    { 'id': 6, 'type': "Sukuna", 'atk_power': 650, 'def_power': 30, 'hp': 1000, 'stok': 0, 'harga': 0 }
]


potions = [
    { 'id': 1, 'type': "strength", 'stok': 5, 'harga': 10 },
    { 'id': 2, 'type': "resilience", 'stok': 3, 'harga': 5 },
    { 'id': 3, 'type': "resilience", 'stok': 7, 'harga': 3 },
    { 'id': 4, 'type': "healing", 'stok': 3, 'harga': 0 },
    { 'id': 5, 'type': "strength", 'stok': 20, 'harga': 0 } 
]            

def create_shop(name):
    return {'name': name, 'items': []}

# PILIHAN PERTAMA UNTUK MELIHAT MONSTER
def show_monster_list(monster_list):
    # Print the header
    print(f"{'ID':<5} {'Type':<10} {'Attack':<8} {'Defense':<8} {'HP':<5} {'Stok':<5} {'Harga':<5}")
    print("="*60)
    
    # Print each monster's details
    for monster in monster_list:
        print(f"{monster['id']:<5} {monster['type']:<10} {monster['atk_power']:<8} {monster['def_power']:<8} {monster['hp']:<5} {monster['stok']:<5} {monster['harga']:<5}")

def show_potion_list(potion_list):
    # Print the header
    print(f"{'ID':<5} {'Type':<12} {'Stok':<5} {'Harga':<5}")
    print("="*30)
    
    # Print each potion's details
    for potion in potion_list:
        harga = potion['harga'] if potion['harga'] is not None else 0
        print(f"{potion['id']:<5} {potion['type']:<12} {potion['stok']:<5} {harga:<5}")
        
# Fungsi untuk menambahkan monster baru
def add_monster(shop):
    id_ = int(input("Masukkan ID monster: "))
    
    # Validasi ID
    for monster in shop:
        if monster['id'] == id_:
            print("ID yang dimasukkan sudah ada, mohon masukkan ID yang lain.")
            return
    
    type_ = input("Masukkan tipe monster: ")
    atk_power = int(input("Masukkan kekuatan serangan monster: "))
    def_power = int(input("Masukkan kekuatan pertahanan monster: "))
    hp = int(input("Masukkan HP monster: "))
    stok = int(input("Masukkan stok monster: "))
    harga = int(input("Masukkan harga monster: "))

    monster = {
        'id': id_,
        'type': type_,
        'atk_power': atk_power,
        'def_power': def_power,
        'hp': hp,
        'stok': stok,
        'harga': harga
    }

    shop.append(monster)
    print("Monster baru berhasil ditambahkan ke toko!")

# Fungsi untuk menambahkan potion baru
def add_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    
    # Validasi ID
    for potion in shop:
        if potion['id'] == id_:
            print("ID yang dimasukkan sudah ada, mohon masukkan ID yang lain.")
            return
    
    type_ = input("Masukkan tipe potion: ")
    stok = int(input("Masukkan stok potion: "))
    harga = int(input("Masukkan harga potion: "))

    potion = {
        'id': id_,
        'type': type_,
        'stok': stok,
        'harga': harga
    }

    shop.append(potion)
    print("Potion baru berhasil ditambahkan ke toko!")

# Fungsi untuk memperbarui informasi monster
def update_monster(shop):
    id_ = int(input("Masukkan ID monster: "))
    for item in shop:
        if item['id'] == id_:
            stok = input("Masukkan stok baru dari monster (tekan enter apabila tidak ingin diubah): ")
            if stok:
                item['stok'] = int(stok)
            harga = input("Masukkan harga baru dari monster (tekan enter apabila tidak ingin diubah): ")
            if harga:
                item['harga'] = int(harga)
            print(f"Monster dengan ID {id_} berhasil diperbaharui!")
            return
    print("Monster tidak ditemukan, cek ID monster!")

# Fungsi untuk memperbarui informasi potion
def update_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    for item in shop:
        if item['id'] == id_:
            stok = input("Masukkan stok baru dari potion (tekan enter apabila tidak ingin diubah): ")
            if stok:
                item['stok'] = int(stok)
            harga = input("Masukkan harga baru dari potion (tekan enter apabila tidak ingin diubah): ")
            if harga:
                item['harga'] = int(harga)
            print(f"Potion dengan ID {id_} berhasil diperbaharui!")
            return
    print("Potion tidak ditemukan, cek ID potion!")

# Fungsi untuk menghapus monster
def delete_monster(shop):
    id_ = int(input("Masukkan ID monster: "))
    for i, monster in enumerate(shop):
        if monster['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus monster ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop[i]
                print(f"Monster berhasil dihapus!")
                return
            else:
                print("Penghapusan monster tidak jadi dilaksanakan.")
                return
    print("Monster tidak ditemukan, cek ID monster!")

# Fungsi untuk menghapus potion
def delete_potion(shop):
    id_ = int(input("Masukkan ID potion: "))
    for i, potion in enumerate(shop):
        if potion['id'] == id_:
            re_ask = input("Apakah anda yakin ingin menghapus potion ini? (iya/tidak): ")
            if re_ask.lower() == 'iya':
                del shop[i]
                print(f"Potion berhasil dihapus!")
                return
            else:
                print("Penghapusan potion tidak jadi dilaksanakan.")
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
                show_monster_list(monsters)
            elif view_choice == '2':
                show_potion_list(potions)
            else:
                print("Pilihan tidak valid, masukkan angka kembali!")

        elif choice == '2':
            print("Komponen apa yang ingin anda tambahkan?")
            print("1. Monster")
            print("2. Potion")
            add_choice = input("Masukkan pilihan angka anda: ")
            if add_choice == '1':
                add_monster(monsters)
            elif add_choice == '2':
                add_potion(potions)

        elif choice == '3':
            print("Komponen apa yang ingin anda perbaharui?")
            print("1. Monster")
            print("2. Potion")
            update_choice = input("Masukkan pilihan angka anda: ")
            if update_choice == '1':
                update_monster(monsters)
            elif update_choice == '2':
                update_potion(potions)

        elif choice == '4':
            print("Komponen apa yang ingin anda hapus?")
            print("1. Monster")
            print("2. Potion")
            delete_choice = input("Masukkan pilihan angka anda: ")
            if delete_choice == '1':
                delete_monster(monsters)
            elif delete_choice == '2':
                delete_potion(potions)

        elif choice == '5':
            print(f"Anda sudah keluar dari toko {shop}. Terima kasih!")
            print("Terima kasih! Progress terakhir telah disimpan.")
            break

        else:
            print("Pilihan tidak valid, masukkan angka kembali!.")

shop = create_shop("Phineas")
shop_management(shop)
