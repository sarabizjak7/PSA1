# Naloga 2: Podkupnine
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA 1



def main():

    def mnozenje_modul(a, b, mod):
        """Mnozi stevili a in b po modulu mod."""
        return ((a % mod) * (b % mod)) % mod

    def potenciranje_modul(q, n, mod):
        """Klasicen algoritem za hitro potenciranje q^n po modulu mod."""
        rez = 1
        while n > 0:
            if n & 1:
                rez = mnozenje_modul(rez, q, mod)
            q = mnozenje_modul(q, q, mod)
            n >>= 1
        return rez

    def geometrijska(eksp, q, t):
        """Izracuna vsoto prvih n-clenov geometrijskega zaporedja po modulu t."""
        prvi = 1
        e = q % t
        vsota = 1 #prvi clen stejem ze v vsoto

        while eksp > 0:
            if eksp & 1:
                vsota = (e * vsota + prvi) % t
            prvi = ((e + 1) * prvi) % t
            e = (e * e) % t
            eksp = eksp // 2
        return vsota



    N = int(input())

    for j in range(N):
        rezultat = 0
        presl = input()
        n, m, q, t = map(int, input().split())
        for i in range(m):
            ai, bi, ci = map(int, input().split())
            rezultat += (((ci % t) * (potenciranje_modul(q, ai - 1, t))) * (geometrijska(bi - ai, q, t))) % t
            rezultat = rezultat % t
            
    
        print(rezultat)

main()
        


