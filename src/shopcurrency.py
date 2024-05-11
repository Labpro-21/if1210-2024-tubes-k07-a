# Program: Shop and Currency
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 11 Mei 2024
# Note: -

from monster import csv_to_array

# ALGORITMA
# baca file monster dan potion
def baca_csv(nama_file):
    return csv_to_array(nama_file)

print("<<<SHOP>>>")
print("Selamat datang di TOKO!!")

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
        longest.append(maks)

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

# menampilkan monster dan potion
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

# fungsi untuk membeli potion
def buy_potion(item_id, quantity, currency):
    item = next((p for p in item_inv if p['id'] == str(item_id)), None)

    if item:
        if item['stock'] >= quantity:
            total_price = item['price'] * quantity
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

# fungsi untuk mengecek apabila monster sudah dimiliki di inventory
def has_monster_in_inventory(monster_type):
    for m in item_inv:
        if m['type'] == monster_type and m['id'] != 0:
            return True
    return False

# fungsi untuk membeli monster
def buy_monster(item_id, quantity, currency):
    item = next((m for m in mons_shop if m['id'] == str(item_id)), None)

    if item:
        if item['stock'] >= quantity:
            if has_monster_in_inventory(item['type']):
                print(f"Anda sudah memiliki {item['type']} di inventory.")
                return currency

            total_price = item['price'] * quantity
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

# fungsi main untuk melihat, membeli, dan keluar
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
                show_id_mons()
            elif item_type.lower() == 'potion':
                show_id_pot()
            else:
                print("Invalid item type.")
        elif choice == '2':
            item_type = input("Anda ingin melihat Potion/Monster: ")
            item_id = int(input("Masukkan ID: "))
            quantity = int(input("Masukkan kuantitas: "))
            currency = buy_item(item_type, item_id, quantity, currency)
        elif choice == '3':
            print(f"Anda sudah keluar dari toko. Terima kasih sudah datang!")
            break
        else:
            print("Pilihan tidak valid. Masukkan kembali angka!")
            
main()
