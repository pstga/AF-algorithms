# sortare topologica
import heapq as hq

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = {i :[] for i in range(n+1)}
    topo = []
    pq = []
    indeg = [0] * (n+1)
    for _ in range (m):
        u, v = map(int, input().split())
        indeg[v] += 1
        adj[u].append(v)

    for k in range (1, n+1):
        if indeg[k] == 0:
            hq.heappush(pq, k)

    while pq:
        u = hq.heappop(pq)
        topo.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                hq.heappush(pq, v)

    print(topo)

