def chebyshev_distance(p1, p2):
    """Calcule la distance de Chebyshev entre deux points.
#Deuxième methode
    
def chebyshev_distance(p1, p2):
    """Calcule la distance de Chebyshev entre deux points.

    Args:
        p1 (tuple): Coordonnées du premier point (x1, y1, z1, ...).
        p2 (tuple): Coordonnées du deuxième point (x2, y2, z2, ...).

    Returns:
        float: Distance de Chebyshev entre les deux points.
    """

    if len(p1) != len(p2):
        raise ValueError("Les deux points doivent avoir la même dimension.")

    differences = [abs(x - y) for x, y in zip(p1, p2)]
    distance = max(differences)

    return distance

# Exemple d'utilisation
point1 = (1, 2, 3)
point2 = (4, 5, 6)
distance = chebyshev_distance(point1, point2)
print("Chebyshev Distance:", distance)
