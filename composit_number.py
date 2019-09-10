a=int(input())
count=0
if(a<=3):
    print("no")
else:
    for i in range(2,a):
        if(a%i==0):
            count+=1
if(count==0):
    print("no")
else:
    print("yes")
