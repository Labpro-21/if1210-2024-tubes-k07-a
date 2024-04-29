# PROGRAM F04 - Menu & Help
# Writer: Michael Alexander Angkawijaya
# Hari, tanggal: 29 April 2024
# KAMUS 
# login : boolean
# role, username : string

def help(login,role,username):
    print()
    print("=========== HELP ===========")
    print()
    if(login):  # sudah login
        if(role=="admin"):
            print("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
            print()
            print("\t1. Logout: Keluar dari akun yang sedang digunakan")
            print("\t2. Shop: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
            print("\t3. Monster: Melakukan manajemen pada database monster")
        else: #role == "agent"
            print(f"Halo Agent {username}. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu tidak sesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print()
            print("\t1. Logout: Keluar dari akun yang sedang digunakan")
            print("\t2. Monster: Melihat owca-dex yang dimiliki oleh Agent")
            print("\t3. Inventory: Melihat detail monster, potion, dan OC yang dimiliki oleh Agent")
            print("\t4. Battle: Bertarung 1v1 melawan monster")
            print("\t5. Arena: Melatih monster yang dimiliki oleh Agent")
            print("\t6. Shop: Membeli item berupa monster atau potion")
            print("\t7. Laboratory: Meningkatkan level monster yang dimiliki oleh Agent")
    else: # belum login
        print("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print()
        print("\t1. Login: Masuk ke dalam akun yang sudah terdaftar")
        print("\t2. Register: Membuat akun baru")
    print()
    print("Footnote:")
    print("\t1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
    print("\t2. Jangan lupa untuk memasukkan input yang valid")
    print()


