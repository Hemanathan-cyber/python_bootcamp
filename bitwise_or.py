N=int(input())
a=list(map(int,input().split()))
c=0
for i in range(N):
  if(i==0):
    c=a[i]|a[i+1]
    i+=1
  else:
    c=c|a[i]
print(c)
