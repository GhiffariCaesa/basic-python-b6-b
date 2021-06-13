list_buah = ["apple","banana","cherry","blueberi","semangka","melon"]
# print(list_buah[0])
# print(list_buah[1])
# print(list_buah[2])
# print(list_buah[3])
# print(list_buah[4])
# print(list_buah[5])
print("=================")
# bentuk 1
for x in list_buah:
    print(x)
print("=================")
# bentuk 2
for x in range(len(list_buah)): 
    print(list_buah[x])

# bentuk 1        bentuk 2 
# x1 = apple      x1 = 0
# x2 = banana     x2 = 1
# x3 ....         x3 ....