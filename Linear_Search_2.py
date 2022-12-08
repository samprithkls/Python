lis=[10,20,30,40,50,60,70,80,90,100,101,102,103,104,105]
n=int(input())
def linear_search(lst, number):
    for i in range(len(lst)):
        if lst[i]==number:
            return i
    return -1

value_found= linear_search(lis,n)
if value_found==-1:
    print("Value not found")
else:
    print("Index is : ",value_found)
