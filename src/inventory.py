# PROGRAM F07 - Inventory
# Writer: Michael Alexander Angkawijaya
# Hari, tanggal: 10 Mei 2024
# KAMUS 
# user : array
# item_inventory : array of array
# monster_inventory : array of array
# monster : array of array

user = [2,"Asep_Spakbor","asepwow123","agent",9999]
item_inventory = [[2,"strength",5],[2,"resilience",3],[3,"resilience",7],[4,"healing",3],[5,"strength",20]]
monster_inventory = [[2,1,1],[3,2,2],[3,3,1],[4,4,1],[5,5,5]]
monster = [[1,"Pikachow",125,10,600],[2,"Bulbu",50,50,1200],[3,"Zeze",300,10,100],[4,"Zuko",100,25,800],[5,"Chacha",80,30,700]]
def inventory(user, item_inventory, monster_inventory, monster):
    user_inventory = []
    count = 1
    print(f"=========== INVENTORY LIST (User ID: {user[0]}) ===========")
    print(f"Jumlah O.W.C.A Coin-mu sekarang {user[4]}.")
    for i in range(len(monster_inventory)):
        if(monster_inventory[i][0]==user[0]): #Jika user_id cocok
            print(f"{count}. Monster \t(Name: {monster[monster_inventory[i][1]-1][1]}, Lvl. {monster_inventory[i][2]}, HP: {monster[monster_inventory[i][1]-1][4]})")
            detail_item = monster[monster_inventory[i][1]-1].copy()
            detail_item[0] = "Monster"
            detail_item.append(monster_inventory[i][2])
            user_inventory.append(detail_item)
            count += 1
    for i in range(len(item_inventory)):
        if(item_inventory[i][0]==user[0]): #Jika user_id cocok
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
    idx = int(input())
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
    
# cara call : inventory(user, item_inventory, monster_inventory, monster)