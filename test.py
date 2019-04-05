from mygraph import Node
from mygraph import Graph

g = Graph()

g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')

g.add_edge('a', 'b', 7)
g.add_edge('a', 'c', 9)
g.add_edge('a', 'f', 14)
g.add_edge('b', 'c', 10)
g.add_edge('b', 'd', 15)
g.add_edge('c', 'd', 11)
g.add_edge('c', 'f', 2)
g.add_edge('d', 'e', 6)
g.add_edge('e', 'f', 9)

print("Nodes")
for n in g:
    print(g.nodes_dict[n.name])

print("Connections")
for n in g:
    for w in n.get_connections():
        print('( %s , %s, %3d)' % (n.id, w.id, n.get_weight(w)))
