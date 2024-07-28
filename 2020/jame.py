# Emina Merlak Susman
# 27151132
# Praktična matematika

import bisect
from operator import xor

(n, p) = map(int, input().split())

kap = list(map(int, input().split()))

p_raw = [0] + list(map(int, input().split())) # "napačne" poizvedbe

kap_urejeno = [kap[0]]
for x in range(1, n):
    nasledn = kap_urejeno[x - 1] + kap[x]
    kap_urejeno.append(nasledn)

#print(kap_urejeno)

p0 = 0
poizvedbe_taprave = [ p0 ]

for i in range(0, p):
    prejsni = poizvedbe_taprave[i]
    #print("prejsni", prejsni)
    zdejsni = p_raw[i+1]
    #print("zdejsni", zdejsni)
    poiz = xor(zdejsni, prejsni)
    #print("poiz", poiz)


    rezultat = bisect.bisect_left(kap_urejeno, poiz) + 1
    poizvedbe_taprave.append(rezultat)
    print(rezultat, end=" ")