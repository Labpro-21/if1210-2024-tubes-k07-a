# PROGRAM Pembaca File CSV Monster dan Mekanik Battle Monster
# Writer: Adrian Sami Pratama
# Hari, tanggal: 30 April 2024

# KAMUS

#Algoritma
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

# print(csv_to_array("D:\ITB\Dasar Pemrograman\Tugas Besar Fix\if1210-2024-tubes-k07-a\data\monster.csv"))