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

# print(attack(500))
# print(csv_to_array("D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv"))