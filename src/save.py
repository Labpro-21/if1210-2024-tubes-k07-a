# PROGRAM F15 - Save
# Writer: Bertha Soliany Frandi
# Tanggal: 9 Mei 2024
# Note : line 47 masih pakai fungsi map
# KAMUS

# ALGORITMA
import os
import time # untuk time.sleep
# setiap function akan return array yang sudah dimodifikasi (karena hasil permainan)

def save(array_user: list, array_monster: list, array_monster_inventory: list, array_monster_shop: list, array_item_inventory: list, array_item_shop: list):
    folder = input("Masukkan nama folder: ")
    print()
    print("Saving...")
    time.sleep(1.5)
    print()

    # pengecekan keberadaan folder parent ./data
    parent_check = os.path.exists("./data")
    if parent_check == False:
        os.makedirs("./data")
        print("Membuat folder data...")
        time.sleep(1.5)
        
    # pengecekan nama folder pada folder parent ./data
    folder_check = os.path.exists("./data/"+folder)
    if folder_check == False:
        os.makedirs(f"./data/{folder}")
        print(f"Membuat folder data/{folder}")
        time.sleep(2)

    # overwrite data
    write_csv(f"./data/{folder}/user.csv", array_user)
    write_csv(f"./data/{folder}/monster.csv", array_monster)
    write_csv(f"./data/{folder}/item_inventory.csv", array_item_inventory)
    write_csv(f"./data/{folder}/monster_inventory.csv", array_monster_inventory)
    write_csv(f"./data/{folder}/item_shop.csv", array_item_shop)
    write_csv(f"./data/{folder}/monster_shop.csv", array_monster_shop)

    print(f"Berhasil menyimpan data di folder data/{folder}!")

# untuk overwrite data
def write_csv(path: str, data: list):
    with open(path, "w") as file: 
        for row in data:
            file.write(';'.join(map(str, row)) + '\n')
