def var(l):
    mean=1.0*sum(l)/len(l)
    return sum([(mean-x)**2 for x in l])

print var([2, 2, -6, -6])
print var([-4, -4, 2])
print var([2, 2, 2])
print var([-6, -6, -4, -4])

