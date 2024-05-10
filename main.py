# load data terlebih dahulu (sebelum program dimulai
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
      # load data dari folder yang dipilih
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
      # meminta perintah berikutnya
      perintah = input(">>> ")
      while perintah != "EXIT":
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
          elif perintah == "SHOP MANAGEMENT": 
              import shop_management
          elif perintah == "MONSTER MANAGEMENT":
              import monster_management
          elif perintah == "SAVE":
              import save
          # meminta input perintah lagi setelah perintah selanjutnya sudah selesai
          perintah = input(">>> ")
      if perintah == "EXIT":
          import exit
    
# keluar dari program jika nama folder tidak ditemukan
elif check_folder == False:
    print('Folder "'+args.folder+'" tidak ditemukan')
