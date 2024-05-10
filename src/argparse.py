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
    
    print("Selamat datang di program OWCA!")

elif check_folder == False:
    print('Folder "'+args.folder+'" tidak ditemukan')
