n=int(input())

temp=n
order=1
count=0
while(n!=0):
    count=count+1
    order=order*10
    n//=10
order//=10


n=temp

last=n%10



first=n//order

i=1
a=0
while(n!=0):
    if(i==1):
        a=a*10+last
    elif(i==count):
        a=a*10+first
    else:
        digit=n//order
        a=a*10+digit
    n=n%order
    order=order//10
    i=i+1
    
print(a)
        
    
