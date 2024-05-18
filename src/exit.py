# PROGRAM F16 - Exit
# Writer: Bertha Soliany Frandi
# Tanggal: 6 Mei 2024

def exit() -> bool:
    # KAMUS LOKAL
    # reassure : string

    # ALGORITMA
    reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ").upper()
    while True:
        if reassure == "Y":
            return True            
        elif reassure == "N":
            return False
        else:
            print("Input tidak valid")
            reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ").upper()
