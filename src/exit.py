# PROGRAM F16 - Exit
# Writer: Bertha Soliany Frandi
# Tanggal: 6 Mei 2024

def exit() -> bool:
    reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
    while True:
        if reassure == "iya" or reassure == "IYA" or reassure == "Iya":
            return True            
        elif reassure == "tidak" or reassure == "TIDAK" or reassure == "Tidak":
            return False
        else:
            print("Input tidak valid")
            reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
