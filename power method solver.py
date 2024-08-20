import numpy as np
Ar=np.array

#constants
mat=[
    [3,-2],
    [-2,0]
]
w=[1,1]
iterations=25
iter_every=5 #outputs

print("Performing the power method")
print("Matrix:")
print(mat)
print("Initial vector")
print(w)
print()

mat=Ar(mat)
w=Ar(w,dtype=np.float64)

def rayliegh(mat,w):
    return np.dot(mat@w,w)/np.dot(w,w)

for i in range(iterations):
    if i%iter_every==0:
        r=rayliegh(mat,w)
        print(f"iter: {i}, rayliegh: {r}, vector: {w}")
    
    w=mat@w
    w/=np.max(np.abs(w))

print()
print("Resulting rayliegh quotient (eigenvalue approximation):",rayliegh(mat,w))
print("Resulting vector:",w)
