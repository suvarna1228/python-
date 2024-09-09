def revnum(n):
    revno=0
    while n>0:
        last_digit=n%10
        n=n//10
        revno=revno*10 + last_digit
    print(revno)
revnum(5467)            
       