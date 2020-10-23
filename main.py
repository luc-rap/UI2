
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
    stack = []
    riadok = [2, 1, -1, -2, -2, -1, 1, 2]
    stlpec = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):

        # vsetky kroky y aktulaneho policka
        nove_X = x + riadok[i]
        nove_Y = y + stlpec[i]

        # zisti, ci nepresahuje von zo sachovnice
        if (skontroluj_krok(n, nove_X, nove_Y)) is True and sachovnica[nove_X][nove_Y][0] != 1: #a nebol navstiveny
            stack.append((nove_X, nove_Y))
            pocet = 0
    return stack


def pohyb(sachovnica, x, y, n):
    susedia = najdi_susedov(sachovnica, x, y, n)
    print(susedia)
    print("_______________")
    for sused in susedia:
        pocet_susedov = najdi_susedov(sachovnica, sused[0], sused[1], n)
        print(pocet_susedov)




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

