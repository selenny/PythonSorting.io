mylist = [89, 23, 33, 45, 10, 12, 45, 45, 45]

for putslot in range(len(mylist)-1,0,-1):
    positionOfMax = 0
    for location in range(1,putslot+1):
        if mylist[location]>mylist[positionOfMax]:
            positionOfMax = location

    temp = mylist[putslot]
    mylist[putslot] = mylist[positionOfMax]
    mylist[positionOfMax] = temp
print(mylist)
