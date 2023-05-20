l1 = [1, 4, 7, 9, 0]
l2 = [1, 6, 8, 2, 3]
c1 = set()
c2 = set()
for c in l1:
    c1.add(c)
for c in l2:
    c2.add(c)
cf = c1.union(c2)
print(cf)