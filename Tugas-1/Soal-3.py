print("Selamat datang di program penentu kelulusanmu")
u = float(input("Berapa nilai ujian teorimu : "))
p = float(input("Berapa nilai ujian praktikmu : "))
if u >= 70 and p >= 70:
    print("Selamat, anda lulus!")
elif u >= 70 and p < 70:
    print("Anda harus mengulang ujian praktik.")
elif u < 70 and p >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktik")