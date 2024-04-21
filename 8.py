import numpy as np 
N=3

A = np.array([[1, 5, 1], [4, -1, 1], [1, 6, 52]])
B = np.array([24, 69, 291])


x = np.linalg.inv(A).dot(B)
print('')
print('X')
for i in range (0,N):
    print('%f'%x[i],end=' ')
print('')

x1 = np.linalg.solve(A,B)
print('')
print('X1')

for i in range (0,N):
    print('%f'%x1[i],end=' ')
print('')
print('\nDet(A)=%f'%np.linalg.det(A))
