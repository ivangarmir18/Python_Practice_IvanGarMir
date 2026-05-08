import numpy as np

datos = [(1, 2), (2, 1), (2, 3), (1, 3), (8, 8), (9, 7), (8, 9), (9, 8)]
centroide_A = (0, 0)
centroide_B = (5, 5)

def d_euclideana(x1, x2, y1, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

def k_means(puntos, c_a, c_b):
    while True:

        grupo_a = []
        grupo_b = []
        
        for d in puntos:
            dist_a = d_euclideana(c_a[0], d[0], c_a[1], d[1])
            dist_b = d_euclideana(c_b[0], d[0], c_b[1], d[1])
            
            if dist_a < dist_b:
                grupo_a.append(d)
            else: 
                grupo_b.append(d)

        nueva_pos_a = (np.mean([p[0] for p in grupo_a]), np.mean([p[1] for p in grupo_a]))
        nueva_pos_b = (np.mean([p[0] for p in grupo_b]), np.mean([p[1] for p in grupo_b]))
        
        if c_a == nueva_pos_a and c_b == nueva_pos_b:
            break

        c_a = nueva_pos_a
        c_b = nueva_pos_b

    return f"Final A: {c_a} con puntos {grupo_a}\nFinal B: {c_b} con puntos {grupo_b}"

print(k_means(datos, centroide_A, centroide_B))