# PROGRAM Menu Option Pada Battle
# Writer: Michael Alexander Angkawijaya
# Hari, tanggal: 8 Mei 2024

# KAMUS
# user_id : int
# item_inventory : matriks
# status_potion : dictionary (str:bool)
# nama_monster : string
def is_integer(user_input: str) -> bool:
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def pilih_potion(user_id: int, item_inventory: list) -> list:
    count = 1

    pilihan_potion = []
    for i in range(len(item_inventory)):
        if(str(user_id)==str(item_inventory[i][0])):
            if(count==1):
                print("=========== POTION LIST ===========")
            # cek ada potion atau tidak 
            if(int(item_inventory[i][2])>0): # Qty > 0
                # cek jenis potion
                if(item_inventory[i][1]=="strength"):
                    txt1 = "Strength"
                    txt2 = "Increases ATK Power"
                elif(item_inventory[i][1]=="resilience"):
                    txt1 = "Resilience"
                    txt2 = "Increases DEF Power"
                else: # item_inventory[i][1]=="healing"
                    txt1 = "Healing"
                    txt2 = "Restores 25% Health"
                print(f"{count}. {txt1} Potion (Qty: {item_inventory[i][2]}) - {txt2}")
                pilihan_potion.append(item_inventory[i].copy())  
                pilihan_potion[count-1].append(i) # menyimpan index di item_inventory untuk memudahkan akses
                count += 1
    if(count==1):
        print("Anda tidak memiliki Potion dalam inventory!")  
    else:
        print(f"{count}. Cancel")
    print()
    return pilihan_potion

def use_potion(user_id: int, item_inventory: list, status_potion: list, nama_monster: str):
    print()
    while True: 
        pilihan_potion = pilih_potion(user_id,item_inventory)
        if(len(pilihan_potion)==0):
            return item_inventory, status_potion, 0 
        while True:
            potion_dipilih = input("Pilih potion untuk diminum: ")
            if(is_integer(potion_dipilih)):
                potion_dipilih = int(potion_dipilih)
                break
            print("Pilihan nomor tidak tersedia!") # input tidak valid
            # ulangi

        print()
        # user memilih cancel
        if(potion_dipilih==len(pilihan_potion)+1):
            print()
            return item_inventory, status_potion, 0 
            #kembali ke state awal? how? (solved)

        #pakai potion
        elif((potion_dipilih>0)and(potion_dipilih<=len(pilihan_potion))): # 0 < potion_dipilih < len(pilihan_potion)
            index = int(pilihan_potion[potion_dipilih-1][3])
            item_inventory[index][2] = int(item_inventory[index][2])
            if(item_inventory[index][2]==0):
                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
                #ulangi
            elif(status_potion[pilihan_potion[potion_dipilih-1][1]]):
                print(f"Kamu mencoba memberikan ramuan ini kepada {nama_monster}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                #ulangi
            else:    
                item_inventory[index][2] -= 1 # mengurangi qty potion yang dipilih 
                if(pilihan_potion[potion_dipilih-1][1]=="strength"):
                    status_potion["strength"] = True
                    code = 1
                    print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {nama_monster} dan gerakannya menjadi lebih cepat dan mematikan.")
                elif(pilihan_potion[potion_dipilih-1][1]=="resilience"):
                    status_potion["resilience"] = True
                    code = 2
                    print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {nama_monster} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                else: # pilihan_potion[i][1]=="healing"
                    status_potion["healing"] = True
                    code = 3
                    print(f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {nama_monster} sembuh dengan cepat. Dalam sekejap, {nama_monster} terlihat kembali prima dan siap melanjutkan pertempuran.")
                print()
                return item_inventory, status_potion, code

        else: # input tidak valid
            print("Pilihan nomor tidak tersedia!")
            #ulangi
        print()

# item_inventory = [["userid","jenis","qty"],[2,"strength",5],[2,"resilience",3],[3,"resilience",7],[4,"healing",3],[5,"strength",20]]
# user_id = 2
# status_potion = {"strength":False,"resilience":False,"healing":False}
# item_inventory, status_potion, code = use_potion(user_id,item_inventory,status_potion,"Pikachow")
# print(item_inventory)
# print(status_potion)
# print(code)
