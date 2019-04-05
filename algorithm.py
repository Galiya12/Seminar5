V = dict()
R = dict()
class algorithm():
    
    def __init__(self):
        pass

    def make_set(self,point):
        V[point] = point
        R[point] = 0

    def find(self,point):
        if V[point] != point:
            V[point] = self.find(V[point])
        return V[point]

    def union(self,point1,point2):
        r1 = self.find(point1)
        r2 = self.find(point2)
        if R[r1] > R[r2]:
            V[r2] = r1
        else:
            V[r1] = r2
            if R[r1] == R[r2]:
                R[r2] += 1

    def kruskal(self,graph):
        for vertice in graph['vertices']:
            self.make_set(vertice)      
        MSTree = set()
        edges = list(graph['edges'])
        edges.sort()                    
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if self.find(vertice1) != self.find(vertice2):
                self.union(vertice1, vertice2)
                MSTree.add(edge)
        return MSTree
