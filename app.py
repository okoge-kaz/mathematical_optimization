import networkx as nx  # type: ignore

# Exercise 1
Graph = nx.Graph()
Graph.add_nodes_from([0, 2, 3, 5, 7])
Graph.add_weighted_edges_from([(0, 2, 1), (0, 5, 4), (0, 7, 2), (2, 5, 1), (2, 3, 7), (5, 3, 1.5), (5, 7, 5), (3, 7, 6)])

print(nx.single_source_dijkstra_path(Graph, source=0, weight="weight"))  # {0: [0], 2: [0, 2], 5: [0, 2, 5], 7: [0, 7], 3: [0, 2, 5, 3]}
print(nx.single_source_bellman_ford_path_length(Graph, source=0, weight="weight"))  # {0: 0, 2: 1, 5: 2, 7: 2, 3: 3.5}

# Exercise 2
Graph2 = nx.DiGraph()
Graph2.add_nodes_from(["s", "1", "2", "3", "4", "5", "t"])

Graph2.add_edge("s", "1", capacity=3)
Graph2.add_edge("s", "3", capacity=1)
Graph2.add_edge("s", "4", capacity=2)

Graph2.add_edge("1", "2", capacity=2)
Graph2.add_edge("1", "3", capacity=2)

Graph2.add_edge("2", "t", capacity=1)

Graph2.add_edge("3", "2", capacity=4)
Graph2.add_edge("3", "t", capacity=2)
Graph2.add_edge("3", "5", capacity=2)

Graph2.add_edge("4", "3", capacity=2)
Graph2.add_edge("4", "5", capacity=1)

Graph2.add_edge("5", "t", capacity=2)

flow_value, flow_dict = nx.maximum_flow(Graph2, "s", "t")
print(flow_value)  # 5
print(flow_dict)  # {'s': {'1': 3, '3': 1, '4': 1}, '1': {'2': 1, '3': 2}, '2': {'t': 1}, '3': {'2': 0, 't': 2, '5': 2}, '4': {'3': 1, '5': 0}, '5': {'t': 2}, 't': {}}
