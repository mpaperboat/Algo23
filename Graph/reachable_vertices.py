def reachable_vertices(g,v,f=[]):
    s=[v]
    if f==[]:
        f=[0]*g.n
    r=[]
    while s:
        u=s[-1]
        s.pop(-1)
        if f[u]==1:
            continue
        r.append(u)
        f[u]=1
        for e in g.outgoing_edges(u):
            s.append(e[1])
    return r