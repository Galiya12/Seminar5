class Node:
    id_g = 0

    def __init__(self, node):
        self.id = Node.id_g
        Node.id_g += 1
        self.name = node
        self.adjacent = {}

    def __str__(self):
        return str(self.name) + ': ' + str([x.name for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.nodes_dict = {}
        self.num_nodes = 0

    def __iter__(self):
        return iter(self.nodes_dict.values())

    def add_node(self, node):
        if node in self.nodes_dict:
            return self.nodes_dict[node]
        else:
            self.num_nodes = self.num_nodes + 1
            new_node = Node(node)
            self.nodes_dict[node] = new_node
            return new_node

    def get_node(self, n):
        if n in self.nodes_dict:
            return self.nodes_dict[n]
        else:
            return None

    def remove_node(self, n):
        if n not in self.nodes_dict:
            return
        self.num_nodes -= 1
        del(self.nodes_dict[n])

    def add_edge(self, frm, to, cost=0):
        if frm not in self.nodes_dict:
            self.add_node(frm)
        if to not in self.nodes_dict:
            self.add_node(to)

        self.nodes_dict[frm].add_neighbor(self.nodes_dict[to], cost)
        # self.nodes_dict[to].add_neighbor(self.nodes_dict[frm], cost)

    def get_nodes(self):
        return self.nodes_dict.keys()
