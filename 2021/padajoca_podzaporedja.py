# Domača naloga 6: Padajoča podzaporedja
# Emina Merlak Susman, 27151132
# praktična matematika, 3. letnik

def how_many_length_k(arr, n, k):
    '''Counts the number of decreasing subsequences of length k in the array.
    It does this by making a matrix of size k x n where the i-th
    element in the row represents how many decreasing subsequences
    of length j end at this element.
    '''

    # number of decr. sub. of each length up to k, that end at i-th element
    count_at_each = [[0 for i in range(n)]
          for i in range(k)]

    for i in range(n):
        count_at_each[0][i] = 1

    for l in range(1, k):

        # loop through subsequences ending at arr[i]
        for i in range(l, n):

            # set count of subs. ending at arr[i] to 0
            count_at_each[l][i] = 0

            # loop through elements behind i in the list.
            # if you find one that's bigger,
            # then the number of decreasing subsequences
            # of length l-1 ending at the bigger elt. is
            # added to the number of decr.sub. at element arr[i]
            for j in range(l - 1, i):
                if (arr[j] > arr[i]):
                    count_at_each[l][i] += count_at_each[l - 1][j]

    # count up the k-th row of the matrix
    total = 0
    for i in range(k - 1, n):
        total += count_at_each[k - 1][i]

    return total


t = int(input())

for i in range(t):
    ln = input()
    n, k, m = list(map(int, input().split()))

    seq = list(map(int, input().split()))

    print(how_many_length_k(seq, n, k) % m)
