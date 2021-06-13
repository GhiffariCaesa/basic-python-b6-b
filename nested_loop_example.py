list_nilai = [80,90,70]
for x in list_nilai:
    print(x*2)
print("===========")
list_nilai_2 = [
    [80,90,70],
    [90,79,100],
]
# bentuk pertama
for x in list_nilai_2:
    for nilai in x:
        print(nilai*2)
print("===========")
# bentuk kedua        
# print(list_nilai_2 [1][2])
for i in range(len(list_nilai_2)):          
    for j in range(len(list_nilai_2[i])):
        print(list_nilai_2 [i][j] * 2)