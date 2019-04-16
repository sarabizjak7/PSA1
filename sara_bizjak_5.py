# Naloga 5: Glasovanje
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA1


N, M = map(int, input().split())


st = list(map(int, input().split()))

glas = list(map(int, input().split()))


stranka = list(range(N))
rang = [0 for x in range(N)]

##########################################################################

def poisci_starse_danega_vozlisca(x):
    if stranka[x] != x:
        stranka[x] = poisci_starse_danega_vozlisca(stranka[x])
    return stranka[x]

def zdruzi(x, y):
    stars_x = poisci_starse_danega_vozlisca(x)
    stars_y = poisci_starse_danega_vozlisca(y)
    
    if stars_x == stars_y:
        return
    
    ## manjsi prilagodi vecjemnu
    elif rang[stars_x] > rang[stars_y]:
        stranka[stars_y] = stars_x
    else:
        stranka[stars_x] = stars_y
        if rang[stars_x] == rang[stars_y]:
            rang[stars_y] += 1


###########################################################################        
#PO SESTANKIH
            
for m in range(M):
    sodelujoce_stranke = list(map(int, input().split()))

    ### dve stranke na sestanku - druga se prilagodi prvi
    
    if len(sodelujoce_stranke) == 2:

        #stranke na sestanku
        prva = int(sodelujoce_stranke[0])
        druga = int(sodelujoce_stranke[1])

        stars_prva = poisci_starse_danega_vozlisca(prva - 1)
        stars_druga = poisci_starse_danega_vozlisca(druga - 1)
        
        #glas druge stranke se prilagodi prvi
        glas[stars_druga] = glas[stars_prva]

        zdruzi(stars_prva, stars_druga)

    ### tri stranke na sestanku - prilagodijo vecini
        
    else:
        #stranke na sestanku
        prva = int(sodelujoce_stranke[0])
        druga = int(sodelujoce_stranke[1])
        tretja = int(sodelujoce_stranke[2])

        stars_prva = poisci_starse_danega_vozlisca(prva - 1)
        stars_druga = poisci_starse_danega_vozlisca(druga - 1)
        stars_tretja = poisci_starse_danega_vozlisca(tretja - 1)

        ### sum glasov je vsaj 2, torej sta vsaj dve stranku za -> mora biti tudi tretja stranka za
        if glas[stars_prva] + glas[stars_druga] + glas[stars_tretja] > 1:
            glas[stars_prva] = 1
            glas[stars_druga] = 1
            glas[stars_tretja] = 1
        ### za je le 1 stranka ali pa nobena, torej se prilagodi vecini in so vse proti
        else:
            glas[stars_prva] = 0
            glas[stars_druga] = 0
            glas[stars_tretja] = 0


za = 0

for n in range(N):
    if glas[poisci_starse_danega_vozlisca(n)] == 1:
            za += st[n] * glas[poisci_starse_danega_vozlisca(n)]
  

print(za, sum(st) - za)
        
        
    
