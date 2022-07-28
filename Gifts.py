# Given an array A of size n, which contains gift ids of various gifts kept in a row. You can select any subarray of gifts that contains all unique gift id.
# What is the longest sequence of successive gifts where each gift id is unique?

test=int(input())

for i in range(test):
  n=int(input())
  a=list(map(int,input().split()))
  start=0
  end=0
  count=0
  num={}
  z=[]
  while(start<=n):
  
  # print(num)
    if a[end] not in num:
      num[a[end]]=1
      count=count+1
      z.append(count)
      # if(count>=max):
        # max=count
      if(end>=n-1):
        break
      end=end+1

    else:
      num.pop(a[start],None)
      start=start+1
      count=count-1

    if(end>n):
      break

  

  # print(num)
  print(max(z))

