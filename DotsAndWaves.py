# Print the required pattern, such that for all numbers in the range[1, N], including N, if the number is odd, print a single~, else print N * without space, on a new line
# For example, consider the value stored inN = 5. Therefore, the required output is
# ~
# *****
# ~
# *****
# ~



n=int(input())

for i in range(1,n+1):
  if(i%2==0):
    print("*"*n)
  else:
    print("~")
