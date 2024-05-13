# PROGRAM F16 - Exit
# Writer: Bertha Soliany Frandi
# Tanggal: 6 Mei 2024

# ALGORITMA
from save import save

def exit(array_user: list, array_monster: list, array_monster_inventory: list, array_item_inventory: list, array_monster_shop: list, array_item_shop: list):
    reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
    while True:
        if reassure == "iya" or reassure == "IYA" or reassure == "Iya":
            save(array_user, array_monster, array_monster_inventory, array_item_inventory, array_monster_shop, array_item_shop)
            break
        elif reassure == "tidak" or reassure == "TIDAK" or reassure == "Tidak":
            break
        else:
            print("Input tidak valid")
            reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
