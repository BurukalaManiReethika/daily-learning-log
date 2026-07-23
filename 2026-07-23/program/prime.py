n=int(input("enter"))
if n>0:
    for i in range(5):
        if n%2==0:
            print("not prime")
        else:
            print("prime")
else:
    print("not prime")
