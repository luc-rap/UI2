import heapq
import sys
from numpy import random

pocet_pokusov = 1


# funkcia vygeneruje sachovnicu s danym rozmerom a naplni ju nulami
def postav_sachovnicu(n):
    sachovnica = [[0 for i in range(n)] for j in range(n)]
    return sachovnica


# funkcia skontroluje, ci kon nevychadza zo sachovnice
def skontroluj_krok(n, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True


# funkcie vypise sachovnicu na standardny vystup
def vypis_sachovnicu(sachovnica):
    for riadok in sachovnica:
        print(riadok)


# funkcia zisti pocet vsetkych policok, ktore sa daju z daneho policka navstivit
def najdi_susedov(sachovnica, x, y, n):
    zoznam_susedov = []
    riadok = [2, 1, -1, -2, -2, -1, 1, 2]
    stlpec = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):

        # vsetky kroky y aktualneho policka
        nove_X = x + riadok[i]
        nove_Y = y + stlpec[i]

        # zisti, ci nepresahuje von zo sachovnice a nebol navstiveny
        if (skontroluj_krok(n, nove_X, nove_Y)) is True and int(sachovnica[nove_X][nove_Y]) == 0:
            zoznam_susedov.append((nove_X, nove_Y))
    return zoznam_susedov


# funkcia pomocou Warnsdorffovej heuristiky a hladania do hlbky hlada cestu pre Eulerovho kona
def najdi_cestu(sachovnica, x, y, n, pocet_krokov):
    global pocet_pokusov

    pq = []

    sachovnica[x][y] = pocet_krokov

    # uspesne sme navstivili vsetky policka
    if pocet_krokov == n * n:
        print("nasli sme vysledok. pocet pokusov: ", pocet_pokusov)
        vypis_sachovnicu(sachovnica)
        return True

    # susedia pre konkretne policko
    susedia = najdi_susedov(sachovnica, x, y, n)

    kam_pojde = [None, None]

    # print("_______________")
    # pre kazdeho suseda vypocitame cenu podla toho, kolko policok sa da z neho navstivit
    for sused in susedia:
        pocet_susedov = len(najdi_susedov(sachovnica, sused[0], sused[1], n))
        # pocet vlozime do min heap spolu so suradnicami (ak je to tuple, zoradi podla prveho elementu)
        heapq.heappush(pq, (pocet_susedov, sused))

    # kym ma susedov
    while pq:
        # vezmeme suseda s najmensim poctom, vnori sa
        kam_pojde = pq[0]
        # vypocitame dalsie suradnice
        x, y = kam_pojde[1][0], kam_pojde[1][1]

        #vypis_sachovnicu(sachovnica)
        if pocet_pokusov >= 10000000:
            # ak hladame prilis dlho
            return False
        # rekurzivne vnaranie s novymi suradnicami
        if najdi_cestu(sachovnica, x, y, n, pocet_krokov + 1):
            return True
        else:
            # print("backtracking...")
            pocet_pokusov += 1
            # funkcia vrati false, ked uz nemal ziadnych susedov, takze vymaze predoslu moznost (pop) a skusi druhu najmensiu
            heapq.heappop(pq)
            # vynulujem policko
            sachovnica[x][y] = 0
    return False


# otestuje zvoleny pocet krat zvolenu sachovnicu s nahodnymi suradnicami
def test(n):
    global pocet_pokusov
    prvy_pokus = 0
    dalsi_pokus = 0
    nenaslo = 0
    pocet_testov = int(input("Zadajte pocet testov: "))
    for i in range(0, pocet_testov):

        sachovnica = postav_sachovnicu(n)
        x = random.randint(n)
        y = random.randint(n)
        pocet_krokov = 1
        print("Nahodne zvolene suradnice: " , x, y)
        vysledok = najdi_cestu(sachovnica, x, y, n, pocet_krokov)
        if not vysledok: # funkcia vrati False, ked sme nenasli riesenie, alebo pocet krokov presiahol limit
            print("Sachovnica nema riesenie, alebo velmi dlho hlada riesenie.")
            nenaslo += 1
        else:
            if pocet_pokusov == 1:
                prvy_pokus += 1
            else:
                dalsi_pokus += 1

        pocet_pokusov = 1

    print("Riesenie sme nasli na prvy pokus: ", prvy_pokus, "krat, co je ", round((prvy_pokus / pocet_testov)*100, 2), "%")
    print("Riesenie sme nasli pre opakovane pokusy: ", dalsi_pokus, "krat, co je ", round((dalsi_pokus / pocet_testov) * 100, 2), "%")
    vysledok = (nenaslo / pocet_testov) * 100
    print("Riesenie sme nenasli alebo trvalo velmi dlho: ", nenaslo, "krat, co je ", round(vysledok, 2),"%")


if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    try:
        n = int(input("Zadajte velkost sachovnice: "))
    except ValueError:
        print("Mozete zadat len cislo.")
    else:
        if n < 5 or n > 35:
            print("Min. velkost je 5 a max. je 35.")
        else:
            prepinac = input("Chcete zadat vlastne suradnice, alebo pustit test? [s] / [t] : ")
            if prepinac == 's':
                sachovnica = postav_sachovnicu(n)
                x = int(input("Zadajte 1. suradnicu kona (riadok): "))
                y = int(input("Zadajte 2. suradnicu kona (stlpec): "))
                pocet_krokov = 1
                vysledok = najdi_cestu(sachovnica, x, y, n, pocet_krokov)
                if not vysledok:
                    print("Sachovnica nema riesenie, alebo velmi dlho hlada riesenie.")
            elif prepinac == 't':
                test(n)
            else:
                print("Neznamy prepinac.")

