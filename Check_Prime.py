def Check_Prime(n):
    
    for i in range(2,n):
        if n%i==0:
            print("not prime")
        else:
            print(" prime")
Check_Prime(5)
