# You are given a string of size N. You have to convert the string into its cipher form.
# For example, the cipher form of a string "aabccd", will be "a2b1c2d1". The new generated string contains the characters, and the count of their occurrences in a consecutive manner.
# Note: The string contains only lower-case characters.


test=int(input())
for x in range(test):
  size=int(input())
  s=input()
  s=s+str(9)
  i=1
  count=1
  arr=""
  for x in range(1,len(s)):
    if(s[x-1]==s[x]):
      count+=1
    else:
      arr=arr+s[x-1]+str(count)
      count=1
    

  print(arr)
