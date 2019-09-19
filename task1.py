a=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
print(len(a))
sc=0
max_length=0
for i in a:
    if isinstance(i,list):
        sc+=1
        if max_length < len(i):
            max_length=len(i)
            index=a.index(i)
print("number of sublist in list :",sc)
print("sub list with max length:",a[index])
print("index of sub list with max length:",index)
print("first element of the sub list with max length:",a[index][0])
