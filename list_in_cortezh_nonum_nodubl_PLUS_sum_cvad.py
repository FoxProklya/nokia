a = [i for i in input().split()]
k = []
s = 0
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


for i in a:
    if is_number(i) == True:
        
        s += float(i)**2
    else:
        if i in k:
            continue
        else:
            k += [i]
b = tuple(k)
print(b)
print(s)
