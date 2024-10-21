import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для моделювання транспортної мережі
city_graph = nx.Graph()

# Додаємо вузли, які представляють перехрестя
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
city_graph.add_nodes_from(nodes)


# Додаємо ребра, які представляють дороги між перехрестями
edges = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('C', 'E'), ('D', 'E'), 
         ('E', 'G'), ('F', 'G'), ('D', 'F'), ('B', 'F')]

city_graph.add_edges_from(edges)

# Виведення кількості вузлів та ребер у графі
print("Загальна кількість перехресть:", city_graph.number_of_nodes())
print("Загальна кількість доріг:", city_graph.number_of_edges())

# Обчислення кількості доріг, що з'єднують кожне перехрестя
intersection_degrees = {node: city_graph.degree(node) for node in city_graph.nodes()}
print("Кількість доріг на кожному перехресті:", intersection_degrees)

# Візуалізація транспортної мережі
layout = nx.spring_layout(city_graph)
nx.draw(city_graph, layout, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
nx.draw_networkx_edge_labels(city_graph, layout, edge_labels={(u, v): f"{u}-{v}" for u, v in city_graph.edges()})
plt.title("Модель транспортної системи")
plt.show()
