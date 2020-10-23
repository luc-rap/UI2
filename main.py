import heapq
pocet_krokov = 0
counter = 1
stack = []

def postav_sachovnicu(n):
    sachovnica = [[[0,0] for i in range(n)] for j in range(n)]
    for riadok in sachovnica:
        print(riadok)
    return sachovnica

def skontroluj_krok(n, x, y): # pridat aj ze nie je visited?
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

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
        if (skontroluj_krok(n, nove_X, nove_Y)) is True and sachovnica[nove_X][nove_Y][0] != 1: #a nebol navstiveny
            zoznam_susedov.append((nove_X, nove_Y))
            pocet = 0
    return zoznam_susedov


def pohyb(sachovnica, x, y, n):
    susedia = najdi_susedov(sachovnica, x, y, n)
    min_pocet_susedov = 8 # max hodnota
    kam_pojde = None
    pq = []
    print(susedia)
    print("_______________")
    for sused in susedia:
        #print(sused)
        pocet_susedov = len(najdi_susedov(sachovnica, sused[0], sused[1], n))
        heapq.heappush(pq, (pocet_susedov, sused)) # According to the example from the documentation, you can use tuples, and it will sort by the first element of the tuple
        #if pocet_susedov < min_pocet_susedov:
            #kam_pojde = sused
            #min_pocet_susedov = pocet_susedov
        #print(pocet_susedov)
    kam_pojde = heapq.heappop(pq)
    print(kam_pojde[1])
    return kam_pojde[1]




if __name__ == '__main__':
    n = int(input("Zadajte velkost sachovnice: "))
    sachovnica = postav_sachovnicu(n)
    x = int(input("Zadajte 1. suradnicu kona (riadok): "))
    y = int(input("Zadajte 2. suradnicu kona (stlpec): "))
    sachovnica[x][y][0] = 1
    sachovnica[x][y][1] = counter
    #for riadok in sachovnica:
        #print(riadok)
    pohyb(sachovnica, x, y, n)

