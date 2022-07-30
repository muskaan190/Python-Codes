# You are given an array A of size N, and a number K. You have to find the sum of all the prime numbers in the array, whose value is strictly lesser than K.


def isPrime(n):
  if(n==1):
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  
  return True


tests=int(input())

for i in range(tests):
  sum=0
  size=int(input())
  arr=list(map(int,input().split()))
  k=int(input())

  for i in range(0,size):
    if((isPrime(arr[i])==True) and (arr[i]<k)):
      sum=sum+arr[i]
  print(sum)
