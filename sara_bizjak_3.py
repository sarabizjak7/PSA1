# Naloga 3: Go
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA 1


def main():

        DIM = 19

        plosca = {}
        veljavni_odmiki = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Mozni odmiki oz sosedi za vsak kamen


        def prestej_prostosti(plosca, x, y, barva):
                """
                Presteje stevilo prostosti skupine kamnov, ki bi ji pripadal kamen te barve na celici (x, y).
                Vrne par (stevilo prostosti, povezana skupina kamnov).
                """
                obiskani = set()
                ze_steli = {(x, y)} # (x,y) ne stejemo k prostim mestom
                neobiskani = [(x, y)] if (x, y) in plosca else []
                prostosti = 0
                # S preiskovanjem v globino obiscimo celo povezano komponento te barve, zacnemo pri (x, y)
                while neobiskani:
                        (i, j) = neobiskani.pop()
                        obiskani.add((i, j))
                        # Preglejmo vse 4 sosede celice (i, j)
                        for (dx, dy) in veljavni_odmiki:
                                (di, dj) = i+dx, j+dy # Sosedi za vsako stran
                                if plosca.get((di, dj), None) == barva and (di, dj) not in obiskani:
                                        neobiskani.append((di, dj))
                                elif plosca.get((di, dj), None) == '.' and (di, dj) not in ze_steli:
                                        prostosti += 1
                                        ze_steli.add((di, dj))
                return prostosti, obiskani


        def poteza(plosca, x, y, barva):
                """ Vrne true, ce je poteza veljavna, sicer vrne False. """
                st_prostosti, _ = prestej_prostosti(plosca, x, y, barva)
                if plosca[(x, y)] == '.':
                        plosca[(x, y)] = barva # Poteza se izvede, ce je mesto prosto
                        st_ujetij = 0
                        # Preverimo, ce je prislo do morebitnih ujetij nasprotnikovih kamnov
                        for (dx, dy) in veljavni_odmiki:
                                st_prostosti_tmp, obiskani = prestej_prostosti(plosca, x+dx, y+dy, plosca.get((x+dx, y+dy), 'Neveljavno'))
                                if st_prostosti_tmp == 0 and plosca.get((x+dx, y+dy), None) != barva: # Obiskana povezana skupina kamnov nima prostosti, torej jo bomo pobrisali
                                        st_ujetij += len(obiskani)
                                        for (i, j) in obiskani:
                                                plosca[(i, j)] = '.'
                        if st_ujetij == 0 and st_prostosti == 0:
                                plosca[(x, y)] = '.'
                                return False
                        return True
                return False


        def izrisi(plosca):
                """ Izpise stanje plosce na izhod. """
                for i in range(1, DIM+1):
                        vrstica = [plosca[(i, j)] for j in range(1, DIM+1)]
                        print(''.join(vrstica))



        plosca = {(i, j): '.' for i in range(1, DIM+1) for j in range(1, DIM+1)}
        barva = 'B'

        while True:
                try:
                        vhod = input()
                        if vhod == "":
                                break
                        else:
                                y, x = map(int, vhod.split())
                                if poteza(plosca, x, y, barva):
                                        barva = 'B' if barva =='W' else 'W'

                except EOFError:
                        break

        izrisi(plosca)

                
         

main()


