# Given an array A of size n with positive numbers, find the total number of subarrays that have sum < m.
# Time Complexity---O(n)

test=int(input())
for i in range(test):
  l=list(map(int,input().split()))
  k=l[1]
  a=list(map(int,input().split()))
  sum=a[0]
  n=l[0]
  count=1
  
# window={a[0]:1}
  start=0
  end=0

  while(start<=n):
    if(sum<k):
      count=count+1
      if(end>=n-1):
        break
      end=end+1
      sum=sum+a[end]
      

    elif(sum>k):
      sum=sum-a[start]
      start=start+1

    else:
      # print("Yes")
      break

    if(end>=n-1):
      # print("No")
      break

  print(count)  
