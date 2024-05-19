# PROGRAM F14 - Load
# Writer: Bertha Soliany Frandi
# Tanggal: 10 Mei 2024

import os
import sys
import argparse

# KAMUS
# folder path : string
# check_folder : bool

# ALGORITMA
parser = argparse.ArgumentParser(description="load data dari folder yang dipilih")
parser.add_argument("folder", nargs='?', help="nama folder yang berisi data yang ingin di load")
args = parser.parse_args()

# mengeluarkan error message
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
