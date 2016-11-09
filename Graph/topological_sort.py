def topological_sort(g):
    r=[]
    d=[len(g.incoming_edges(i)) for i in range(g.n)]
    q=[i for i in range(g.n) if d[i]==0]
    while len(q):
        v=q[0]
        q.pop(0)
        r+=[v]
        for e in g.outgoing_edges(v):
            d[e[1]]-=1
            if d[e[1]]==0:
                q.append(e[1])
    return r
