from save import save

def exit():
    reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
    while True:
        if reassure == "iya" or reassure == "IYA" or reassure == "Iya":
            save()
            break
        elif reassure == "tidak" or reassure == "TIDAK" or reassure == "Tidak":
            break
        else:
            print("Input tidak valid")
            reassure = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (iya/tidak) ")
exit()