#Frida Rangel
#A01651385
#Problema 3

import numpy as np

#sistema de ecuaciones del problema:

#0.25x + 0.45y +0.3z = 1.5
#0.15x + 0.5y +0.35z = 5
#0.75y +0.25z = 3

#resolver sistema de ecuaciones

A = np.array ([[0.25, 0.15, 0.0], [0.45, 0.5, 0.75], [0.3, 0.35, 0.25]])

#solución de cada ecuación
B = np.array ([1.5, 5, 3])

#resolver para x y z y comprobar después con regla de crammer

x, y, z = np.linalg.solve(A, B)
print((x, y, z))

#regla de cramer 
d = ((0.25*0.5*0.25) + (0.15*0.75*0.3) + (0.35*0.45*0)-((0*0.5*0.3) + (0.25*0.75*0.35) + (0.25*0.45*0.15))) 
x1 = ((1.5*0.5*0.25) + (5*0.35*0) + (3*0.15*0.75)-((3*0.5*0) + (1.5*0.35*0.75) + (5*0.15*0.25)))
y1 = ((0.25*5*0.25) + (0.45*3*0) + (0.3*1.5*0.75)-((0*5*0.3) + (0.25*3*0.75) + (0.45*1.5*0.25)))
z1 = ((0.25*0.5*3) + (0.45*0.35*1.5) + (0.3*0.15*5)-((0.3*0.5*1.5) + (0.25*0.35*5) + (3*0.45*0.15))) 

x = x1/d
y = y1/d
z = z1/d

#resultados de crammer

print(x)
print(y)
print(z)