s1 = 'asdfg'
s2 = '123asd456'
s3 = []
for i in s1:
    s3 += i
for i in s2:
    if i in s3:
        continue
    else:
        s3 += i
for i in s3:
    print(i, end = ' ')
