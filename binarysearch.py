def binary_search(arr,x):
   l=0
   r=len(arr)-1
   while(l<=r):
      mid=(l+r)//2
      if(arr[mid]==x):
         return mid
      elif(x<arr[mid]):
         r=mid-1
      elif(x>arr[mid]):
         l=mid+1
   return -1
array=[1,2,3,4,5,6,7,8,9,10]
a=7
print(binary_search(array,a))
b=15
print(binary_search(array,b))
