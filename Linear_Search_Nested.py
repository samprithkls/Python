lst=[1,3,8,[67,90,81,[100,4,21]],82]
key=int(input("Enter Key: "))
for i in range(len(lst)):
    if type(lst[i]) == list:
        for j in range(len(lst[i])):
            if(lst[i][j]==key):
                print(i,j)
                break
            elif type(lst[i][j])== list:
                for k in range(len(lst[i][j])):
                    if(lst[i][j][k]==key):
                        print(i,j,k)
                        exit
    if lst[i]==key:
            print(i)

