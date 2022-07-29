# You are given a number stored in a variable with the namenum
# Check if the number is a prime number or not
# If  the value stored innum, is a prime number printYes, else printNo


num=int(input())
count=0
if(num==1 and num==0):
  print("No")

else:
  for i in range(2,num):
    if(num%i)==0:
      count=count+1
      
    
if(count>0):
  print("No")
else:
  print("Yes")
