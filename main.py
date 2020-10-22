import numpy as np
import sys

riadok = [2, 1, -1, -2, -2, -1, 1, 2, 2]
stlpec = [1, 2, 2, 1, -1, -2, -2, -1, 1]

stack = []

def postav_sachovnicu(n):
    sachovnica = [[0 for i in range(n)] for j in range(n)]
    for riadok in sachovnica:
        print(riadok)
    return sachovnica




if __name__ == '__main__':
    n = input("Zadajte velkost sachovnice: ")
    sachovnica = postav_sachovnicu(int(n))
    x = int(input("Zadajte 1. suradnicu kona (riadok): "))
    y = int(input("Zadajte 2. suradnicu kona (stlpec): "))
    sachovnica[x][y] = [1, 'visited']
    print(sachovnica[0][0][0])
    for riadok in sachovnica:
        print(riadok)

