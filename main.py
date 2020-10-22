import numpy as np
import sys


pocet_krokov = 0

stack = []

def postav_sachovnicu(n):
    sachovnica = [[0 for i in range(n)] for j in range(n)]
    for riadok in sachovnica:
        print(riadok)
    return sachovnica

def skontroluj_krok(n, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    return True

def najdi_cestu(sachovnica, x, y, n):
    # ak pocet krokov je 64 a vsetko je navstivene, nalsi sme riesenie?
    riadok = [2, 1, -1, -2, -2, -1, 1, 2, 2]
    stlpec = [1, 2, 2, 1, -1, -2, -2, -1, 1]
    for i in range(9):
        # vsetky kroky y aktulaneho policka
        cestaX = x + riadok[i]
        cestaY = y + stlpec[i]
        # zisti, ci nepresahuje von zo sachovnice
        if (skontroluj_krok(n, cestaX, cestaY)) is True: #a nebol navstiveny
            print(cestaX, cestaY)
            pocet = 0
            # ak je to valid move, ziskam pocet krokov, ktore viem z toho policka urobim
            for j in range(9):
                childNodesX = cestaX + riadok[j]
                childNodesY = cestaY + stlpec[j]
                if (skontroluj_krok(n, childNodesX, childNodesY)) is True:
                    pocet += 1
                # vyber minimum x,y, pop
                # sachovnica[minx][miny] = counter
                # najdi cestu
                # inak nastav na miesto nulu, chod spat a zober druhe minimum (backtracking)
            print(pocet)




if __name__ == '__main__':
    n = int(input("Zadajte velkost sachovnice: "))
    sachovnica = postav_sachovnicu(n)
    x = int(input("Zadajte 1. suradnicu kona (riadok): "))
    y = int(input("Zadajte 2. suradnicu kona (stlpec): "))
    sachovnica[x][y] = [1, 'visited']
    for riadok in sachovnica:
        print(riadok)
    najdi_cestu(sachovnica, x, y, n)

