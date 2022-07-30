# You are given a ciphered string, you have to decipher the string.
# For example, if the given string is "a2b1c2", then the deciphered string will be "aabcc".
# Note: The string contains only lower-case letters and numbers.



test=int(input())
for i in range(test):
  size=int(input())
  s=input()
  a=""
  for x in range(0,size,2):
    a=a+(s[x]*int(s[x+1]))

  print(a) 
