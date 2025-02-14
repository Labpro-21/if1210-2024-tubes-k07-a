# PROGRAM Simulasi Battle Turn Based
# Writer: Adrian Sami Pratama
# Hari, tanggal: 3 Mei 2024
# Note: All bug fixed (harusnya)

# Kamus
# monsterarray, item_inventory, monster_inventory: list
# monster_muncul: integer

# Algoritma
from src.monster import *
from src.potion import *
import math
import time
# monsterarray = csv_to_array(r"D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv")
# item_inventory = csv_to_array(r"D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\item_inventory.csv")
# monster_inventory = csv_to_array(r"D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster_inventory.csv")
# user_id = 3

def is_integer(user_input: str) -> bool:
    for char in str(user_input):
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def pilih_monster(user_id: int, monster_inventory: list, monsterarray: list) -> list:
    count = 1 # Nomor list
    # i adalah user id
    pilihan_monster = []
    for i in range(len(monster_inventory)):
        if str(user_id) == str(monster_inventory[i][0]):
            monster_id = int(monster_inventory[i][1])
            print(f"{count}. {monsterarray[monster_id][1]}")
            count += 1
            pilihan_monster.append(monsterarray[monster_id].copy())
    return pilihan_monster

def gambar_monster_user(): # Untuk mengeprint gambar monster yang dipilih user
    print(r"""
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 
""")

def monster_dipilih_user(level: int, user_battle_monster: list): # Untuk menampilkan data monster user
    print(f"""
RAWRRR, Agent X mengeluarkan monster {user_battle_monster[1]} !!!

Name      : {user_battle_monster[1]}
ATK Power : {user_battle_monster[2]}
DEF Power : {user_battle_monster[3]}
HP        : {user_battle_monster[4]}
Level     : {level}
""")
    
def output_user_turn(turn_counter: int, monster_name: str): # Untuk menampilkan pilihan yang bisa dilakukan user
    print(f"""
============ TURN {turn_counter} ({monster_name}) ============
1. Attack
2. Use Potion
3. Quit
""")

def output_bot_turn(turn_counter: int, bot_monster_name: str, user_monster_name: str): # Untuk menampilkan turn bot (hanya attack)
    print(f"""
============ TURN {turn_counter} ({bot_monster_name}) ============

SCHWINKKK, {bot_monster_name} menyerang {user_monster_name} !!!
""")
    time.sleep(1)

def attack_result(enemy_battle_monster: list, user_battle_monster: list, user_damage: int, damage_reduction: int, damage_after_reduction:int, base_HP_enemy_monster: int, user_battle_monster_level: int, enemy_battle_monster_level: int):
    tanda = 1
    if user_damage < user_battle_monster[2]:
        tanda = 0
    else:
        tanda = 1
    if tanda == 0:
        tanda = '-'
        print(f"""
Name      : {enemy_battle_monster[1]}
ATK Power : {enemy_battle_monster[2]}
DEF Power : {enemy_battle_monster[3]}
HP        : {base_HP_enemy_monster}
Level     : {enemy_battle_monster_level}

Penjelasan: ATT: {user_damage} ({tanda}{math.floor((user_battle_monster[2]-user_damage)/user_battle_monster[2]*100)}%), Reduced by: {damage_reduction} ({enemy_battle_monster[3]}%), ATT Results: {damage_after_reduction}
""")
    else:
        tanda = '+'
        print(f"""
Name      : {enemy_battle_monster[1]}
ATK Power : {enemy_battle_monster[2]}
DEF Power : {enemy_battle_monster[3]}
HP        : {base_HP_enemy_monster}
Level     : {enemy_battle_monster_level}

Penjelasan: ATT: {user_damage} ({tanda}{math.floor((user_damage-user_battle_monster[2])/user_battle_monster[2]*100)}%), Reduced by: {damage_reduction} ({enemy_battle_monster[3]}%), ATT Results: {damage_after_reduction}
""")

def user_attack_turn(user_monster_name: str, bot_monster_name: str): # Untuk menampilkan 
    print(f"""
SCHWINKKK, {user_monster_name} menyerang {bot_monster_name} !!!
""")
    time.sleep(1)

def gambar_monster_musuh(): # Untuk mengeprint gambar monster yang muncul
    print(r"""
           _/\----/\   
          /         \     /\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
""")

