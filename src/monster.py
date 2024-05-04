# PROGRAM Pembaca File CSV Monster dan Mekanik Battle Monster
# Writer: Adrian Sami Pratama
# Hari, tanggal: 30 April 2024

# KAMUS

#Algoritma
from lcg import *
# monsterfile = open("D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv")

def csv_to_array (filepath: str) -> list: # Fungsi untuk mengubah csv menjadi array
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

def attack(attackpower: float) -> float: # Fungsi untuk generate damage dari attack power
    x = generate_number(defaultlcg, [0,2])
    tanda = 0
    if x == 0:
        tanda = -1
    else:
        tanda = 1
    pengali = generate_number(defaultlcg, [1, 31])
    damage = ((tanda*pengali)/100)*attackpower + attackpower
    return damage 
    
def defense(defpower: float, enemydamage: float) -> float: # Fungsi untuk menghitung damage yang diterima setelah dikurangi dengan DEF power
    damage_taken = enemydamage - (defpower/100)*enemydamage
    return damage_taken

def level_buff(level: int, user_battle_monster: list) -> list: # Buff atribut sesuai level. Digunakan pada saat battle, otomatis mengubah atribut attack, defense, HP menjadi integer
    if level > 1: # Jika level lebih dari 1, atribut dibuff sesuai level, dan diubah menjadi integer
        user_battle_monster[2] = int(user_battle_monster[2]) + (int(user_battle_monster[2])*((level*10)/100)) # Buff attack
        user_battle_monster[3] = int(user_battle_monster[3]) + (int(user_battle_monster[3])*((level*10)/100)) # Buff defense
        user_battle_monster[4] = int(user_battle_monster[4]) + (int(user_battle_monster[4])*((level*10)/100)) # Buff HP
    else: # Jika level 1, atribut tidak dibuff, hanya diubah menjadi integer saja
        user_battle_monster[2] = int(user_battle_monster[2])
        user_battle_monster[3] = int(user_battle_monster[3])
        user_battle_monster[4] = int(user_battle_monster[4])
    return user_battle_monster

# monsterarray = csv_to_array(r"D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv")
# print(monsterarray)
# print(level_buff(5, 2, monsterarray))

# print(attack(500))
# print(csv_to_array("D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv"))