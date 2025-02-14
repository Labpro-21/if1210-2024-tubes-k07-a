# ALGORITMA
import os
import sys
import time
import argparse
from src.load import csv_to_array
from src.menu_help import *
from src.register import *
from src.login import *
from src.logout import *
from src.save import *
from src.exit import *
from src.shop_management import *
from src.monster_management import *
from src.inventory import *
from src.battle import *
from src.arena import *
from src.shop_currency import *
from src.laboratory import *

parser = argparse.ArgumentParser(description="load data dari folder yang dipilih")
parser.add_argument("folder", nargs='?', help="nama folder yang berisi data yang ingin di load")
args = parser.parse_args()

# mengeluarkan error message jika nama folder tidak diberikan
if not args.folder:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage : python main.py <nama_folder>")
    sys.exit()
else:
    folder_path = "./data/"+args.folder
    # mengecek apakah folder ada
    check_folder = os.path.exists(folder_path)
    if check_folder == True:
        print("Loading...")
        
        array_user = csv_to_array(folder_path+"/user.csv")
        array_monster = csv_to_array(folder_path+"/monster.csv")
        array_monster_inventory = csv_to_array(folder_path+"/monster_inventory.csv")
        array_monster_shop = csv_to_array(folder_path+"/monster_shop.csv")
        array_item_inventory = csv_to_array(folder_path+"/item_inventory.csv")
        array_item_shop = csv_to_array(folder_path+"/item_shop.csv")
    
        time.sleep(2)
    
        print("Selamat datang di program OWCA!")
        time.sleep(1)
        print()
    
        # inisialisasi
        logged_in = False
        username = ''
        role = ''
        user_id = 0
        # meminta perintah berikutnya
        print('Masukkan perintah!\nKetik "HELP" untuk melihat menu')
        perintah = input(">>> ").upper()
        print()
        while True:
            if logged_in == False:
                if perintah == "HELP" or perintah == "MENU":
                    help(logged_in,role,username)
                elif perintah == "REGISTER":   
                    register(logged_in,array_user, array_monster, array_monster_inventory)
                elif perintah == "LOGIN":
                    logged_in, user_id = login(logged_in,user_id,array_user)
                elif perintah == "LOGOUT":
                    logged_in = logout(logged_in)
                elif perintah == "SAVE":
                    save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                elif perintah == "EXIT":
                    keluar = exit()
                    if keluar == True:
                        save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                        print("Sampai jumpa kembali!")
                    elif keluar == False:
                        print("Sampai jumpa kembali!")
                    break
                else:
                    print("Perintah tidak valid! Pastikan input sudah benar.")
            elif logged_in == True:
                # mendapatkan role user yang sedang login
                username = array_user[user_id][1]
                role = array_user[user_id][3]
                if role == "admin":
                    if perintah == "HELP" or perintah == "MENU":
                        help(logged_in,role,username)
                    elif perintah == "REGISTER":
                        register(logged_in,array_user, array_monster, array_monster_inventory)
                    elif perintah == "LOGIN":
                        logged_in, user_id = login(logged_in,user_id,array_user)
                    elif perintah == "LOGOUT":
                        logged_in = logout(logged_in)
                    elif perintah == "SHOP MANAGEMENT": 
                        array_monster_shop, array_item_shop = shop_management(array_monster_shop, array_monster, array_item_shop)
                    elif perintah == "MONSTER MANAGEMENT":
                        array_monster = monster_management(array_monster)
                    elif perintah == "SAVE":
                        save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                    elif perintah == "EXIT":
                        keluar = exit()
                        if keluar == True:
                            save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                            print("Sampai jumpa kembali admin!")
                        elif keluar == False:
                            print("Sampai jumpa kembali admin!")
                        break
                    else:
                        print("Perintah tidak valid!")
                elif role == "agent":
                    if perintah == "REGISTER":
                        register(logged_in,array_user, array_monster, array_monster_inventory)
                    elif perintah == "LOGIN":
                        logged_in, user_id = login(logged_in,user_id,array_user)
                    elif perintah == "LOGOUT":
                        logged_in = logout(logged_in)
                    elif perintah == "HELP" or perintah == "MENU":
                        help(logged_in,role,username)
                    elif perintah == "INVENTORY":
                        inventory(array_user[user_id], array_item_inventory, array_monster_inventory, array_monster)
                    elif perintah == "BATTLE":
                        array_user[user_id] = battlemain(array_monster, array_monster_inventory, array_item_inventory, user_id, 1, False, 0 ,[], array_user)
                    elif perintah == "ARENA":
                        oc_received = arena(array_monster, array_monster_inventory, array_item_inventory, user_id, 1)
                        oc_received += int(array_user[user_id][4])
                        array_user[user_id][4] = str(oc_received)
                    elif perintah == "SHOP":
                        array_monster_shop, array_item_shop, array_monster_inventory, array_item_inventory, array_user = shopmain(array_monster_shop, array_monster, array_item_shop, array_monster_inventory, array_item_inventory, array_user, user_id)
                    elif perintah == "LABORATORY":
                        array_monster_inventory, array_user = laboratory(array_user, array_monster_inventory, array_monster, user_id)
                    elif perintah == "SAVE":
                        save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                    elif perintah == "EXIT":
                        keluar = exit()
                        if keluar == True:
                            save(array_user, array_monster, array_monster_inventory, array_monster_shop, array_item_inventory, array_item_shop)
                            print("Sampai jumpa kembali Agent!")
                        elif keluar == False:
                            print("Sampai jumpa kembali Agent!")
                        break
                    else:
                        print("Perintah tidak valid!")
    
            print()
            print('Masukkan perintah!\nKetik "HELP" untuk melihat menu')
            perintah = input(">>> ").upper()
                
    # keluar dari program jika nama folder tidak ditemukan
    elif check_folder == False:
        print('Folder "'+args.folder+'" tidak ditemukan!')