str = "Hello,Python"
suffix = "Python"
print (str.endswith(suffix,2))

nl = [1,2,5,3,5]

nl.append(4)
nl.insert(0,7)
nl.sort()

print (nl)

import numpy as np
a = np.repeat(np.arange(5).reshape([1,-1]),10,axis = 0)+10.0 
b = np.random.randint(5, size= a.shape)
c = np.argmin(a*b, axis=1)
b = np.zeros(a.shape)
b[np.arange(b.shape[0]), c] = 1
print (b)