def munculmonster(monsterarray: list, monster_muncul_id: int): # Untuk menampilkan data monster yang muncul
    gambar_monster(monsterarray[monster_muncul_id][0])
    print(f"""
RAWRRR, Monster {monsterarray[monster_muncul_id][1]} telah muncul !!!

Name      : {monsterarray[monster_muncul_id][1]}
ATK Power : {monsterarray[monster_muncul_id][2]}
DEF Power : {monsterarray[monster_muncul_id][3]}
HP        : {monsterarray[monster_muncul_id][4]}
Level     : 1

""")

def dapet_duit(user: list)-> list:
    OC = generate_number(lcg(a=48271, c=0, m=2**31-1, seed=None), [5, 31])
    print(f"OC yang diperoleh: {OC}")
    user_oc = int(user[4])
    user_oc += OC
    user[4] = str(user_oc)  
    return user

def pilihmonster(monsterarray: list, monster_inventory: list, user_id: int)-> tuple[int,list]:
    print(r"============ MONSTER LIST ============")
    pilihan_monster = pilih_monster(user_id, monster_inventory, monsterarray)
    while True: # Validasi pilihan monster
        monster_dipilih = input("Pilih monster untuk bertarung: ")
        print()
        if monster_dipilih == "":
            print("Input tidak boleh kosong!")
        elif(is_integer(monster_dipilih)):
            monster_dipilih = int(monster_dipilih)
            if((monster_dipilih>=1)and(monster_dipilih<=len(pilihan_monster))): 
                break
        print("Pilihan nomor tidak tersedia!\n")
    return monster_dipilih, pilihan_monster

