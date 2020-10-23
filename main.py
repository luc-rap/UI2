import heapq
import sys

def postav_sachovnicu(n):
    sachovnica = [[0 for i in range(n)] for j in range(n)]
    for riadok in sachovnica:
        print(riadok)
    return sachovnica


def skontroluj_krok(n, x, y):  # pridat aj ze nie je visited?
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True


def vypis_sachovnicu(sachovnica):
    for riadok in sachovnica:
        print(riadok)


def najdi_susedov(sachovnica, x, y, n):
    # ak pocet krokov je 64 a vsetko je navstivene, nalsi sme riesenie?
    zoznam_susedov = []
    riadok = [2, 1, -1, -2, -2, -1, 1, 2]
    stlpec = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):

        # vsetky kroky y aktulaneho policka
        nove_X = x + riadok[i]
        nove_Y = y + stlpec[i]

        # zisti, ci nepresahuje von zo sachovnice
        if (skontroluj_krok(n, nove_X, nove_Y)) is True and int(sachovnica[nove_X][nove_Y]) == 0:  # a nebol navstiveny
            zoznam_susedov.append((nove_X, nove_Y))
            pocet = 0
    return zoznam_susedov

def najdi_cestu(sachovnica, x, y, n, pocet_krokov):
    sachovnica[x][y] = pocet_krokov
    if pocet_krokov == n * n:
        print("nasli sme vysledok")
        vypis_sachovnicu(sachovnica)
        exit()
        # return
        # vypis sachovnicu
    susedia = najdi_susedov(sachovnica, x, y, n)
    min_pocet_susedov = 8  # max hodnota
    pq = []
    kam_pojde = [None, None]
    print("_______________")

    for sused in susedia:
        pocet_susedov = len(najdi_susedov(sachovnica, sused[0], sused[1], n))
        heapq.heappush(pq, (pocet_susedov, sused)) # will sort by the first element of the tuple
    # kym ma susedov
    while pq:
        # vezme najlepsieho suseda, vnori sa
        kam_pojde = pq[0]
        x, y = kam_pojde[1][0], kam_pojde[1][1]
        vypis_sachovnicu(sachovnica)
        #vypis_sachovnicu(sachovnica)
        if najdi_cestu(sachovnica, x, y, n, pocet_krokov + 1):
            return True
        else:
            print("backtracking...")
            # funkcia vrati false, pretoze uz nemal ziadnych suedov, takze vymaze predoslu moznost a skusi druhu
            heapq.heappop(pq)
            sachovnica[x][y] = 0
    return False


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    n = int(input("Zadajte velkost sachovnice: "))
    sachovnica = postav_sachovnicu(n)
    x = int(input("Zadajte 1. suradnicu kona (riadok): "))
    y = int(input("Zadajte 2. suradnicu kona (stlpec): "))
    pocet_krokov = 1
    najdi_cestu(sachovnica, x, y, n, pocet_krokov)
