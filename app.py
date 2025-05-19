import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fonction pour appliquer la rotation
def rotation_point(point, matrice_rotation):
    point_vector = np.array(point)
    rotated_point = np.dot(matrice_rotation, point_vector)
    return tuple(round(float(coord), 4) for coord in rotated_point)

# Titre de l'application
st.title("Rotation 3D d'un point autour d'un axe")

# Entrée utilisateur pour les coordonnées du point
x = st.number_input("Coordonnée X", value=1.0)
y = st.number_input("Coordonnée Y", value=2.0)
z = st.number_input("Coordonnée Z", value=5.0)
point = (x, y, z)

# Sélection de l'axe de rotation
axe = st.selectbox("Axe de rotation", ["X", "Y", "Z"])

# Entrée de l'angle
angle_deg = st.slider("Angle de rotation (en degrés)", min_value=0, max_value=360, value=90)
theta = np.radians(angle_deg)

# Définition des matrices de rotation
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(theta), -np.sin(theta)],
    [0, np.sin(theta),  np.cos(theta)]
])

rotation_y = np.array([
    [np.cos(theta), 0, np.sin(theta)],
    [0, 1, 0],
    [-np.sin(theta), 0, np.cos(theta)]
])

rotation_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Choisir la bonne matrice
if axe == "X":
    result = rotation_point(point, rotation_x)
elif axe == "Y":
    result = rotation_point(point, rotation_y)
else:
    result = rotation_point(point, rotation_z)

# Affichage du résultat
st.write(f"Point initial : {point}")
st.write(f"Point après rotation autour de l'axe {axe} de {angle_deg}° : {result}")

# Affichage 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tracer le point original
ax.scatter(*point, color='blue', label='Original')
ax.text(*point, "Origine", color='blue')

# Tracer le point après rotation
ax.scatter(*result, color='red', label='Rotated')
ax.text(*result, "Roté", color='red')

# Configurer l'affichage
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title("Visualisation 3D de la rotation")

# Ajuster l'échelle des axes
arr = np.array([point, result])
max_range = np.ptp(arr, axis=0).max()
mid_x = (point[0] + result[0]) / 2
mid_y = (point[1] + result[1]) / 2
mid_z = (point[2] + result[2]) / 2

ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

# Afficher dans Streamlit
st.pyplot(fig)