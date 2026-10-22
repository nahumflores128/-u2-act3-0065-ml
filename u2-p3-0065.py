# Nahum flores Nc 0065 fecha 22 de octubre 2026
import numpy as np

# Arreglo de una dimensión
n0065 = np.array([10, 20, 30, 40, 50])

print(n0065)
print(n0065[0])
print(n0065[3])
print(n0065[-1])
print(n0065[-2])

print("-----------------------------------")

# Arreglo de dos dimensiones (2x3)
n0065 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(n0065)
print(n0065[0, 0])
print(n0065[1, 2])
print(n0065[-1, -1])
print(n0065[-2, -2])

print("-----------------------------------")
# Arreglo de tres dimensiones (2x2x3)
n0065 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0065)
print(n0065[0, 0, 0])
print(n0065[1, 1, 2])
print(n0065[-1, -1, -2])