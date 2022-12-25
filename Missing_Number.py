"""

    Missing Number
    https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1

"""


class Solution:
    def MissingNumber(self,a,n):
        a.sort()
        for i in range(0,n):
            if a[i]==i+1:
                continue
            else:
                return i+1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends