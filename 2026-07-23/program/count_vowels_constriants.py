n="mani"
v=0
c=0
for ch in n:
    if ch in "aioeu":
        v+=1
    else:
        c+=1
print(v) 
print(c)
