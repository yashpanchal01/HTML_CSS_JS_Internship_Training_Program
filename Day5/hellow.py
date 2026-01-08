import copy
Numbers = [1, 2, 3, 4, 5, 6, 7]

box1 = [1, 2]
box2 = [3, 4]
a = [box1, box2]



c = a.copy()
b = copy.deepcopy(a)
print (c)
print (b)


