# PROGRAM Arena
# Writer: Adrian Sami Pratama
# Hari, tanggal: 11 Mei 2024

# Kamus
from src.battle import *
# Algoritma
def arena(monsterarray: list, monster_inventory: list, item_inventory: list, user_id: int, stage: int) -> int:
    # Mulai program arena 
    print("Selamat datang di Arena!!")
    print()
    total_OC = 0
    total_damage_dealt = 0
    total_damage_taken = 0
    damage_dealt = 0
    damage_taken = 0
    while True:
        win, damage_dealt, damage_taken = battle(monsterarray, monster_inventory, item_inventory, user_id, stage, True)
        total_damage_dealt += damage_dealt
        total_damage_taken += damage_taken
        OC = [30, 50, 100, 200, 500]
        if(win):
            total_OC += OC[stage-1]
            print()
            print(f"STAGE CLEARED! Anda akan mendapatkan {OC[stage-1]} OC pada sesi ini!")
            print()
            if(stage==5):
                print("Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!")
                print()
                break
            else:
                print("Memulai stage berikutnya...")
            stage += 1
        else:
            print(f"GAME OVER! Sesi latihan berakhir pada stage {stage}!")
            print()
            break
    print(f"""
    ============== STATS ==============
    Total hadiah      : {total_OC} OC
    Jumlah stage      : {stage}
    Damage diberikan  : {int(total_damage_dealt)}
    Damage diterima   : {int(total_damage_taken)}
    """)
    return total_OC    