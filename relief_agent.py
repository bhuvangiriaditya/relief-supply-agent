import networkx as nx
from statistics import mean


class ReliefAgent:
    def __init__(self):
        self.ukraine_graph = nx.Graph()
        self.nodes = ['Kiev', 'Kharkiv', 'Lviv', 'Mariupol', 'Mikolaive', 'Dnipro', 'Kherson', 'Odessa']
        self.ukraine_graph.add_nodes_from(self.nodes)
        self.edges = [('Kiev','Kharkiv',10),('Kharkiv','Odessa',7),('Odessa','Kiev',5),('Kiev','Lviv',17),('Lviv','Dnipro',4),('Dnipro','Odessa',25),('Lviv','Mikolaive',12),('Mikolaive','Keiv',15),('Lviv','Mariupol',2),('Lviv','Kherson',10),('Kherson','Dnipro',11)]
        self.ukraine_graph.add_weighted_edges_from(self.edges)

    def calculate_heuristic(self, start, goal):
        all_routes = list(nx.all_simple_paths(self.ukraine_graph, source=start, target=goal))
        all_routes_costs = []
        for route in all_routes:
            path_cost = 0
            for i in range(len(route) - 1):
                path_cost += self.ukraine_graph[route[i]][route[i+1]]['weight']
            all_routes_costs.append(path_cost)
        if all_routes_costs:
            return mean(all_routes_costs)
        else:
            return 0




dc=ReliefAgent()
start='Kiev'
goal='Kherson'
heuristic_cost = dc.calculate_heuristic(start=start, goal=goal)
print(start,goal,heuristic_cost)