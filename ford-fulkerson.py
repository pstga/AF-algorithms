def ford_fulkerson(graf_original, sursa, destinatie):
    gf = [rand[:] for rand in graf_original]
    n = len(gf)
    flux_maxim = 0

    def gaseste_drum(s, t, parinte):
        vizitat = [False] * n
        stiva = [s]
        vizitat[s] = True

        while stiva:
            u = stiva.pop()
            for v in range(n):
                if not vizitat[v] and gf[u][v] > 0:
                    parinte[v] = u
                    vizitat[v] = True
                    if v == t: return True
                    stiva.append(v)
        return False

    parinte = [-1] * n
    while gaseste_drum(sursa, destinatie, parinte):

        flux_drum = float('inf')
        nod = destinatie
        while nod != sursa:
            u = parinte[nod]
            flux_drum = min(flux_drum, gf[u][nod])
            nod = u

        v = destinatie
        while v != sursa:
            u = parinte[v]
            gf[u][v] -= flux_drum
            gf[v][u] += flux_drum
            v = u

        flux_maxim += flux_drum

    return flux_maxim

# exemplu; n am mai scris main; i will in viitor
retea = [
    [0, 10, 10, 0],  # de la 0 la 1 (cap 10) și la 2 (cap 10)
    [0, 0, 2, 8],  # de la 1 la 2 (cap 2) și la 3 (cap 8)
    [0, 0, 0, 10],  # de la 2 la 3 (cap 10)
    [0, 0, 0, 0]  # destinația nu trimite nicăieri
]

rezultat = ford_fulkerson(retea, 0, 3)
print(f"Fluxul maxim calculat este: {rezultat}")