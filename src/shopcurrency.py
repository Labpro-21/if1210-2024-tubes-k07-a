# Program: Shop and Currency
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 14 Mei 2024
# Note: -

# array
monsters = [
    { 'id': 1, 'type': "Pikachow", 'atk_power': 125, 'def_power': 10, 'hp': 600, 'stok': 10, 'harga': 500 },
    { 'id': 2, 'type': "Bulbu", 'atk_power': 50, 'def_power': 50, 'hp': 1200, 'stok': 4, 'harga': 700 },
    { 'id': 3, 'type': "Zeze", 'atk_power': 300, 'def_power': 10, 'hp': 100, 'stok': 3, 'harga': 1000 },
    { 'id': 4, 'type': "Zuko", 'atk_power': 100, 'def_power': 25, 'hp': 800, 'stok': 8, 'harga': 550 },
    { 'id': 5, 'type': "Chacha", 'atk_power': 80, 'def_power': 30, 'hp': 700, 'stok': 8, 'harga': 550 },
    { 'id': 6, 'type': "Sukuna", 'atk_power': 650, 'def_power': 30, 'hp': 1000, 'stok': 0, 'harga': 0 }
]

item_inventory = [
    { 'id': 2, 'type': "Bulbu" },
    { 'id': 1, 'type': "Pikachow" }, 
    { 'id': 0, 'type': "empty" }, 
]

potions = [
    { 'id': 1, 'type': "strength", 'stok': 5, 'harga': 10 },
    { 'id': 2, 'type': "resilience", 'stok': 3, 'harga': 5 },
    { 'id': 3, 'type': "resilience", 'stok': 7, 'harga': 3 },
    { 'id': 4, 'type': "healing", 'stok': 3, 'harga': 0 },
    { 'id': 5, 'type': "strength", 'stok': 20, 'harga': 0 } 
]            

currency = 1500
# ALGORITMA
print("<<<SHOP>>>")
print("Selamat datang di TOKO!!")

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

# Fungsi untuk membeli potion
def buy_potion(item_id, quantity, currency, potions_shop):
    item = next((p for p in potions_shop if p['id'] == str(item_id)), None)

    if item:
        if item['stok'] >= quantity:
            total_price = item['harga'] * quantity
            if currency >= total_price:
                currency -= total_price
                item['stok'] -= quantity
                print(f"Anda berhasil membeli {quantity} {item['type']} dengan harga {total_price}. Sisa currency anda: {currency}")
            else:
                print("Currency anda tidak cukup.")
        else:
            print("Stok tidak mencukupi.")
    else:
        print("Item tidak ditemukan.")

    return currency

# Fungsi untuk memeriksa apakah monster sudah ada di inventory
def has_monster_in_inventory(monster_type, item_inv):
    for m in item_inv:
        if m['type'] == monster_type and m['id'] != 0:
            return True
    return False

# Fungsi untuk membeli monster
def buy_monster(item_id, quantity, currency, item_inv, monster_shop):
    item = next((m for m in monster_shop if m['id'] == str(item_id)), None)

    if item:
        if item['stock'] >= quantity:
            if has_monster_in_inventory(item['type'], item_inv):
                print(f"Anda sudah memiliki {item['type']} di inventory.")
                return currency

            total_price = item['harga'] * quantity
            if currency >= total_price:
                currency -= total_price
                item['stock'] -= quantity
                print(f"Anda berhasil membeli {quantity} {item['type']} dengan harga {total_price}. Sisa currency anda: {currency}")
            else:
                print("Currency anda tidak cukup.")
        else:
            print("Stok tidak mencukupi.")
    else:
        print("Item tidak ditemukan.")

    return currency

# Fungsi main untuk melihat, membeli, dan keluar
def main():
    currency = 0

    while True:
        print("SHOP MENU:")
        print("1. Lihat")
        print("2. Beli")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        if choice == '1':
            item_type = input("Anda ingin melihat Potion/Monster: ")
            if item_type.lower() == 'monster':
                show_monster_list(monsters)
            elif item_type.lower() == 'potion':
                show_potion_list(potions)
            else:
                print("Invalid item type.")
        elif choice == '2':
            item_type = input("Anda ingin membeli Potion/Monster: ")
    
            if item_type.lower() == 'monster':
                item_id = int(input("Masukkan ID monster: "))
                quantity = int(input("Masukkan kuantitas: "))
                currency = buy_monster(item_id, quantity, currency, item_inventory, monster_shop)
            elif item_type.lower() == 'potion':
                item_id = int(input("Masukkan ID potion: "))
                quantity = int(input("Masukkan kuantitas: "))
                currency = buy_potion(item_id, quantity, currency, potions_shop)
            else:
                print("Pilihan tidak valid. Silakan masukkan kembali!")
        elif choice == '3':
            print(f"Anda sudah keluar dari toko. Terima kasih sudah datang!")
            break
        else:
            print("Pilihan tidak valid. Masukkan kembali!")
            
main()
