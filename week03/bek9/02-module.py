# load module
import mod1 # have to use same directory

print(mod1.sum(3, 4)) # 7
print(mod1.safe_sum(4, 'a')) # error

# load function
from mod1 import sum

print(sum(3, 5)) # 8

from mod1 import sum, safe_sum
from mod1 import *

# load var, class
import mod2

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI, 4.4))

from mod2 import Math, PI
b = Math()
print(b, PI)

# another directory module
import sys
# sys.path.append("directory")