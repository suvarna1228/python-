def armstrong_Numbers(n):
    a=n
    sum=0
    while n>0:
        lastdigit=n%10
        sum=sum+lastdigit*lastdigit*lastdigit
       
        n=n//10
    if (sum==a):
       print("the number is amstrong number")
    else:
        print("not a amstrong number") 
armstrong_Numbers(371) 
   