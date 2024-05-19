# PROGRAM F07 - Inventory
# Writer: Michael Alexander Angkawijaya
# Hari, tanggal: 10 Mei 2024

# KAMUS 
# user : array
# item_inventory : array of array
# monster_inventory : array of array
# monster : array of array

def is_integer(user_input: str) -> bool:
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True


def inventory(user: list, item_inventory: list, monster_inventory: list, monster: list):
    print()
    print("Selamat datang di Inventory!\nAnda dapat melihat detail monster dan item yang dimiliki pada Inventory\n")
    while True:
        print("Pilih aksi yang Anda ingin lakukan!")
        print("1.Buka Inventory\n2.Keluar\n")
        aksi = input("Masukkan angka dari aksi yang ingin Anda lakukan: ")
        if aksi == "1":
            print()
            user_inventory = []
            count = 1
            print(f"=========== INVENTORY LIST (User ID: {user[0]}) ===========")
            print(f"Jumlah O.W.C.A Coin-mu sekarang {user[4]}.")
            for i in range(len(monster_inventory)):
                if(str(monster_inventory[i][0])==str(user[0])): #Jika user_id cocok
                    print(f"{count}. Monster \t(Name: {monster[int(monster_inventory[i][1])][1]}, Lvl. {monster_inventory[i][2]}, HP: {monster[int(monster_inventory[i][1])][4]})")
                    detail_item = monster[int(monster_inventory[i][1])].copy()
                    detail_item[0] = "Monster"
                    detail_item.append(monster_inventory[i][2])
                    user_inventory.append(detail_item)
                    count += 1
            for i in range(len(item_inventory)):
                if(str(item_inventory[i][0])==str(user[0])): #Jika user_id cocok
                    if(int(item_inventory[i][2])!=0): #Jika potion ada
                        if(item_inventory[i][1]=="strength"):
                            tipe = "ATK"
                        elif(item_inventory[i][1]=="resilience"):
                            tipe = "DEF"
                        else:
                            tipe = "Heal"
                        print(f"{count}. Potion \t(Type: {tipe}, Qty: {item_inventory[i][2]})")
                        detail_item = ["Potion",tipe,item_inventory[i][2]]
                        user_inventory.append(detail_item)
                        count += 1
            print()
            print("Ketikkan id untuk menampilkan detail item: ",end="")
            while(True):
                idx = input()
                if idx == "":
                    print("Input tidak boleh kosong!")
                elif(is_integer(idx)):
                    idx = int(idx)
                    if((idx>=1)and(idx<count)):
                        break
                    else:
                        print("Input tidak valid! Masukkan angka yang sesuai dengan jumlah jenis barang yang Anda punya!")
                print("\nKetikkan id untuk menampilkan detail item: ",end="")
            print()
            if(user_inventory[idx-1][0]=="Monster"):
                print(f"""Monster
        Name      : {user_inventory[idx-1][1]}
        ATK Power : {int(user_inventory[idx-1][2]) + int((int(user_inventory[idx-1][2])*(((int(user_inventory[idx-1][5])-1)*10)/100)))}
        DEF Power : {int(user_inventory[idx-1][3]) + int((int(user_inventory[idx-1][3])*(((int(user_inventory[idx-1][5])-1)*10)/100)))}
        HP        : {int(user_inventory[idx-1][4]) + int((int(user_inventory[idx-1][4])*(((int(user_inventory[idx-1][5])-1)*10)/100)))}
        Level     : {user_inventory[idx-1][5]}
        """)
            else: # user_inventory[idx-1][0]=="Potion"
                print(f"""Potion
        Type      : {user_inventory[idx-1][1]}
        Quantity  : {user_inventory[idx-1][2]}
        """)
        elif aksi == "2":
            print("Anda keluar dari Inventory!")
            break
        else:
            print("Aksi tidak valid! Masukkan ulang input!\n")