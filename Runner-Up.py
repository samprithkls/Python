"""

    Find the Runner-Up Score!
    https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

"""
n=int(input())
scores=list(map(int,input().split()))
maxi=scores[0]
runn=-1
for i in scores:
    if(i>maxi):
        maxi=i
for i in scores:
    if(i==maxi):
        continue
    else:
        if(i>runn):
            runn=i     
print(runn)
