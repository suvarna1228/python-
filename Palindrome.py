def palidrome(n):
    revno=0
    while n>0:
        last_digit=n%10
        n=n//10
        revno=revno*10 + last_digit
    if revno==n:
       print("the number is palidrome")
    else:
        print("not a palidrome number") 
palidrome(5467)  