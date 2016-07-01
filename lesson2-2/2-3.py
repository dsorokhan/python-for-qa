import collections

t = [1, 2, 3, 4, 4, 6, 2]

a = list(set(t))

s = [item for item, count in collections.Counter(t).items() if count > 1]

dif = list(set(a) - set(s))

print (dif)

