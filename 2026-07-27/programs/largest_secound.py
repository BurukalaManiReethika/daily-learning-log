n=[1,2,3,4,5,55]
large=secound=float('-inf')
for i in n:
    if i>large:
        secound=large
        large=i
    elif i>secound and i!=large:
        secound=i
print(large)
print(secound)
output:55
5

=== Code Execution Successful ===
