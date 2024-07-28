# Emina Merlak Susman
# 27151132
# Praktična matematika

N, M = map(int, input().split())

votes = list(map(int, input().split()))
supp = list(map(int, input().split()))

parties = [-1 for i in range(N)]


def find_first(p):
    # finds the party at the root
    while parties[p] != -1:
        p = parties[p]
    return p


def change_opinion_prev(p, r):
    # changing opinions of all the parties
    # p has ever signed a contract with

    while parties[p] != -1:
        c = p
        p = parties[p]
        parties[c] = r


for i in range(M):
    ln = list(map(int, input().split()))

    p1 = ln[0] - 1
    p2 = ln[1] - 1

    r1 = find_first(p1)
    r2 = find_first(p2)

    if len(ln) == 2:
        # both parties sign a contract
        if r1 != r2:
            parties[r1] = r2
            supp[r2] = supp[r1]
            votes[r2] += votes[r1]
            change_opinion_prev(p1, r2)  # set p2's root opinion to all the parties that p1 has a contract with

    else:
        p3 = ln[2] - 1
        r3 = find_first(p3)

        op = supp[r1] + supp[r2] + supp[r3]
        if op >= 2:
            supp[r1] = 1
            supp[r2] = 1
            supp[r3] = 1
        else:
            supp[r1] = 0
            supp[r2] = 0
            supp[r3] = 0

        change_opinion_prev(p3, r3)
        change_opinion_prev(p1, r1)
        change_opinion_prev(p2, r2)

y = 0
n = 0

for i in range(N):
    if parties[i] == -1:
        if supp[i] == 1:
            y += votes[i]
        else:
            n += votes[i]

print(y, n)

#res = open("glasovanje01.out")
#print(res.readline())
