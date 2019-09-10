n=int(input())
count=0
if(n<=3):
    print("no")
else:
    for i in range(2,n):
        if(n%i==0):
            count+=1
if(count==0):
    print("no")
else:
    print("yes")
