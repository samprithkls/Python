lst=list(map(int,input().split()))
a=lst[0]
b=lst[1]
for i in range(a,b+1,1):
    if(i-a==b-i):
        print(i)
