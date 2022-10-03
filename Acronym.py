
s = input('Enter full Name ')
s = s.rstrip()
s = s.lstrip()
l = s.split()
a = list()
a = str()
for x in l:
    a = a+str(x[0])
print(a)
