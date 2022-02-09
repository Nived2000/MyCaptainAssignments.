n= int(input("Enter a number up to which series is to be printed: "))
myList = [0, 1, ]
for i in range(n):
    myList.append(i + 1)
    myList[i + 1] = myList[i] + myList[i - 1]

myList.pop()

print("The fibonacci series of", n, "is : ", myList)