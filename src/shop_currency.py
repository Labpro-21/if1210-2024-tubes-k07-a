# Program: Shop Currency
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 14 Mei 2024
# Note: 

def is_integer(user_input: str) -> bool:
    for char in user_input:
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

def table(array):
    max_lengths = [0] * len(array[0]) # inisialisasi panjang maksimum dengan angka 0
    for line in array:
        for i in range(len(line)):
            item_length = len(str(line[i]))
            if item_length > max_lengths[i]:
                max_lengths[i] = item_length # mencari panjang maksimum untuk mengetahui berapa banyak whitespace yang perlu ditambahkan
    for line in array:
        for i in range(len(line)):
            item = line[i]
            num_spaces = max_lengths[i] - len(str(item))  # menambah whitespace sesuai panjang maksimum dikurangi panjang item
            if i < len(line) - 1: # kalau bukan akhir dari tabel tambahkan "|"
                print(item, end=" " * num_spaces + " | ")
            else: # untuk akhir dari tabel tidak perlu ditambah "|"
                print(item, end=" " * num_spaces + " ")
        print()
        
# fungsi untuk mengeluarkan list dari monster/potion 
# pilihan aksi pertama dari Main (Lihat)
def display(data_monstershop: list, data_monster: list, data_potionshop: list):
    # validasi aksi yang akan dilakukan
    item_type = input("Anda ingin melihat Potion/Monster: ")
    if item_type.lower() == 'monster':
        table(read_filemonster(data_monstershop, data_monster))
    elif item_type.lower() == 'potion':
        table(read_filepotion(data_potionshop))
    else:
        print("Masukkan anda tidak valid. Masukkan lagi!")

def id_shop(data: list)-> list:
    # Akan digunakan untuk mengecek id yang akan digunakan
    # saat akan membeli monster
    id = []
    for i in range(1, len(data)):
        id.append(data[i][0])
    
    return id

# fungsi untuk membaca file dari monster dan dari potion
def read_filemonster(data_monstershop: list, data_monster: list)-> list:
    data_monsternew = []
    
    data_monsternew.append (["id", "type", "atk_power", "def_power", "hp", "stok", "harga"])
    for i in range (1, len(data_monstershop)):
        for j in range (1, len(data_monster)):
            if data_monster [j][0] == data_monstershop[i][0]:
                data_monsternew.append(
                    [data_monster[j][0], data_monster[j][1], 
                     data_monster[j][2], data_monster[j][3],
                     data_monster[j][4], data_monstershop[i][1],
                     data_monstershop[i][2]])
    return data_monsternew

def read_filepotion(data_potionshop: list)-> list:

    # membuat id untuk data potion karena belum tersedia di csv item shop
    data_potion = []
    data_potion.append(["id", data_potionshop[0][0], data_potionshop[0][1], data_potionshop[0][2]])
    
    for i in range(1, len(data_potionshop)):
        data_potion.append([str(i), data_potionshop[i][0], data_potionshop[i][1], data_potionshop[i][2]])
        
    return data_potion

# apabila user sudah memiliki monster di dalam inventory, maka hasil akan true
def has_monsterinven(user_id: str, id: str, data_inventory: list)->bool:
    for m in data_inventory:
        if m[0] == user_id:
            if(m[1]==id):
                return True
    return False

# fungsi untuk membeli monster dan potion
def buy_monster(data_monster_inventory: list, data_monster: list, data_monstershop: list, data_owca: list, user_id: int)-> list:
    table(read_filemonster(data_monstershop, data_monster))
    item_id = input("Masukkan ID monster: ")
    while True:
        if(is_integer(item_id)):
            if has_monsterinven(str(user_id),str(item_id),data_monster_inventory):
                print("Anda sudah memiliki monster ini, masukkan ID lain!")
                return data_monster_inventory, data_monstershop, data_owca
                # apabila user sudah memiliki monster tersebut, maka akan dilakukan return
            else:
                break
        item_id = input("Masukkan ID monster: ")
    item_id = int(item_id)

    for i in range(1, len(data_monstershop)):
        id = int(data_monstershop[i][0])  
        type = data_monster[i][1]
        stok = int(data_monstershop[i][1]) 
        price = int(data_monstershop[i][2])  
        owca = int(data_owca[user_id][4])  
    
        if item_id == id:
            if(stok>0):
                if owca >= price:
                    print(f"Kamu berhasil membeli {type}. Item sudah masuk ke inventory-mu! ")
                    print(f"Sisa O.W.C.A. Coin-mu {owca-price}.")
                    owca -= price
                    data_owca[user_id][4] = str(owca)
                    stok -= 1
                    data_monstershop[i][1] = str(stok)
                    data_monster_inventory.append([str(user_id),str(id),str(1)])
                else:
                    print("O.W.C.A Coin-mu kurang")
            else:
                print("Stok monster tidak mencukupi.")
            return data_monster_inventory, data_monstershop, data_owca
    print("Masukkan anda tidak valid.")
    return data_monster_inventory, data_monstershop, data_owca

