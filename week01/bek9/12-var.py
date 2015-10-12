# memory
v1 = 3
v2 = 3
print(v1 is v2) # a, b 메모리 같음

# tuple
a, b = 'python', 'life'
(c, d) = ('python', 'life')
print((a, b), (c, d)) # ('python', 'life') ('python', 'life')

# list
[e, f] = ['python', 'life']
print([e, f]) # ['python', 'life']

# duplication
g = h = 'python'
print(g, h) # python python

# change
a, b = b, a
print(a, b) # life python

# copy list
li = [1, 2, 3] 
li2 = li[:] # use slicing
li[1] = 4
print(li, li2) # [1, 4, 3] [1, 2, 3]

from copy import copy # load moduled
li3 = copy(li2)
print(li3 is li2) # False