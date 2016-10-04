a = True
c1 = 0

while c1 <= 1 :
    c2 = 0
    b = True
    while c2 <= 1 :
        c3 = 0
        c = True
        while c3 <= 1 :
            d = (a or not b) and (c or not a)
            print (a,b,c,d)
            c3 = c3 + 1
            c = False
        c2 = c2 + 1
        b = False
    c1 = c1 + 1
    a = False


