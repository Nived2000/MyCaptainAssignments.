string=input("Enter any string:")
n=int(len(string))
mydict={}
def most_frequent(string):
    for i in range(n):
        count_i=string.count(string[i])
        mydict[string[i]]=count_i
        if i==n-1:
            list=sorted(mydict.items(), key=lambda x: x[1],reverse=True)
            sorted_dict=dict(list)


            print(sorted_dict)

most_frequent(string)



