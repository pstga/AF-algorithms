import heapq as hq
def topo_sort(adj, indeg, pq):
    topo = []

    while pq:
        u = hq.heappop(pq)
        topo.append(u)
        for fin in adj[u]:
            v, w = fin
            indeg[v] -= 1
            if indeg[v] == 0:
                hq.heappush(pq, v)
    return topo

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = {i : [] for i in range(1, n+ 1)}
    d = [999] * (n+1)
    tata = [0] * (n+1)
    indeg = [0] * (n + 1)
    pq = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        indeg[v] += 1
        adj[u].append([v, w])

    for k in range(1, n+1):
        if indeg[k] == 0:
            hq.heappush(pq, k)
    d[1] = 0
    topo = topo_sort(adj, indeg, pq)
    for u in topo:
        for fin in adj[u]:
            v, w = fin
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                tata[v] = u
    print(d, tata)