# Naloga 1: Sosedski odnosi
# Sara Bizjak, 27161075, sara.bizjak@student.fmf.uni.lj.si
# matematika, PSA 1


 
def main():
 
    def sosedski_odnosi(N, D, sez):
        sez.sort()
        sosedi = 0
        j = 0
        
        for i in range(N):            
            while j <= (N -1) and sez[i] + D >= sez[j]:
                j += 1 
            sosedi += j - i - 1
        return sosedi
 
 
    N, D = map(int, input().split())
    sez = list(map(int, input().split()))
    print(sosedski_odnosi(N, D, sez))

main()
