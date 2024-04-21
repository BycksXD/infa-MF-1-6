A = [1, 2, 3, 0, -5, 6, 7, 0, -3]

NM = None
NZ = None

for i in range(len(A)):
    if A[i] < 0 and NM is None:
        NM = i + 1  
    if A[i] == 0 and NZ is None:
        NZ = i + 1  
    if NM is not None and NZ is not None:
        break

print("Массив A:", A)
print("Номер первого отрицательного элемента (NM):", NM)
print("Номер первого нулевого элемента (NZ):", NZ)
