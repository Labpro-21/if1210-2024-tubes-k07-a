# PROGRAM F14 - Load
# Writer: Bertha Soliany Frandi
# Tanggal: 10 Mei 2024

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
    
    from load import csv_to_array
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

    # inisialisasi
    logged_in = False
    username = ''
    # meminta perintah berikutnya
    print('Ketik "HELP" untuk melihat menu')
    perintah = input(">>> ")
    while True:
        if logged_in == False:
            if perintah == "HELP" or perintah == "MENU":
                import menu_help
            elif perintah == "REGISTER":
                import register
            elif perintah == "LOGIN":
                import login
            elif perintah == "SAVE":
                import save
            elif perintah == "EXIT":
                import exit
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
                    import menu_help
                elif perintah == "REGISTER":
                    import register
                elif perintah == "LOGIN":
                    import login
                elif perintah == "SHOP MANAGEMENT": 
                    import shop_management
                elif perintah == "MONSTER MANAGEMENT":
                    import monster_management
                elif perintah == "SAVE":
                    import save
                elif perintah == "EXIT":
                    import exit
                    break
                else:
                    print("Perintah tidak valid!")
            elif role == "agent":
                if perintah == "REGISTER":
                    import register
                elif perintah == "LOGIN":
                    import login
                elif perintah == "LOGOUT":
                    import logout
                elif perintah == "HELP" or perintah == "MENU":
                    import menu_help
                elif perintah == "INVENTORY":
                    import inventory
                elif perintah == "BATTLE":
                    import battle
                elif perintah == "ARENA":
                    import arena
                elif perintah == "SHOP":
                    import shop
                elif perintah == "LABORATORY":
                    import laboratory
                elif perintah == "SAVE":
                    import save
                elif perintah == "EXIT":
                    import exit
                    break
                else:
                    print("Perintah tidak valid!")
        perintah = input(">>> ")
            

# keluar dari program jika nama folder tidak ditemukan
elif check_folder == False:
    print('Folder "'+args.folder+'" tidak ditemukan')
