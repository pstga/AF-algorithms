# ctc in graf orientat

def dfs(adj, n):
    viz[n] = 1
    if n in adj:
        for v in adj[n]:
            if viz[v] == 0:
                dfs(adj, v)
    s.append(n)
    viz[n] = 2

def dfs2(adj, n):
    viz2[n] = 1
    s2.append(n)
    if n in adj:
        for v in adj[n]:
            if viz2[v] == 0:
                dfs2(adj, v)


viz = []   # nod vizitat sau nevizitat
viz2 = []  # viz pt transpusa
s = []     # stiva mea frumoasa pt parcurgereadoi
s2 = []    # stiva cu ctc
if __name__ == '__main__':
    adj = {}
    adj2 = {}
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
        # construim graful transpus odata ce citim muchiile guys !!
        if v not in adj2:
            adj2[v] = [u]
        else:
            adj2[v].append(u)
    viz = [0] * (n+1)
    viz2 = [0] * (n+1)
    for i in range(1, n+1):
        if viz[i] == 0:
            dfs(adj, i)
    s.reverse()
    for i in s:
        if viz2[i] == 0:
            s2 = []
            dfs2(adj2, i)
            print(s2, end = ' ')



