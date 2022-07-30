# You are given n numbers and you have to answer q queries. In each query, you will be provided with a number k and you have to find the first number which is greater than k.
# For instance, if there are 7 numbers 9,5,8,1,2,3,4 and k is 6, then there are 2 numbers greater than 6 => 8 and 9, but the first element greater than it is 8. So, print 8.
# In case there is no number greater than k in the array, print -1


n=int(input())
arr=list(map(int,input().split()))
lines=int(input())
for f in range(lines):
  x=int(input())
  arr.sort()
  i=0
  for q in range(len(arr)):
    if arr[i]<x:
      i=i+1
    elif arr[i]>x:
      print(arr[i])
      break
      
