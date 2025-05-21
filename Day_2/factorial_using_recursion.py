def fact(n):
    if n==0 | n==1:
        return 1
    else:
        return n*fact(n-1)
    number=int(input("enter a number"))
    print(f"the factoiral of {number} is:{fact(number)}")
    