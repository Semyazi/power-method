import numpy as np
import random
Ar=np.array

# constants
R=4 # generates eigenvectors with entries in [-R,R]
MAX_E=14 # maximum entry of the output matrix
EP=0.000001 # epsilon
eigs=[-1,1,2,4] # eigenvals, choose your favourite numbers
mats=5 # how many matrices to generate

D=np.diagflat(eigs)
dim=len(eigs)

def gen_mtx():
    # keep going until we get a "nice" (with no fractions) matrix
    while True:
        eigv=[random.randint(-R,R) for _ in range(dim**2)]
        eigv=Ar(eigv).reshape((dim,dim))
        if np.abs(np.linalg.det(eigv))<EP: continue # ensure linear independence
        eigvi=np.linalg.inv(eigv)
        mat=eigv@D@eigvi

        good=True
        for i in range(dim**2):
            r=i//dim
            c=i%dim
            entry=mat[r,c]
            good_entry=(abs(round(entry)-entry))<EP
            if abs(round(entry))>MAX_E:
                good_entry=False
            if not good_entry:
                good=False
                break
            mat[r,c]=round(entry)
        if good:break

    return mat

print("--Matrices--")
for i in range(mats):
    print(gen_mtx())
