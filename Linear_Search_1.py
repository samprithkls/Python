lis=[10,20,30,40,50,60,70,80,90,100,101,102,103,104,105]
n=int(input())
bool=False
for i in range(0,len(lis),1):
    if(lis[i]==n):
        bool=True
        print("Number is at position: ",i)
if(bool==False):
    print("Number not found")