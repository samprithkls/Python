#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		lw=0
		hi=n-1
		while(lw<=hi):
		    mid=(lw+hi)//2
		    if(arr[mid]==k):
		        return mid
		    elif(k<arr[mid]):
		        hi=mid-1
		    else:
		        lw=mid+1
		return -1
		        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends