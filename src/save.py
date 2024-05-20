# PROGRAM F15 - Save
# Writer: Bertha Soliany Frandi
# Tanggal: 9 Mei 2024

# ALGORITMA
import os
import time # untuk time.sleep
# setiap function akan return array yang sudah dimodifikasi (karena hasil permainan)

def save(array_user: list, array_monster: list, array_monster_inventory: list, array_monster_shop: list, array_item_inventory: list, array_item_shop: list):
    # KAMUS LOKAL
    # folder : string
    # parent_check, folder_check : bool
    # list_folder : array of character
    # list_ascii : array of integer

    # ALGORITMA
    folder = input("Masukkan nama folder: ")

    while True:
        # convert to ASCII
        # mengubah username dari string ["halo"] menjadi array of character ['h','a','l','o']
        list_folder = []   # inisialisasi list of character dari nama folder
        for letter in list_folder:
            list_folder.append(letter) 
        # mengubah username menjadi ASCII
        list_ascii = [0 for i in range(len(folder))] # inisialisasi array ASCII
        for i in range(len(folder)): 
            list_ascii[i] = ord(folder[i])

        for i in list_ascii:
            if i == 34 or i == 42 or i == 47 or i == 58 or i == 60 or i == 62 or i == 63 or i == 92 or i ==124:
                print(r'Nama folder tidak boleh mengandung karakter sebagai berikut: \/:*?"<>|')
                folder = input("Masukkan nama folder: ")
        if folder == "":
            print("Nama folder tidak boleh kosong. Masukkan ulang nama folder.")
            folder = input("Masukkan nama folder: ")
        else:
            break
    
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
            for i in range(len(row)):
                if i == len(row)-1:
                    file.write(row[i])
                elif i < len(row)-1:
                    file.write(row[i] + ';')
            file.write('\n')
