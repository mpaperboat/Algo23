class AdjacencyMatrix:
    def __init__(self,*a):
        if len(a)==1:
            v=a[0].vertices()
            e=a[0].edges()
        else:
            v=a[0]
            e=a[1]
        self.m=len(e)
        self.v=[0]*v if type(v)==type(int)else v;
        self.n=len(self.v)
        self.e=[[[] for i in range(self.n)] for x in range(self.n)]
        for i in e:
            self.e[i[0]][i[1]]+=[i]
    def vertices(self):
        return V;
    def edges(self):
        return [j for i in range(self.n) for j in self.outgoingEdges(i)]
    def outgoingEdges(self,v):
        return [j for i in self.e[v] for j in i]
    def incomingEdges(self,v):
        return [j for i in range(self.n) for j in self.e[i][v]]
    def addEdge(self,e):
        self.e[e[0]][e[1]]+=[e]
    def removeEdge(self,e):
        self.e[e[0][e[1]]]=[i for i in self.e[e[0][e[1]]] if i!=e]