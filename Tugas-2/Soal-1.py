daftar_kontak = []
a = 0

while a==0:
    print("Selamat datang !")
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()

    menu = int(input("Pilih menu : ")) 
    z = menu    
    def tambah_kontak():
        for i in range(1):
            nama = input("Nama : ")
            notelp = input("No Telepon : ")
            data = {
                "nama"   : nama,
                "notelp" : notelp,
            }
        daftar_kontak.append(data)
        print("Kontak berhasil ditambahkan")
        print()
    def kontak():
        for i in daftar_kontak:
            print("Nama : ",i["nama"])
            print("No Telepon : ",i["notelp"])
            print()

    x=0 
    if menu == 1:
        while x==0:
            kontak()
            pilihan = input("Apakah sudah selesai (Y/T) : ")
            if pilihan=="Y":
                x = 1 

    elif menu == 2:
      while x==0:  
        tambah_kontak()
        pilihan = input("Apakah sudah selesai (Y/T) : ")
        if pilihan=="Y":
          x = 1   
    elif menu == 3:
        print("Program selesai, sampai jumpa!")  
    else:
        print("Menu tidak tersedia")     

    
    if z == 3:
        a = 1                