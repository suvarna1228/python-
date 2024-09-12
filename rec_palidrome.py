def palidrome(s,start,end):
    if start>=end:
        return True
    if s[start]!=s[end]:
        return False
    return palidrome(s,start+1,end-1)
s="madam"
print(palidrome(s,0,len(s)-1))