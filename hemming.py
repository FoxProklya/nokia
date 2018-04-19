a = int(input())
b = int(input())
count = 0
x = 0
a1 = str(a)
b1 = str(b)
if len(a1) == len(b1):
    for i in a1:
        for j in b1[x::]:
            if i != j:
               count += 1
            x += 1
            break
print(count)
