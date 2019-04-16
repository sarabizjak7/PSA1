# Naloga 6: Žaba
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA 1

import sys
sys.setrecursionlimit(10000000)

####################################################################################

#N je stevilo lokvanjev, K pomeni, da zaba pristane na k-tem lokvanju
N, K = map(int, input().split())

#seznam n stevil mi, mi = st. muh na i-tem lokvanju
muhe = list(map(int, input().split()))

####################################################################################

max_skok = 141

tabela = [[0] * (2 * max_skok + 1) for i in range(N)]

def zaba(zacetek, pozicija):

    if pozicija >= N:
        return 0

    trenutna = K + zacetek - max_skok

    if trenutna <= 0:
        return 0

    if tabela[pozicija][zacetek] != 0:
        return tabela[pozicija][zacetek]


    #vse tri moznosti, kamor lahko skocimo : za (k - 1) / (k) / (k + 1) naprej
    #dolzina dveh zaporednih skokov razlicna za najvec 1
    zaba1 = zaba(zacetek - 1, pozicija + trenutna - 1)
    zaba2 = zaba(zacetek, pozicija + trenutna)
    zaba3 = zaba(zacetek + 1, pozicija + trenutna + 1)
    
    #izberemo pot, kjer poberemo najvec muh, maksimiziramo
    zabica = max(zaba1, zaba2, zaba3) + muhe[pozicija]
                
    tabela[pozicija][zacetek] = zabica

    return zabica

print(zaba(max_skok, K - 1))

    

    


