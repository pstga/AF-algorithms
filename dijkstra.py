# dijkstra n^2, fara minHeap
import heapq as hq

def dijkstra(e, d, tata):
    viz = [False] * (n + 1)
    for _ in range(n):
        u = -1
        min_dist = 999
        for i in range(1, n + 1):
            if not viz[i] and d[i] < min_dist:
                min_dist = d[i]
                u = i
        if u == -1:
            break
        viz[u] = True
        for edge in e:
            start, end, weight = edge
            if start == u:
                if d[u] + weight < d[end]:
                    d[end] = d[u] + weight
                    tata[end] = u

# dijkstra o(mlogn) cu minheap
def dijkstra_mh(adj, s, d, tata):
    pq = [(0, s)] # cost, nodul respectiv; d[i], i
    while pq:
        dist_u, u = hq.heappop(pq)

        if dist_u > d[u]:
            continue

        for edge in adj[u]:
            v, w = edge
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                tata[v] = u
                hq.heappush(pq, (d[v], v))

    return d, tata


if __name__ == '__main__':
    n, m = map(int, input().split())
    e = []
    adj = {i:[] for i in range(1, n + 1)}

    d = [999] * (n+1)
    tata = [0] * (n+1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        e.append([u, v, w])
        adj[u].append([v, w])
        adj[v].append([u, w])

    d[1] = 0
    dijkstra_mh(adj, 1, d, tata)
    print(d, tata)

