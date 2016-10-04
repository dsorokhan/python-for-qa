mylist = [1,14,13,5]

i = 0
result_sum = 0

if len(mylist) != 0:

    while i < (len(mylist)):
        if mylist[i] != 13:
            result_sum = result_sum + mylist[i]
            i = i + 1
        else:
            break

print (result_sum)