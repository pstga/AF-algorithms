# arbore partial de cost minim - sortare crescatoare in functie de cost

r = []
n, m = 0, 0

def init(u):
    r[u] = u

# def afis(u):
#    return r[u]

def unite(u, v):
    for k in range(n+1):
        if r[k] == r[v]:
            r[k] = r[u]

def kruskal(e):
    rez = []
    m = 0
    for edge in e:
        if r[edge[0]] != r[edge[1]]:
            rez.append(edge)
            m += 1
            unite(edge[0], edge[1])
            if m == n-1:
                break
    return rez

if __name__ == '__main__':
    n, m = map(int, input().split())
    e = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        e.append([u, v, w])
    e.sort(key=lambda x: x[2])
    r = [0] * (n+1)
    for i in range(1, n+1):
        init(i)
    print(kruskal(e))

