a=[3,5,[3,56],3,[3,7,'zen',4.6],'guvi',5,2,'pit']
print(len(a))
count=0
max=0
for i in a:
    if isinstance(i,list):
        count+=1
        if max < len(i):
            max=len(i)
            index=a.index(i)
print("number of sublist in the list :",count)
print("sub list with maximum length is :",a[index])
print("index of sub list with maximum length is :",index)
print("first element of the sub list with maximum length is :",a[index][0])
