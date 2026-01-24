# de mentionat ca aceasta constructie are nodurile notate de la 0 legit puteam sa scriu +1 de 2-3 ori in cod si era ok
# insa mi a fost lene; important e ca merge
# constructie arbore bazat pe lista de grade
def constructie(s, l, adj, n):
    for _ in range(n-2):
        k, t = l.pop(0), s[0]
        adj[k[1]].append(t[1])
        adj[t[1]].append(k[1])
        t[0] -= 1
        if t[0] == 1:
            s.pop(0)
            l.append(t)
        if t[0] < 0:
            return False
    first = l.pop(0)
    second = l.pop(0)
    adj[first[1]].append(second[1])
    adj[second[1]].append(first[1])
    return True

if __name__ == '__main__':
    s0 = [int(x) for x in input().split()]
    s = [[d, i] for i, d in enumerate(s0) if d != 1]
    l = [[d, i] for i, d in enumerate(s0) if d == 1]
    adj = {i: [] for i, d in enumerate(s0)}
    n = len(s0)

    if sum(s0) != 2*(len(s0)-1):
        print("nu e un arbore")
    elif sum(s0) % 2 == 1:
        print("nu e un graf")
    else:
        if not constructie(s, l, adj, n):
            print("nu e un arbore")
        else:
            print(adj)