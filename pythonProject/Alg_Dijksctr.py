N = 8  # Количество вершин (исправлено с 6 на 8, так как матрица 8x8)
inf = 3000
w = [
    [0, 1, 2, inf, inf, inf, inf, inf],
    [1, 0, 1, 5, 2, inf, inf, inf],
    [2, 1, 0, 2, 1, 4, inf, inf],
    [inf, 5, 2, 0, 3, 7, 8, inf],
    [inf, 2, 1, 3, 0, 3, 7, inf],
    [inf, inf, 4, 6, 3, 0, 5, 2],
    [inf, inf, inf, 8, 7, 5, 0, 6],
    [inf, inf, inf, inf, inf, 2, 6, 0]
]

selected = [False] * N
dist = [inf] * N

start = int(input('Введите номер начальной точки: ')) - 1
dist[start] = 0
v = start
minDist = 0

while minDist < inf:
    selected[v] = True
    for j in range(N):
        if dist[v] + w[v][j] < dist[j]:  # Исправлено умножение на сложение
            dist[j] = dist[v] + w[v][j]

    minDist = inf  # Исправлено left0 на inf
    for j in range(N):
        if not selected[j] and dist[j] < minDist:
            minDist = dist[j]
            v = j

end = int(input('Введите номер конечной точки: ')) - 1
print('Длина пути:', dist[end])

# Восстановление пути
path = []
current = end
path.append(current + 1)

while current != start:
    for i in range(N):
        if i != current and dist[i] + w[i][current] == dist[current]:
            current = i
            path.append(current + 1)
            break

print('Путь в обратном порядке:')
print(' -> '.join(map(str, reversed(path))))