# You are given an array of N integers and a single integer K. You need to find out if there is a subarray, which has the sum exactly as K.

test=int(input())
for i in range(test):
  l=list(map(int,input().split()))
  k=l[1]
  a=list(map(int,input().split()))
  sum=a[0]
  n=l[0]
  flag=False
  
# window={a[0]:1}
  start=0
  end=0

  while(start<n):
    if(sum<k):
      if(end>=n-1):
        break
      end=end+1
      sum=sum+a[end]

    elif(sum>k):
      sum=sum-a[start]
      start=start+1

    else:
      print("Yes")
      flag=True
      break

  if(flag==False):
    print("No")
    
