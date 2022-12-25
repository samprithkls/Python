def printer(arr: list):
    print('\n') 
    for i in range (len(arr)):
        print(arr[i])

    N = int(input()) 
    check=0
    arr=[]
    while(check<N):
        flg=input()
        check+=1
        if(flg==insert):
            insert:arr.insert(input(), input())
        elif(flg==print):
            print:printer(arr)
        elif(flg==remove):
            remove:arr.remove(input())
        elif(flg==append):
            append:arr.append(input())
        elif(flg==pop):
            pop:arr.pop()
        elif(flg==reverse):
            reverse:arr.reverse()
        else:
            printer(arr)