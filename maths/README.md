# 🌀 3D Point Rotation in Python

Ce guide montre comment effectuer une **rotation 3D** d’un point en utilisant des **matrices de rotation** selon les axes X, Y et Z.

---

## 📌 Function to Rotate a Point

```python
def rotation_point(point, matrice_rotation, theta):
    point_vector = np.array(point)
    rotated_point = np.dot(matrice_rotation, point_vector)
    return rotated_point
```

## 🔁 Angle de rotation :
On défini _l'angle de rotation_ **Théta** suivant chaque axe.
```python
theta = np.radians(90)
```

## 🔄 Matrice Rotation :
### 🟥 Rotation X :
```python
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(theta), - np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
])
```

### 🟩 Rotation Y :

```python
rotation_y = np.array([
    [np.cos(theta), 0, np.sin(theta)],
    [0, 1, 0],
    [- np.sin(theta), 0, np.cos(theta)]
]) 
```

### 🟦 Rotation Z :
```python
rotation_z = np.array([
    [np.cos(theta), - np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
```

## 📚 Notes
- N'oublier pas d'importer numpy:
```python 
import numpy as np
```
- Les angles doivent être exprimés en radians pour les fonctions trigonométriques comme np.sin et np.cos.
- Vous pouvez appliquer différentes matrices de rotation en fonction de l'axe de rotation souhaité.
