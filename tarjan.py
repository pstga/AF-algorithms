# punti si puncte critice intr un graf neorientat

def dfs(u, tata = -1):
    nonlocal adj
    nonlocal time
    nonlocal punti
    nonlocal puncte
    viz[u] = True
    idx[u] = low[u] = time
    time += 1
    copii = 0

    for v in adj[u]:
        if v == tata:
            continue
        if viz[v]:
            low[u] = min(low[u], idx[v])
        else:
            copii += 1
            dfs(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > idx[u]:
                punti.append((u, v))
            if tata != -1 and low[v] >= idx[u]:
                puncte.add(u)

    if tata == -1 and copii > 1:
        puncte.add(u)



if __name__ == '__main__':
    n, m = map(int, input().split())
    low = [-1] * (n+1)
    idx = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    viz = [False] * (n+1)
    puncte = set()
    punti = []
    time = 0
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    for i in range(1, n+1):
        if not viz[i]:
            dfs(i)

    print(punti, puncte)