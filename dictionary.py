# dictionary created
pelanggan_dict = {
    "nama" : "nafi",
    "umur" : 21,
    #key     # value
}

# list created example
pelanggan_list = []

# change data
pelanggan_dict["nama"] = "joni"

# akses dictionary
print(pelanggan_dict["nama"])
print(pelanggan_dict["umur"])

# input data dictionary data lebih dari 1
for i in range(1):
    nama = input("Masukkan Nama anda : ")
    umur = input("Masukkan Umur anda : ")
    data = {
        "nama" : nama,
        "umur" : umur,
    }
    pelanggan_list.append(data)

for i in pelanggan_list:
    print("Nama Pelanggan : ",i["nama"])
    print("Umur Pelanggan : ",i["umur"])

#data = pelanggan_list[0]
#print("Nama pelanggan : ",data["nama"])
#print("Umur pelanggan : ",data["umur"])