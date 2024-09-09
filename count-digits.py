def count_digits(n):
    count=0
    while n>0:
        lastdigit=n%10
        count=count+1
        n=n//10
    print(count)
count_digits(5467)