def buy_potion(data_potion_inventory: list, data_potionshop: list,  data_owca: list, user_id: int):         
    table(read_filepotion(data_potionshop))
    item_id = input("Masukkan ID potion: ")
    while True:
        if(is_integer(item_id)):
            break
        item_id = input("Masukkan ID potion: ")
    item_id = int(item_id)

    quantity = input("Masukkan kuantitas: ")
    while True:
        if(is_integer(quantity)):
            break
        quantity = input("Masukkan kuantitas: ")
    quantity = int(quantity)

    for j in range (1, len(data_potionshop)):
        id_1 = j
        type_1 = data_potionshop[j][0]
        stok_1 = int(data_potionshop[j][1])
        harga_1 = int(data_potionshop[j][2])
        if item_id == id_1:
            if(stok_1==0):
                print("Stok potion tidak mencukupi.")
            elif(quantity>stok_1):
                print("Stok potion tidak mencukupi.")
            else:
                owca = int(data_owca[user_id][4])
                harga_1 = int(harga_1)
                jumlah = quantity * harga_1
                if owca >= jumlah:
                    print(f"kamu berhasil membeli {quantity} {type_1} Potion. Item sudah masuk ke inventory-mu!")
                    print(f"Sisa O.W.C.A. Coin-mu {owca-jumlah}.")
                    owca -= jumlah
                    data_owca[user_id][4] = str(owca)
                    stok_1 -= quantity
                    data_potionshop[j][1] = str(stok_1)
                    for k in range(1,len(data_potion_inventory)):
                        if(data_potion_inventory[k][0]==user_id):
                            if(data_potion_inventory[k][1]==type_1):
                                stok = int(data_potion_inventory[k][1])
                                stok += quantity
                                data_potion_inventory[k][1] = str(stok)
                                return data_potion_inventory, data_potionshop, data_owca # langsung return kalau sudah punya
                    new_potion = [str(user_id),str(type_1),str(quantity)]
                    data_potion_inventory.append(new_potion)
                else: # owca < jumlah
                    print("O.W.C.A Coin-mu kurang.")
            return data_potion_inventory, data_potionshop, data_owca
    print("Masukkan anda tidak valid.")
    return data_potion_inventory, data_potionshop, data_owca

# contoh penggunaan dan tampilan akan seperti apa
def shopmain(data_monstershop: list, data_monster: list, data_potionshop: list, data_monster_inventory: list, data_potion_inventory: list, data_owca: list, user_id:int):
    # pilihan aksi
    while True:
        print("SHOP MENU:")
        print("1. Lihat")
        print("2. Beli")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        if choice == '1':
            display(data_monstershop, data_monster, data_potionshop)
        elif choice == '2':
            print(f"Jumlah O.W.C.A Coin-mu sekarang {data_owca[user_id][4]}.")
            item_type = input("Anda ingin membeli Potion/Monster: ")
            # validasi aksi yang akan dilakukan
            if item_type.lower() == 'monster':
                data_monster_inventory, data_monstershop, data_owca = buy_monster(data_monster_inventory, data_monster, data_monstershop, data_owca, user_id)
            elif item_type.lower() == 'potion':
                data_potion_inventory, data_potionshop, data_owca = buy_potion(data_potion_inventory, data_potionshop,  data_owca, user_id)
            else:
                print("Pilihan tidak valid. Silakan masukkan kembali!")
        elif choice == '3':
            print(f"Anda sudah keluar dari toko. Terima kasih sudah datang!")
            break
        else:
            print("Pilihan tidak valid. Masukkan kembali!")
    return data_monstershop, data_potionshop, data_monster_inventory, data_potion_inventory, data_owca
