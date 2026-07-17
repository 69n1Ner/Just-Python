import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Функция добавления узла с автоматическим вычислением значения
def add_node_with_value(G, name, value=None):
    if value is None:
        value = 0  # или любая логика по умолчанию
    G.add_node(name, value=value)

# Функция добавления ребра с автоматическим созданием узлов
def add_flow(G, source, target, weight):
    G.add_edge(source, target, weight=weight)
    # Автоматически проставляем значения, если их нет
    if 'value' not in G.nodes[source]:
        G.nodes[source]['value'] = weight
    if 'value' not in G.nodes[target]:
        G.nodes[target]['value'] = weight

# Динамически строим граф
add_flow(G, "Вход", "Разделитель 1", 180)
add_flow(G, "Разделитель 1", "Линия А", 90)
add_flow(G, "Разделитель 1", "Линия Б", 90)

# Добавляем ещё один узел на лету
add_flow(G, "Линия А", "Потребитель 1", 50)
add_flow(G, "Линия А", "Потребитель 2", 40)

for n in G.nodes():
    print(n, G.nodes[n])

# Отрисовка
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='lightblue')
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

node_labels = {n: f"{n}\n({d.get('value', '?')})" for n, d in G.nodes(data=True)}
edge_labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.axis('off')
plt.show()