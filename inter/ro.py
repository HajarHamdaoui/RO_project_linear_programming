import matplotlib.pyplot as plt
import numpy as np

# Définir les inégalités (coefficients de la forme ax + by <= c)
coefficients = np.array([[3, 5, 15], [5, 2, 10]]) #efficient way to store coefficients for multiple equations.

# Définir les inégalités sous la forme ax + by >= c
#coefficients = np.array([[1, 1, -1], [-1, 1, 1]])

# Générer des valeurs de x pour le traçage
x = np.linspace(0, 10, 400)

# Liste pour stocker les points extrêmes
extreme_points = []

# Vérifier chaque paire d'inégalités pour trouver les points d'intersection
for i in range(len(coefficients)):
    for j in range(i + 1, len(coefficients)):
        a1, b1, c1 = coefficients[i]
        a2, b2, c2 = coefficients[j]
        
        # Calculer l'intersection des deux droites
        x_intersection = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
        y_intersection = (c1 - a1 * x_intersection) / b1
        
        # Vérifier si le point d'intersection est à l'intérieur des limites x et y
        if 0 <= x_intersection <= 10 and 0 <= y_intersection <= 10:
            extreme_points.append((x_intersection, y_intersection))

# Afficher les points extrêmes
print("Points extrêmes de la région admissible :")
for point in extreme_points:
    print(point)

# Tracer les inégalités
plt.figure(figsize=(8, 6))
for coef in coefficients:
    a, b, c = coef
    y = (c - a * x) / b
    plt.plot(x, y, label=f'{a}x + {b}y <= {c}')

# Fill the feasible region
y1 = np.minimum((coefficients[0, 2] - coefficients[0, 0] * x) / coefficients[0, 1],
                (coefficients[1, 2] - coefficients[1, 0] * x) / coefficients[1, 1])
plt.fill_between(x, 0, y1, alpha=0.2, color='gray', label='Feasible Region')


# Tracer les points extrêmes
extreme_x, extreme_y = zip(*extreme_points)
plt.plot(extreme_x, extreme_y, 'ro')  # Point rouge pour les points extrêmes
plt.title('Points Extrêmes de la Région Admissible')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.show()
