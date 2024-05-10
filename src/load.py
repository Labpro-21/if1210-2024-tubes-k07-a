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

    # fungsi panggil data csv menjadi array
    def load (filepath: str) -> list:
        lines = []
        with open(filepath, 'r') as file:
            for row in file:
                lines.append(row) # Mengubah csv menjadi array per baris 
        array = []
        for line in lines:
            row = []
            kata = ''
            for elmt in line:
                if elmt != ';' and elmt != '\n':
                    kata += elmt
                elif elmt == ';':
                    row.append(kata)
                    kata = ''
            row.append(kata)
            array.append(row)
        return array
    
    array_user = load(folder_path+"/user.csv")
    array_monster = load(folder_path+"/monster.csv")
    array_monster_inventory = load(folder_path+"/monster_inventory.csv")
    array_monster_shop = load(folder_path+"/monster_shop.csv")
    array_item_inventory = load(folder_path+"/item_inventory.csv")
    array_item_shop = load(folder_path+"/item_shop.csv")

elif check_folder == False:
    print('Folder "'+args.folder+'" tidak ditemukan')
