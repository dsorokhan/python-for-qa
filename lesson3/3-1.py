i = 0
a = []
while i <  1001:
    if i % 2 == 0 and i % 3 == 0:
        a.append(i)
    i = i + 1

b = [i for i in range(1000) if i % 2 == 0 and i  % 3 == 0]
c = filter(lambda i: i % 2 == 0 and i  % 3 == 0, range(1000))

print (a)
print (b)
print (c)
