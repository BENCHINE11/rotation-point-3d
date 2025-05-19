import numpy as np

# Fonction Rotation :
def rotation_point(point, matrice_rotation):
    point_vector = np.array(point)
    rotated_point = np.dot(matrice_rotation, point_vector)
    return tuple (round(float(coord), 4) for coord in rotated_point)

# Angle Rotation
theta = np.radians(90)

# Point à Transformer
point = (1, 2, 5)

# Matrice Rotation suivant X
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(theta), - np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
])

print("Point", point ,"+ Rotation suivant X =", rotation_point(point, rotation_x))

# Matrice Rotation suivant Y
rotation_y = np.array([
    [np.cos(theta), 0, np.sin(theta)],
    [0, 1, 0],
    [- np.sin(theta), 0, np.cos(theta)]
])

print("Point", point ,"+ Rotation suivant Y =", rotation_point(point, rotation_y))

# Matrice Rotation suivant Z
rotation_z = np.array([
    [np.cos(theta), - np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
print("Point", point ,"+ Rotation suivant Z =", rotation_point(point, rotation_z))

