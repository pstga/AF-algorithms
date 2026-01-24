# constructie / verificare graf bazat pe lista de grade

def hhkm(s0): # returneaza doar daca am sau nu graf cu acea secventa de grade
    s0 = [ x for x in s0 if x >0]
    while s0:
        s0 = sorted(s0, reverse=True)
        d = s0.pop(0)
        if d > len(s0):
            return False
        for i in range(d):
            s0[i] = s0[i]-1
            if s0[i] < 0:
                return False
    return True

def hhkm_graf(s): # imi construieste o lista de adiacenta a grafului meu; folosesc si indexul nodului
    adj = { i: [] for i in range(len(s))}
    while True:
        s.sort(key = lambda x: x[0]) # le sortez dupa grad
        s = [x for x in s if x[0] > 0]
        if not s: break

        d, id = s.pop(0)
        if d > len(s):
            return False
        for i in range(d):
            s[i][0] -= 1
            if s[i][0] < 0:
                return False
            adj[id+1].append(s[i][1]+1)
            adj[s[i][1]+1].append(id+1)
    return adj


if __name__ == "__main__":
    s0 = [int(x) for x in input().split()]
    s = [[d, i] for i, d in enumerate(s0)]

    if sum(s0) % 2 == 1:
        print('nuuu')
    else:
        print(hhkm_graf(s))
# pentru a tine minte si nodul, folosim structura de date tuple(grad, nod)
