# Naloga 1: Podkupnine
# Emina Merlak Susman
# Praktična matematika, 3. letnik
# za primere z velikimi b-ji, a-ji in q-ji laufa v približno 5s, ne računa pravilnih odgovorov razen za prvi testni

from decimal import Decimal

def powerLL(x, n):
    result = 1;
    while (n):
        if (n & 1):
            result = result * x % t;
        n = n // 2;
        x = x * x % t;
    return result;

def vsota(c, q_na_b):
    # vsota omejenega naraščajočega geometrijskega zaporedja z
    # b členi: c + cq + cq² + ... + cq^b-1
    prvi = c/abs(1 - q)%t
    drugi = abs(q_na_b - 1)%t
    if q_na_b == 0:
        return (c/abs(1 - q) % t)*abs(t - 1)
    return int(prvi*drugi) % t
            
primeri = open('primeri_big.txt')
st_testnih = int(primeri.readline())

for i in range(st_testnih):
    ln = primeri.readline()
    n, m, q, t = map(int, primeri.readline().split(' '))
    vs_total = 0
    rem = 1/abs(q - 1) % t
    for j in range(m):
        a, b, c = map(int, primeri.readline().split())
        quotient = (c%t * rem) %t
        
        #print("kvocient", quotient)
        q_na_b = pow(q,b,t)
        #print(f"{q}_na_{b}", q_na_b)
        q_na_a = pow(q,a-1,t)
        #print(f"{q}_na_{a-1}", q_na_a)
        vsota_do_b = vsota(c, q_na_b)
        vsota_do_a = vsota(c, q_na_a)

        vsota_chunk_polinoma = abs(vsota_do_b - vsota_do_a) % t

        #print(f"delna vsota: {vsota_do_b} - {vsota_do_a} = {vsota_chunk_polinoma}")
        vs_total += vsota_chunk_polinoma

    
    print(int(vs_total) % t)
    
#a = (5 + 5*53 + 5*pow(53,2) + 5*pow(53,3) + 5*pow(53,4) + 5*pow(53,5) + 5*pow(53,6) + 5*pow(53,7)) % 10061
#b = (5 + 5*53 + 5*53**2 + 5*53**3 + 5*53**4 + 5*53**5 + 5*53**6) % 10061
#print(b-a, b, a)