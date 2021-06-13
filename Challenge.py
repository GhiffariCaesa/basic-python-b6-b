phi = 22/7
r = int(input("Masukkan jari-jari : "))
def luas_lingkaran(phi, r):
    return phi*(r**2)
def keliling_lingkaran(phi, r):
    return 2*phi*r
print("Luas Lingkaran adalah : ",luas_lingkaran(phi, r))  
print("Keliling lingkaran adalah : ",keliling_lingkaran(phi, r))