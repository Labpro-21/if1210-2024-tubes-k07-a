
def csv_to_array (path):
    lines = []
    with open(path, 'r') as file:
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
        
def display():
    # validasi aksi yang akan dilakukan
    item_type = input("Anda ingin melihat Potion/Monster: ")
    if item_type.lower() == 'monster':
        table(read_filemonster())
    elif item_type.lower() == 'potion':
        table(read_filepotion())
    else:
        print("Masukkan anda tidak valid. Masukkan lagi!")

# membaca id yang ada di monster buat ngecek saat membeli monster
def id_shop(csv_file):
    id = []
    data_id = csv_to_array(csv_file)
    for i in range(1, len(data_id)):
        id.append(data_id[i][0])
    
    return id
      
# fungsi untuk membaca file dari monster dan dari potion
def read_filemonster():
    data_monsternew = []
    data_monstershop = csv_to_array('data/monster_shop.csv')
    data_monster = csv_to_array('data/monster.csv')
    
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

def read_filepotion():
    data_potionshop = csv_to_array('data/item_shop.csv')

    data_potion = []
    data_potion.append(["id", data_potionshop[0][0], data_potionshop[0][1], data_potionshop[0][2]])
    
    for i in range(1, len(data_potionshop)):
        data_potion.append([str(i), data_potionshop[i][0], data_potionshop[i][1], data_potionshop[i][2]])
        
    return data_potion

# apabila user sudah memiliki monster di dalam inventory, maka hasil akan true
def has_monsterinven(id):
    data_inventory = csv_to_array('data/monster_inventory.csv')
    for m in data_inventory:
        if m[0] == id:
            return True
    return False

# fungsi untuk membeli monster dan potion
def buy_monster():
    data_monstershop = csv_to_array("data/monster_shop.csv")
    data_monster = csv_to_array("data/monster.csv")
    data_owca = csv_to_array("data/user.csv")
    
    item_id = int(input("Masukkan ID monster: "))
    id_monster = id_shop("data/monster_shop.csv")

    if has_monsterinven(str(item_id)):
        print("Anda sudah memiliki monster ini, masukkan ID lain!")
        return
    # apabila user sudah memiliki monster tersebut, maka akan dilakukan return

    quantity = int(input("Masukkan kuantitas: "))  

    for i in range(1, len(data_monstershop)):
        id = int(data_monstershop[i][0])  
        type = data_monster[i][1]
        atk_power = data_monster[i][2]
        def_power = data_monster[i][3]
        hp = data_monster[i][4]
        stok = int(data_monstershop[i][1]) 
        price = int(data_monstershop[i][2])  
        owca = int(data_owca[user_id][4])  
    
        if item_id == id:
            owca = price * int(owca)
            price = int(price)
            if owca >= price:
                if owca >= price:
                    print(f"Kamu berhasil membeli {type}")
                    print(f"Sisa O.W.C.A kamu {owca - price}")
                    owca -= price
                    csv_to_array[user_id][4] = owca
                else:
                    print("Stok monster tidak mencukupi.")
            else:
                print("O.W.C.A kamu kurang")
            break
                
def buy_potion():
    data_potionshop = csv_to_array("data/item_inventory.csv")
    data_potion = csv_to_array("data/item_shop.csv")
    data_owca = csv_to_array("data/user.csv")         
    
    item_id = int(input("Masukkan ID potion: "))
    quantity = int(input("Masukkan kuantitas: "))
    
    for j in range (1, len(read_filepotion)):
        id_1 = j
        type_1 = data_potion[j][0]
        stok_1 = data_potion[j][1]
        harga_1 = data_potion[j][2]
    if item_id == id_1:
        owca = int(owca)
        harga_1 = int(harga_1)
        jumlah = quantity * harga_1
        if owca >= harga_1:
            print(f"kamu berhasil membeli {type_1}")
            print(f"Sisa O.W.C.A kamu {owca-jumlah}")
            owca = owca - jumlah
            data_owca[user_id][4] = owca
        elif owca < harga_1:
            print("O.W.C.A kamu kurang")

# cek dulu user ke berapa yang sedang membuka shop
user_id = int(input("Masukkan user id anda: "))

# contoh penggunaan dan tampilan akan seperti apa
def main():
    currency = 0
        
    # pilihan aksi
    while True:
        print("SHOP MENU:")
        print("1. Lihat")
        print("2. Beli")
        print("3. Keluar")
        choice = input("Masukkan pilihan anda (1/2/3): ")

        if choice == '1':
            display()
        elif choice == '2':
            item_type = input("Anda ingin membeli Potion/Monster: ")
            # validasi aksi yang akan dilakukan
            if item_type.lower() == 'monster':
                buy_monster()
            elif item_type.lower() == 'potion':
                buy_potion()
            else:
                print("Pilihan tidak valid. Silakan masukkan kembali!")
        elif choice == '3':
            print(f"Anda sudah keluar dari toko. Terima kasih sudah datang!")
            break
        else:
            print("Pilihan tidak valid. Masukkan kembali!")
            
            
main()
            
