mylist = []
n = int(input("Enter number of elements required in the set:"))
for i in range(n):
    mylist.append(i)
    mylist[i] = int(input("Enter number:"))

print("The input is", mylist)

list2 = []
for i in range(n):
    if mylist[i] > 0:
        list2.append(mylist[i])

print("The positive numbers are", list2)
