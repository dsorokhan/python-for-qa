n = 100

my_list = range(2,n+1,2)

my_list2 = []
for i in my_list:
    my_list2.append(i ** 2)

result_dict = dict(zip(my_list, my_list2))

print (result_dict)
