# You are given a sorted arrayAof sizeN, and another integerK
# You have to find if there exists a pair of integers with indexiandj, such thati != j, andA[i] - A[j] = k
# If such a pair exists, printYes, else printNo


test=int(input())
for i in range(test):
  a=list(map(int,input().split()))
  arr=list(map(int,input().split()))
  k=a[1]
  i=0
  j=a[0]-1
  flag=0
  
  for i in range(0,len(a)):
    diff=arr[j]-arr[i]
    if(diff>k):
      i=i+1
    elif(diff<k):
      j=j-1
    else:
      flag=1
      break
  
  
  if(flag==1):
    print("Yes")
  else:
    print("No")
  
