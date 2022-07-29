#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left


def count_substring(string, sub_string):
    name=[]
    for i in range(0,len(string)):
        for j in range(i,len(string)):
            name.append(string[i:j+1])
    
    count=0
    for i in name:
        if i==sub_string:
            count=count+1
    
    return count
