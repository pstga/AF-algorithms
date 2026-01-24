# drum minim de maxim k arcuri in graf orientat ponderat cu ponderi intregi

def bmf(e, d, tata):
    for k in range(n):
        for edge in e:
            u, v, w = edge
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                tata[v] = u


if __name__ == '__main__':
    n, m = map(int, input().split())
    e = []
    d = [999] * (n+1)
    tata = [0] * (n+1)
    for _ in range(m):
        u, v, w = map(int, input().split())
        e.append([u, v, w])

    d[1] = 0
    bmf(e, d, tata)
    print(d)
