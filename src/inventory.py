# PROGRAM F07 - Inventory
# Writer: Michael Alexander Angkawijaya
# Hari, tanggal: 10 Mei 2024
# KAMUS 
# user : array
# item_inventory : array of array
# monster_inventory : array of array
# monster : array of array

def is_integer(user_input: str):
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True


def inventory(user: list, item_inventory: list, monster_inventory: list, monster: list):
    user_inventory = []
    count = 1
    print(f"=========== INVENTORY LIST (User ID: {user[0]}) ===========")
    print(f"Jumlah O.W.C.A Coin-mu sekarang {user[4]}.")
    for i in range(len(monster_inventory)):
        if(str(monster_inventory[i][0])==str(user[0])): #Jika user_id cocok
            print(f"{count}. Monster \t(Name: {monster[int(monster_inventory[i][1])-1][1]}, Lvl. {monster_inventory[i][2]}, HP: {monster[int(monster_inventory[i][1])-1][4]})")
            detail_item = monster[int(monster_inventory[i][1])-1].copy()
            detail_item[0] = "Monster"
            detail_item.append(monster_inventory[i][2])
            user_inventory.append(detail_item)
            count += 1
    for i in range(len(item_inventory)):
        if(str(item_inventory[i][0])==str(user[0])): #Jika user_id cocok
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
    print("Ketikkan id untuk menampilkan detail item:")
    while(True):
        idx = input()
        if(is_integer(idx)):
            idx = int(idx)
            if((idx>=1)and(idx<count)):
                break
        print("Ketikkan id untuk menampilkan detail item:")
    if(user_inventory[idx-1][0]=="Monster"):
        print(f"""Monster
Name      : {user_inventory[idx-1][1]}
ATK Power : {user_inventory[idx-1][2]}
DEF Power : {user_inventory[idx-1][3]}
HP        : {user_inventory[idx-1][4]}
Level     : {user_inventory[idx-1][5]}
""")
    else: # user_inventory[idx-1][0]=="Potion"
        print(f"""Potion
Type      : {user_inventory[idx-1][1]}
Quantity  : {user_inventory[idx-1][2]}
""")
    