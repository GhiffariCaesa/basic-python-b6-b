x = int(input("Masukkan x : "))
y = int(input("Masukkan y : "))

if x > y :
    print("x itu lebih besar dari y")
elif x < y:
    print("x itu kurang dari y")
elif x == y:
    print("x dan y itu sama")
else:
    print("salah input !")

tanya = input("Mau makan ? ")
if tanya == "ya" or tanya == "YA":
    print("mau makan apa ?")
elif tanya == "tidak":
    print("oke kalau gitu mau cemilan ?")
else:
    print("oke")