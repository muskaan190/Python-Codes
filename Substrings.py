# Substrings with K distinct letters
# Given string str of lowercase alphabets of length n and an integer K, the task is to count all substrings of length K which have exactly K distinct characters.

l=list(map(int,input().split()))
v=input()

start=0
end=0
k=l[1]
words={v[0]:1}
count=1
dis=0

while(start<len(v)):
  if(end-start+1<k): 
    end=end+1
    if(end>=len(v)):
      break
    if v[end] not in words:
      words[v[end]]=1
      count=count+1
    else:
      words[v[end]]=words[v[end]]+1
    
  else:
    words[v[start]]=words[v[start]]-1
    if words[v[start]]==0:
      words.pop(v[start],None)
      count=count-1
    start=start+1
  
  if(count==k and end-start+1==k):
    dis=dis+1
    # print(v[start:end+1])

print(dis)