# Mulai program
def battle(monsterarray: list, monster_inventory: list, item_inventory: list, user_id: int, bot_battle_monster_level: int, arena: bool, monster_dipilih:int, pilihan_monster:list)-> bool:
    time.sleep(1)
    win = False # Boolean untuk hasil battle
    monster_muncul_id = generate_number(lcg(a=48271, c=0, m=2**31-1, seed=None), [1,len(monsterarray)])
    munculmonster(monsterarray, monster_muncul_id)
    if not arena:
        monster_dipilih, pilihan_monster = pilihmonster(monsterarray, monster_inventory, user_id)
    # Sudah memilih monster yang akan bertarung, memasukkan semua variabel untuk dipake kalkulasi battle
    user_battle_monster = pilihan_monster[monster_dipilih-1].copy() # Memasukkan data array monster user yang dipilih
    bot_battle_monster = monsterarray[monster_muncul_id].copy() # Memasukkan data array monster bot yang akan melawan user
    user_battle_monster_level = 1
    for i in range(1, len(monster_inventory)): # Memasukkan data level monster user
        if user_id == int(monster_inventory[i][0]) and int(monster_inventory[i][1]) == int(user_battle_monster[0]):
            user_battle_monster_level = int(monster_inventory[i][2]) # Level monster user

    user_battle_monster = level_buff(user_battle_monster_level, user_battle_monster) # Mengubah atribut sesuai level monster dan menjadikannya integer
    bot_battle_monster = level_buff(bot_battle_monster_level, bot_battle_monster) # Mengubah atribut monster musuh menjadi integer (level musuh di-cap di lvl 1)

    # Base atk, base def, HP user yang sudah dibuff level
    base_atk_user_monster = user_battle_monster[2]
    base_def_user_monster = user_battle_monster[3]
    base_HP_user_monster = user_battle_monster[4]

    # Base atk, base def, HP bot yang sudah dibuff level
    base_atk_bot_monster = bot_battle_monster[2]
    base_def_bot_monster = bot_battle_monster[3]
    base_HP_bot_monster = bot_battle_monster[4]

    # Proses battle
    if(arena):
        print(f"============= STAGE {bot_battle_monster_level} =============")
    time.sleep(1)
    gambar_monster(user_battle_monster[0])
    monster_dipilih_user(user_battle_monster_level, user_battle_monster)
    time.sleep(1)
    status_potion = {"strength":False,"resilience":False,"healing":False}
    turn_counter = 1
    kabur = False
    total_damage_dealt = 0
    total_damage_taken = 0
    while base_HP_user_monster > 0 and base_HP_bot_monster > 0:
        # Turn user
        output_user_turn(turn_counter, user_battle_monster[1])
        while(True):
            user_action = input("Pilih perintah: ") # Aksi yang dipilih user pada turn
            if user_action == "":
                print("Aksi tidak boleh kosong!")
            elif(is_integer(user_action)):
                user_action = int(user_action)
                if user_action == 1: # Jika user memilih attack
                    user_attack_turn(user_battle_monster[1], bot_battle_monster[1]) # User menyerang bot
                    damage = attack_user(base_atk_user_monster) # Randomize damage +- 30%
                    damage_reduction = defense(base_def_bot_monster, damage) # Damage reduction akibat atribut defense
                    damage_after_reduction = damage - defense(base_def_bot_monster, damage) # Damage setelah dikurangi defense musuh
                    total_damage_dealt += damage_after_reduction # khusus arena
                    base_HP_bot_monster = math.floor(base_HP_bot_monster - damage_after_reduction) # HP berkurang karena damage musuh
                    if base_HP_bot_monster <= 0:
                        base_HP_bot_monster = 0
                    attack_result(bot_battle_monster, user_battle_monster, damage, damage_reduction, damage_after_reduction, base_HP_bot_monster, user_battle_monster_level, 1)
                    time.sleep(2)
                    break
                elif user_action == 2: # Jika user memilih use potion
                    item_inventory, status_potion, code = use_potion(user_id,item_inventory,status_potion,user_battle_monster[1])
                    if(code==1):
                        base_atk_user_monster += int(base_atk_user_monster*5/100)
                        user_battle_monster[2] = base_atk_user_monster # untuk di print
                        break
                    elif(code==2):
                        base_def_user_monster += int(base_def_user_monster*5/100)
                        user_battle_monster[3] = base_def_user_monster # untuk di print
                        break
                    elif(code==3):
                        base_HP_user_monster += int(base_HP_user_monster*25/100)
                        if(base_HP_user_monster>user_battle_monster[4]):
                            base_HP_user_monster = user_battle_monster[4]
                            user_battle_monster[4] = base_HP_user_monster # untuk di print
                        break
                    else: # code == 0, artinya user memilih Cancel pada potion
                        pass
                elif user_action == 3: # Jika user memilih quit
                    kabur = True
                    print("Anda berhasil kabur dari BATTLE!")
                    break
                else:
                    print("Perintah tidak valid, ulangi!")
            else:
                print("Perintah tidak valid, ulangi!")
        if(kabur):
            break

        if base_HP_bot_monster == 0: # Jika saat user menyerang, musuh sudah mati
            break

        # Turn bot
        output_bot_turn(turn_counter, bot_battle_monster[1], user_battle_monster[1])
        damage = attack_bot(base_atk_bot_monster) # Randomize damage +- 30%
        damage_reduction = defense(base_def_user_monster, damage) # Damage reduction akibat atribut defense
        damage_after_reduction = damage - defense(base_def_user_monster, damage) # Damage setelah dikurangi defense musuh
        total_damage_taken += damage_after_reduction #khusus arena
        base_HP_user_monster = math.floor(base_HP_user_monster - damage_after_reduction) # HP berkurang karena damage musuh
        if base_HP_user_monster <= 0:
            base_HP_user_monster = 0
        attack_result(user_battle_monster, bot_battle_monster, damage, damage_reduction, damage_after_reduction, base_HP_user_monster, 1, user_battle_monster_level)
        time.sleep(2)
        turn_counter += 1

    # Selesai battle
    if base_HP_bot_monster == 0: # Kasus menang
        print(f"Selamat, Anda berhasil mengalahkan monster {bot_battle_monster[1]} !!!")
        win = True

    elif base_HP_user_monster == 0: # Kasus kalah
        print(f"Yahhh, Anda dikalahkan monster {bot_battle_monster[1]}. Jangan menyerah, coba lagi !!!")
    if(arena):
        return win, total_damage_dealt, total_damage_taken

    return win

# print(battle(monsterarray, monster_inventory, item_inventory, user_id)) # Contoh battle

def battlemain(monsterarray: list, monster_inventory: list, item_inventory: list, user_id: int, bot_battle_monster_level: int, arena: bool, monster_dipilih:int, pilihan_monster:list, array_user:list)->list:
    while True:
        win = battle(monsterarray, monster_inventory, item_inventory, user_id, bot_battle_monster_level, arena, monster_dipilih, pilihan_monster)
        if(win):
            array_user[user_id] = dapet_duit(array_user[user_id])
        print()        
        print("============= =============")
        battle_lagi = input("Apakah Anda ingin melakukan Battle lagi? (Y/N) ").upper()
        while True:
            if battle_lagi != "Y" and battle_lagi != "N":
                print("Input tidak valid! Lakukan input ulang!\n")
                battle_lagi = input("Apakah Anda ingin melakukan Battle lagi? (Y/N) ").upper()
            else:
                break
        if battle_lagi == "N":
            print("Sampai jumpa di BATTLE selanjutnya, Agent!\n")
            break
    return array_user[user_id]