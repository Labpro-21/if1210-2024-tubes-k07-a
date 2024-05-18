# Program: Shop management
# Writer: Felicia Kannitha Ruth
# Hari, tanggal: 14 Mei 2024
# Note: 

def is_integer(user_input: str) -> bool:
    for char in user_input:
        if (ord(char) < ord('0')) or (ord(char) > ord('9')):
            return False
    return True

# fungsi untuk mengeluarkan list dengan rapih
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

def id_shop(data: list)-> list:
    # Akan digunakan untuk mengecek id yang akan digunakan
    # saat akan membeli monster
    id = []
    for i in range(1, len(data)):
        id.append(data[i][0])
    
    return id

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

def add(data_monstershop: list, data_monster: list, data_potionshop: list)-> tuple[list,list]:
    while True: 
        add_things = input("Mau menambahkan apa? (monster/potion): ").lower()
        if add_things == 'monster':
            # data untuk id monster
            id_monster = id_shop(data_monstershop)
            # data untuk monster
        
            data_monsterid = [] # membuat array untuk menyimpan data
            id_add = []
        
            # id monster yang ada di database tetapi belum ada di shop
            # cek biar bisa menambahkan 
            for i in range(len(data_monster)):
                # apabila ada data yang belum ada di shop
                if data_monster[i][0] not in id_monster:
                    data_monsterid.append(data_monster[i].copy())
                    if data_monster[i][0] != "id":
                        id_add.append((data_monster[i][0]))
            
            # jika sudah ada semua maka tidak ada yang bisa ditambahkan lagi
            if len(data_monsterid) == 1:
                print("Tidak ada monster yang dapat ditambahkan!")
                break
        
            # menghasilkan data terbaru
            table(data_monsterid)
            monster_shop = []
            
            # cek masukkan id, stok, dan harga
            while True:
                # cek masukkan id apakah ada atau tidak
                id = input("Masukkan ID monster: ")
                if id not in id_add:
                    print("ID salah! Masukkan lagi")
                    continue
                else:
                    monster_shop.append(id)
                    break
            while True:
                # cek masukkan stok
                stok = input("Masukkan stok awal: ")
                if(is_integer(stok)):
                    if int(stok) < 0:
                        print("Stok awal harus lebih besar dari nol!")
                        continue
                    else:
                        monster_shop.append(stok)
                        break
            while True:
                # cek  masukkan harga
                harga = input("Masukkan harga: ")
                if(is_integer(harga)):
                    if int(harga) < 0:
                        print("Harga harus lebih besar dari nol!")
                        continue
                    else:
                        monster_shop.append(harga)
                        break
                
            # Menyimpan monster baru pada monster_shop
            data_monstershop.append(monster_shop)
            print("Monster baru berhasil ditambahkan ke dalam toko!")
            
            break
    
        elif add_things == "potion":
            potion_shop = [] # menyimpan list potion yang belum ada di shop
            
            for i in range(1, len(data_potionshop)):
                potion_shop.append(data_potionshop[i][0])

            data_potionid = []
            data_potionid.append(["ID", "TYPE"])
            # data akan dimasukkan ke data_potionid
            if "strength" not in potion_shop:
                data_potionid.append([str(len(data_potionid)), "strength"])
            if "resilience" not in potion_shop:
                data_potionid.append([str(len(data_potionid)), "resilience"])
            if "healing" not in potion_shop:
                data_potionid.append([str(len(data_potionid)), "healing"])
            
            if len(data_potionid) == 1:
                print("Tidak ada potion yang dapat ditambahkan!")
                break

            #  Menampilkan data potion terbaru
            table(data_potionid)

            # List ID yang dapat ditambah untuk validasi input
            id_tambah = []
            for i in range(1, len(data_potionid)):
                id_tambah.append(data_potionid[i][0])

            # Untuk input potion yang ingin ditambahkan
            potion_baru = []
            
            # validasi id, stok, dan harga
            while True:
                # cek apakah id valid atau tidak
                id = input("Masukkan ID potion: ")
                if id not in id_tambah:
                    print("ID salah! Masukkan ID kembali")
                    continue
                else:
                    potion_baru.append(data_potionid[int(id)][1]) # potion type
                    break
            while True:
                # cek apakah stok valid atau tidak
                stok = input("Masukkan stok awal: ")
                if(is_integer(stok)):
                    if int(stok) < 0:
                        print("Stok tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        potion_baru.append(stok)
                        break
            while True:
                # cek apakah harga valid atau tidak
                harga = input(" Masukkan harga: ")
                if(is_integer(harga)):
                    if int(harga) < 0:
                        print("Harga tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        potion_baru.append(harga)
                        break
            
            # Menyimpan potion baru
            data_potionshop.append(potion_baru)
            print("Potion baru berhasil ditambahkan ke dalam toko!")
            break
        else:
            print("Masukkan anda tidak valid. Masukkan lagi!")
    return data_monstershop, data_potionshop

# Aksi update
def update(data_monstershop: list, data_monster: list, data_potionshop: list)-> list:
    while True:
        update = input("Komponen apa yang ingin diperbaharui? (monster/potion): ")
        if update == "monster":
            
            # Menampilkan list dari monster yang ada
            table(read_filemonster(data_monstershop, data_monster))

            id_monster = id_shop(data_monstershop)
            # Validasi ID, stok, dan harga
            while True:
                id = input("Masukkan ID monster: ")
                if id not in id_monster:
                    print("ID salah! Masukkan ID kembali")
                    continue
                else:
                    break
            while True:
                harga = input("Masukkan harga baru: ")
                if(is_integer(harga)):
                    if int(harga) < 0:
                        print("Harga tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        break
            while True:
                stok = input("Masukkan stok baru: ")
                if(is_integer(stok)):
                    if int(stok) < 0:
                        print("Stok tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        break
            
            # Update stok dan harga terbaru melalui ke file monster_shop
            for i in range(len(data_monstershop)):
                if data_monstershop[i][0] == id:
                    data_monstershop[i][1] = stok
                    data_monstershop[i][2] = harga
            break

        elif update == "potion":
            
            # Menampilkan data potion pada shop
            table(read_filepotion(data_potionshop))

            id_potion = [str(i) for i in range(1, len(data_potionshop))]
            
            # Validasi ID, stok, dan harga
            while True:
                id = input("Masukkan ID potion: ")
                if id not in id_potion:
                    print("ID salah! Masukkan ID kembali")
                    continue
                else:
                    break
            while True:
                harga = input("Masukkan harga baru: ")
                if(is_integer(harga)):
                    if int(harga) < 0:
                        print("Harga tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        break
            while True:
                stok = input("Masukkan stok baru: ")
                if(is_integer(stok)):
                    if int(stok) < 0:
                        print("Stok tidak bisa lebih kecil dari nol!")
                        continue
                    else:
                        break

            # Update stok dan harga terbaru melalui ID
            for i in range(len(data_potionshop)):
                if str(i) == id:
                    data_potionshop[i][1] = stok
                    data_potionshop[i][2] = harga
            break
        else:
            print("Masukkan anda tidak valid. Masukkan lagi!")
    return  data_monstershop, data_potionshop

# Aksi delete
def delete(data_monstershop: list, data_monster: list, data_potionshop: list):
    while True:
        delete = input("Komponen apa yang ingin dihapus? (monster/potion): ")
        if delete == "monster":
            
            # Menampilkan list monster yang ada  
            table(read_filemonster(data_monstershop, data_monster))
            id_monster = id_shop(data_monstershop)
            
            while True:
                id_delete = input("Masukkan id monster: ")
                if id_delete not in id_monster:
                    # monster yang ingin dihapus harus memiliki id yang benar
                    print("ID salah! Masukkan ID kembali")
                    continue
                else: 
                    break   
                
            while True:
                check = input("Apakah anda yakin ingin menghapus monster dari toko (iya/tidak): ")
                if check.lower() == 'iya':
                # update data monster terbaru
                    data_update = []
                    for i in range(len(data_monstershop)):
                        if data_monstershop[i][0] != id_delete:
                            data_update.append(data_monstershop[i].copy())
                    return data_update, data_potionshop
                elif check.lower() == 'tidak':
                    break
                else: # masukkan selain iya atau tidak
                    print("Masukkan salah!")
            break  
        elif delete == 'potion':
            
            # Menampikan data potion pada shop
            table(read_filepotion(data_potionshop))
            
            id_delete = [str(i) for i in range(1, len(data_potionshop))]

            while True:
                id = input("Masukkan ID potion: ")
                if id not in id_delete:
                    print("ID salah! Masukkan ID kembali")
                    continue
                else:
                    break

            while True:
                check = input("Apakah anda yakin ingin menghapus potion dari toko (iya/tidak): ")
                if check.lower() == 'iya':
                    data_update = []
                    for i in range(len(data_potionshop)):
                        if str(i) != id:
                            data_update.append(data_potionshop[i].copy())
                    return data_monstershop, data_update
                elif check.lower() == 'tidak':
                    break
                else: # masukkan selain iya atau tidak
                    print("Masukkan salah!")
            break
        else:
            print("Masukkan anda tidak valid. Masukkan lagi!")
    return data_monstershop, data_potionshop

# contoh penggunaan dan tampilan akan seperti apa
# tampilan yang akan keluar
def shop_management(data_monstershop: list, data_monster: list, data_potionshop: list):
    while True:
        print("Shop Management System (Admin)")
        print("1. Lihat")
        print("2. Tambah")
        print("3. Update")
        print("4. Hapus")
        print("5. Keluar")
        choice = input("Masukkan pilihan anda: ")

        if choice == '1':
            display(data_monstershop, data_monster, data_potionshop)
        elif choice == '2':
            data_monstershop, data_potionshop = add(data_monstershop, data_monster, data_potionshop)
        elif choice == '3':
            data_monstershop, data_potionshop = update(data_monstershop, data_monster, data_potionshop)
        elif choice == '4':
            data_monstershop, data_potionshop = delete(data_monstershop, data_monster, data_potionshop)
        elif choice == '5':
            print("Anda sudah keluar dari toko. Terima kasih!")
            print("Terima kasih! Progress terakhir telah disimpan.")
            break
        else:
            print("Pilihan tidak valid, masukkan angka kembali!.")
    return data_monstershop, data_potionshop

# shop_management(data_monstershop,data_monster,data_potionshop)