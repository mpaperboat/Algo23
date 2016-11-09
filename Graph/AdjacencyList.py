class AdjacencyList:
    def __init__(self,*a):
        if len(a)==1:
            v=a[0].vertices()
            e=a[0].edges()
        else:
            v=a[0]
            e=a[1]
        self.m=len(e)
        self.v=[0]*v if type(v)==int else v;
        self.n=len(self.v)
        self.e=[[] for i in range(self.n)]
        for i in e:
            self.e[i[0]]+=[i]
    def vertices(self):
        return self.v;
    def edges(self):
        return [j for i in range(self.n) for j in self.e[i]]
    def outgoing_edges(self,v):
        return self.e[v]
    def incoming_edges(self,v):
        return [j for i in range(self.n) for j in self.e[i] if j[1]==v]
    def add_edge(self,e):
        self.e[e[0]]+=[e]
    def remove_edge(self,e):
        self.e[e[0]]=[i for i in self.e[e[0]] if i!=e]