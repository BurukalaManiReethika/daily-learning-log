n=int(input("enter"))
temp=n
count=0
while temp>0:
    temp=temp//10
    count+=1
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**count
    temp=temp//10
if n==sum:
    print("armstrong")
else:
    print("not armstrong")
