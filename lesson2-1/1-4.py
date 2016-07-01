import string
a = 'asdasd ASJAD HI hi Hi'

b = a.lower()

count = 0
for i in range(len(b) - 1):
    count += b[i] == 'h' and b[i + 1] == 'i'

d = b.replace ('hi', 'bye')
print (count)
print (d)