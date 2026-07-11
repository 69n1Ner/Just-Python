from itertools import *
from collections import *
for i,w in enumerate(product(sorted('АПОБЕД'),repeat=6),start=1):
    w=''.join(w)
    if i%2==0 and w[0]=="О" and list(Counter(w).values())==[1,1,1,1,1,1]:
        print(i,w)
