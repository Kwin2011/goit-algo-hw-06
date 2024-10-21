import networkx as nx
import heapq

# Створення графа з вагами для транспортної системи міста
city_graph = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
city_graph.add_nodes_from(nodes)

# Додаємо ребра з вагами (ваги можуть означати відстані або час у дорозі)
weighted_edges = [
    ('A', 'B', 3), ('A', 'D', 2), ('B', 'C', 5), 
    ('C', 'E', 6), ('D', 'E', 1), ('E', 'G', 2), 
    ('F', 'G', 1), ('D', 'F', 4), ('B', 'F', 3)
]
city_graph.add_weighted_edges_from(weighted_edges)

# Реалізація алгоритму Дейкстри для пошуку найкоротших шляхів з заданого вузла
def dijkstra(graph, start):
    # Пріоритетна черга для вибору вершин з найменшою відстанню
    priority_queue = []
    # Ініціалізація відстаней як нескінченність для всіх вузлів
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        # Вибираємо вузол з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо, якщо знайдений шлях довший, ніж уже відомий
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідніх вузлів
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']
            distance = current_distance + weight

            # Якщо новий шлях коротший, оновлюємо значення
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Обчислення найкоротших шляхів від кожного вузла
for start_node in nodes:
    shortest_paths = dijkstra(city_graph, start_node)
    print(f"Найкоротші шляхи з {start_node}: {shortest_paths}")
