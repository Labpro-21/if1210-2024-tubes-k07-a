# PROGRAM F14 - Load
# Writer: Bertha Soliany Frandi
# Tanggal: 10 Mei 2024

# Note : Belum ada pengecekan ketika user tidak memberikan nama folder (Masih )
import argparse
parser = argparse.ArgumentParser(description="load data dari folder yang dipilih")
parser.add_argument("folder", help="nama folder yang berisi data yang ingin di load")
args = parser.parse_args()
folder_path = "./data/"+args.folder

# mengecek apakah folder ada
import os
check_folder = os.path.exists(folder_path)
if check_folder == True:
    print("Loading...")
    
    from src.load import csv_to_array
    array_user = csv_to_array(folder_path+"/user.csv")
    array_monster = csv_to_array(folder_path+"/monster.csv")
    array_monster_inventory = csv_to_array(folder_path+"/monster_inventory.csv")
    array_monster_shop = csv_to_array(folder_path+"/monster_shop.csv")
    array_item_inventory = csv_to_array(folder_path+"/item_inventory.csv")
    array_item_shop = csv_to_array(folder_path+"/item_shop.csv")

    import time
    time.sleep(2)

    print("Selamat datang di program OWCA!")
    time.sleep(1)
    print()

    from src.menu_help import *
    from src.register import *
    # from src.login import *
    # from src.save import *
    # from src.exit import *
    # from src.shop_management import *
    # from src.monster_management import *
    # from src.inventory import *
    # from src.battle import *
    # from src.arena import *
    # from src.shopcurrency import *
    # from src.laboratory import *
    # inisialisasi
    logged_in = False
    username = ''
    role = ''
    # meminta perintah berikutnya
    print('Ketik "HELP" untuk melihat menu')
    perintah = input(">>> ")
    while True:
        if logged_in == False:
            if perintah == "HELP" or perintah == "MENU":
                help(logged_in,role,username)
            elif perintah == "REGISTER":   
                array_monster_inventory = register(logged_in,array_user, array_monster, array_monster_inventory)
            elif perintah == "LOGIN":
                pass
            elif perintah == "SAVE":
                pass
            elif perintah == "EXIT":
                pass
                break
            else:
                print("perintah tidak valid!")
        elif logged_in == True:
            # mendapatkan role user yang sedang login
            for i in range(5):
                if username == array_user[i][1]:
                    role = array_user[i][3]
            if role == "admin":
                if perintah == "HELP" or perintah == "MENU":
                    help(logged_in,role,username)
                elif perintah == "REGISTER":
                    register(logged_in,array_user, array_monster, array_monster_inventory)
                elif perintah == "LOGIN":
                    pass
                elif perintah == "SHOP MANAGEMENT": 
                    pass
                elif perintah == "MONSTER MANAGEMENT":
                    pass
                elif perintah == "SAVE":
                    pass
                elif perintah == "EXIT":
                    pass
                    break
                else:
                    print("Perintah tidak valid!")
            elif role == "agent":
                if perintah == "REGISTER":
                    register(logged_in,array_user, array_monster, array_monster_inventory)
                elif perintah == "LOGIN":
                    pass
                elif perintah == "LOGOUT":
                    pass
                elif perintah == "HELP" or perintah == "MENU":
                    help(logged_in,role,username)
                elif perintah == "INVENTORY":
                    pass
                elif perintah == "BATTLE":
                    pass
                elif perintah == "ARENA":
                    pass
                elif perintah == "SHOP":
                    pass
                elif perintah == "LABORATORY":
                    pass
                elif perintah == "SAVE":
                    pass
                elif perintah == "EXIT":
                    pass
                    break
                else:
                    print("Perintah tidak valid!")
        perintah = input(">>> ")
            

# keluar dari program jika nama folder tidak ditemukan
elif check_folder == False:
    print('Folder "'+args.folder+'" tidak ditemukan')
