import math

# Öklid mesafesi fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D uzayda noktalar listesi
points = [(1, 2), (3, 4), (6, 1), (7, 5), (4, 6)]

# Mesafeleri saklamak için bir liste
distances = []

# Mesafeleri hesaplamak için döngü
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        print(f"Mesafe {points[i]} ve {points[j]} arasında: {dist:.2f}")

# Minimum mesafenin bulunması
min_distance = min(distances)
print(f"En küçük mesafe: {min_distance:.2f}")
