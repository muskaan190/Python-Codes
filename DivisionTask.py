# You are given a number N.
# Let’s say you derive a variablexwhich is equal to the floor of a number you get when 32 is divided by N.
# In case x is 0, printToo Low
# In case it is not possible to generate a valid number, print-1
# In all other cases, printx.


num=int(input())
if(num==0):
  print("-1")
else:  
  x=32//num

  if(x==0):
    print("Too Low")

  else:
    print(x)
