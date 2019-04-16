# Naloga 4: Lov na zaklad
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA 1


import sys
sys.setrecursionlimit(100000)

def main():

    def tarjan(graph):
        n = len(graph)
        index_counter = 0
        component_counter = 0
        stack = []
        in_stack = [False]*n
        lowlinks = [n+1]*n
        index = [-1]*n
        result = []
        stevilo_komp = []


        def strongconnect(node, component_counter, index_counter):

            index[node] = index_counter
            lowlinks[node] = index_counter
            index_counter += 1
            stack.append(node)
            in_stack[node] = True

            for v, w in graph[node]:
                if index[v] == -1:
                    component_counter, index_counter = strongconnect(v, component_counter, index_counter)
                    lowlinks[node] = min(lowlinks[node], lowlinks[v])
                elif in_stack[v]:
                    lowlinks[node] = min(lowlinks[node], index[v])

            if lowlinks[node] == index[node]:
                component = []
                while True:
                    v = stack.pop()
                    in_stack[v] = False
                    component.append(v)
                    stevilo_komp.append((v, component_counter)) #ni urejeno, uredimo po vozliscih, torej po prvi komponenti
                    if v == node: break
                result.append(component)
                component_counter += 1

            return component_counter, index_counter


        for i in range(n):
            if index[i] == -1:
                component_counter, index_counter = strongconnect(i, component_counter, index_counter)

        stevilo_komp.sort()
        

        return result, stevilo_komp


#########################################################################################
                        
   
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]

    for i in range(M):
        Ai, Bi, Ci = map(int, input().split())
        #vozlisca se zacnejo pri 0
        G[Ai - 1].append((Bi - 1, Ci))

    KPK, stevilo_komp = tarjan(G)


        
    najdrazja_pot = [0 for _ in range(N)]

    for i in range(len(KPK)):
        vrednost = [0]

        for komponenta in KPK[i]:
             for vozl, utez in G[komponenta]:
                 if stevilo_komp[vozl][1] == i:
                    najdrazja_pot[i] += utez

                 else:
                     vrednost.append(utez + najdrazja_pot[stevilo_komp[vozl][1]])
        najdrazja_pot[i] += max(vrednost)


    for vozlisce in range(N): 
        print(najdrazja_pot[stevilo_komp[vozlisce][1]])


main()
