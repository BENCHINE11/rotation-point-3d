# Computer Vision 

## Définir la fonction de rotation :
```python
def rotation_point(point, matrice_rotation, theta):
    point_vector = np.array(point)
    rotated_point = np.dot(matrice_rotation, point_vector)
    return rotated_point
```

## Angle de rotation :
On défini _l'angle de rotation_ **Théta** suivant chaque axe.
```python
theta = np.radians(90)
```

## Matrice Rotation suivant l'axe X :
```python
rotation_x = np.array([
    [1, 0, 0],
    [0, np.cos(theta), - np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
])
```

## Matrice Rotation suivant l'axe Y :
```python
rotation_y = np.array([
    [np.cos(theta), 0, np.sin(theta)],
    [0, 1, 0],
    [- np.sin(theta), 0, np.cos(theta)]
]) 
```

## Matrice Rotation suivant l'axe Z :
```python
rotation_z = np.array([
    [np.cos(theta), - np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
```

