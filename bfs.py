def bfs(adj, n):
    viz[n] = 1
    q = [n]
    while q:
        n = q.pop(0)
        for v in adj[n]:
            if viz[v] == 0:
                viz[v] = 1
                tata[v] = n
                d[v] = d[tata[v]] + 1
                q.append(v)

q=[]
viz=[]
d=[]
tata=[]
if __name__ == '__main__':
    adj = {}
    n, m = input().split()
    n = int(n)
    m = int(m)
    for _ in range(m):
        u, v = input().split()
        u = int(u)
        v = int(v)
        if u not in adj:
            adj[u] = [v]
        else:
            adj[u].append(v)
        if v not in adj:
            adj[v] = [u]
        else:
            adj[v].append(u)
    q = []
    viz = [0] * (n+1)
    d = [999999] * (n+1)
    tata = [0] * (n+1)
    d[1] = 0
    bfs(adj, 1)
    print (tata[1:]) # vectorul de tati
    print(d[3]) # distanta de la nodul 1 la nodul 3
    