# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    
    n=len(arr)
    sum1=0
    sum2=0
    for i in range(0,n):
        for j in range(0,n):
            if i==j:
                sum1=sum1+arr[i][j]
    
    j=n-1
    for i in range(0,n):
        sum2=sum2+arr[i][j]
        j=j-1
    
    if(sum1>sum2):
        return sum1-sum2
    return sum2-sum1
