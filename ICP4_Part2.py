import numpy as np
random_array = np.random.randint(0,20, size=15)
print(random_array)
a= random_array.flatten()
counts = np.bincount(a)
print (np.argmax(counts, axis=0))
