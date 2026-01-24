def dfs(adj, n):
    viz[n] = 1
    for v in adj[n]:
        if viz[v] == 0:
            tata[v] = n
            d[v] = d[tata[v]] + 1
            if dfs(adj, v):
                return True
        elif v != tata[n]:
            return True
    viz[n] = 2
    return False

viz = []
d = []
tata = []
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
    d = [999999] * (n+1)
    tata = [0] * (n+1)
    viz = [0] * (n+1)
    d[1] = 0
    ciclu = False
    for i in range(1, n+1):
        if viz[i] == 0:
            if dfs(adj, i):
                ciclu = True
    print(ciclu)
    print(d, tata)
