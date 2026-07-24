n=[1,2,3,4,5]
target=3
seen={}
for i ,num in enumerate(n):
  diff=target-num
  if diff in seen:
    print(f"{diff}+{num}={target}")
    print(f"indicates:{seen[diff]},{i}")
    break
  seen[num]=i
