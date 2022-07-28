# Given a sorted array of integers, return indices of two numbers such that they add up to a target value.
# Print -1 -1 if not found.



test=int(input())
for x in range(test):
  l=list(map(int,input().split()))
  n=l[0]
  k=l[1]
  a=list(map(int,input().split()))
  i=0
  j=n-1
  while(i<j):
    sum=a[i]+a[j]
    if(sum>k):
      j=j-1
    elif(sum<k):
      i=i+1
    elif(sum==k):
      print(i,j)
      break
  
  if(i==j):
    print("-1 -1")
  
