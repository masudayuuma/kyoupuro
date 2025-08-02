# N, A, B = map(int, input().split())
# S = input()

# ans = S[A:N-B]
# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))


# for b in B:
#     if b in A:
#         A.remove(b) 

# if A:  
#     print(*A)

# from collections import defaultdict
# N = int(input())
# A = list(map(int, input().split()))

# count = defaultdict(int)
# result = 0

# for i in range(N):
#     target = i - A[i]
    
#     result += count[target]

#     count[i+A[i]] += 1

# print(result)

MAX_PRECOMPUTE = 100000
N = int(input())
presents = []

for _ in range(N):
    P, A, B = map(int, input().split())
    presents.append((P, A, B))

Q = int(input())
precomputed = [0] * (MAX_PRECOMPUTE + 1)

for initial in range(MAX_PRECOMPUTE + 1):
    tension = initial
    for P, A, B in presents:
        if P >= tension:
            tension += A
        else:
            tension = max(0, tension - B)
    precomputed[initial] = tension

for _ in range(Q):
    X = int(input())
    
    if X <= MAX_PRECOMPUTE:
        print(precomputed[X])
    else:
        tension = X
        for P, A, B in presents:
            if P >= tension:
                tension += A
            elif tension < 5000000:
                tension = max(0, tension - B)
            
        print(tension)