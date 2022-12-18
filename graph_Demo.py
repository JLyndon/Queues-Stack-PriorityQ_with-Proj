# >>> from graph import City, load_graph

# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)

# >>> nodes["london"]
# City(
#     name='City of London',
#     country='England',
#     year=None,
#     latitude=51.507222,
#     longitude=-0.1275
# )

# >>> print(graph)
# Graph with 70 nodes and 137 edges

# ------------------ PART II---------------

# >>> for neighbor in graph.neighbors(nodes["london"]):
# ...     print(neighbor.name)
# ...

# ------------------ PART III---------------

# >>> for neighbor, weights in graph[nodes["london"]].items():
# ...     print(weights["distance"], neighbor.name)
# ...

# ------------------ PART IV---------------

# >>> def sort_by(neighbors, strategy):
# ...     return sorted(neighbors.items(), key=lambda item: strategy(item[1]))
# ...
# >>> def by_distance(weights):
# ...     return float(weights["distance"])
# ...
# >>> for neighbor, weights in sort_by(graph[nodes["london"]], by_distance):
# ...     print(f"{weights['distance']:>3} miles, {neighbor.name}")
# ...

# ------------------ PART V---------------

# >>> import networkx as nx
# >>> from graph import City, load_graph

# >>> def is_twentieth_century(year):
# ...     return year and 1901 <= year <= 2000
# ...
# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)
# >>> for node in nx.bfs_tree(graph, nodes["edinburgh"]):
# ...     print("📍", node.name)
# ...     if is_twentieth_century(node.year):
# ...         print("Found:", node.name, node.year)
# ...         break
# ... else:
# ...     print("Not found")
# ...

# ------------------ PART VI---------------

# >>> def order(neighbors):
# ...     def by_latitude(city):
# ...         return city.latitude
# ...     return iter(sorted(neighbors, key=by_latitude, reverse=True))

# >>> for node in nx.bfs_tree(graph, nodes["edinburgh"], sort_neighbors=order):
# ...     print("📍", node.name)
# ...     if is_twentieth_century(node.year):
# ...         print("Found:", node.name, node.year)
# ...         break
# ... else:
# ...     print("Not found")
# ...

# ------------------ PART VII---------------

# >>> from graph import (
# ...     City,
# ...     load_graph,
# ...     breadth_first_traverse,
# ...     breadth_first_search as bfs,
# ... )

# >>> def is_twentieth_century(city):
# ...     return city.year and 1901 <= city.year <= 2000

# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)
# >>> city = bfs(graph, nodes["edinburgh"], is_twentieth_century)
# >>> city.name
# 'Lancaster'

# >>> for city in breadth_first_traverse(graph, nodes["edinburgh"]):
# ...     print(city.name)
# ...

# ------------------ PART VIII---------------

# >>> import networkx as nx
# >>> from graph import City, load_graph

# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)

# >>> city1 = nodes["aberdeen"]
# >>> city2 = nodes["perth"]

# >>> for i, path in enumerate(nx.all_shortest_paths(graph, city1, city2), 1):
# ...     print(f"{i}.", " → ".join(city.name for city in path))

# ------------------ PART IX---------------

# >>> from graph import shortest_path

# >>> " → ".join(city.name for city in shortest_path(graph, city1, city2))
# 'Aberdeen → Dundee → Perth'

# >>> def by_latitude(city):
# ...     return -city.latitude
# ...
# >>> " → ".join(
# ...     city.name
# ...     for city in shortest_path(graph, city1, city2, by_latitude)
# ... )

# ------------------ PART X---------------

# >>> from graph import connected
# >>> connected(graph, nodes["belfast"], nodes["glasgow"])
# False
# >>> connected(graph, nodes["belfast"], nodes["derry"])
# True

# ------------------ PART XI---------------

# >>> import networkx as nx
# >>> from graph import City, load_graph

# >>> def is_twentieth_century(year):
# ...     return year and 1901 <= year <= 2000
# ...
# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)
# >>> for node in nx.dfs_tree(graph, nodes["edinburgh"]):
# ...     print("📍", node.name)
# ...     if is_twentieth_century(node.year):
# ...         print("Found:", node.name, node.year)
# ...         break
# ... else:
# ...     print("Not found")
# ...
# 📍 Edinburgh
# 📍 Dundee
# 📍 Aberdeen
# 📍 Inverness
# 📍 Perth
# 📍 Stirling
# 📍 Glasgow
# 📍 Carlisle
# 📍 Lancaster
# Found: Lancaster 1937

# ------------------ PART XII---------------

# >>> from graph import (
# ...     City,
# ...     load_graph,
# ...     depth_first_traverse,
# ...     depth_first_search as dfs,
# ... )

# >>> def is_twentieth_century(city):
# ...     return city.year and 1901 <= city.year <= 2000
# ...
# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)
# >>> city = dfs(graph, nodes["edinburgh"], is_twentieth_century)
# >>> city.name
# 'Lancaster'

# >>> for city in depth_first_traverse(graph, nodes["edinburgh"]):
# ...     print(city.name)
# ...

# ------------------ PART XIII---------------

# >>> import networkx as nx
# >>> from graph import City, load_graph, dijkstra_shortest_path

# >>> nodes, graph = load_graph("roadmap.dot", City.from_dict)

# >>> city1 = nodes["london"]
# >>> city2 = nodes["edinburgh"]

# >>> def distance(weights):
# ...     return float(weights["distance"])
# ...
# >>> for city in dijkstra_shortest_path(graph, city1, city2, distance):
# ...     print(city.name)
# ...



# >>> def weight(node1, node2, weights):
# ...     return distance(weights)
# ...
# >>> for city in nx.dijkstra_path(graph, city1, city2, weight):
# ...     print(city.name)
# ...




