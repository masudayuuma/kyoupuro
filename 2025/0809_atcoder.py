# N = int(input())
# S = input()

# if len(S) >= 3 and S[-3:] == "tea":
#     print("Yes")
# else:
#     print("No")



# S = input().strip()
# n = len(S)
# ans = 0.0

# for i in range(n):
#     if S[i] != 't':
#         continue
#     t_count = 1 
#     for j in range(i + 1, n):
#         if S[j] == 't':
#             t_count += 1
#             length = j - i + 1
#             if length >= 3:
#                 rate = (t_count - 2) / (length - 2)
#                 if rate > ans:
#                     ans = rate

# print(f"{ans:.17f}")

# S=input()
# n=len(S)

# ans=0
# for i in range(n-1):
#     if S[i] != 't':
#         continue
#     t_count = 1
#     for j in range(i+1, n):
#         if S[j] == 't':
#             t_count += 1
#             lenght = j-i+1
#             if lenght >= 3:
#                 rate = (t_count-2)/(lenght-2)
#                 # print(i,j,t_count, lenght, rate, ans)
#                 if rate > ans:
#                     ans = rate

# print(ans)
      


# import sys
# input = sys.stdin.readline
# import bisect

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort()
# pref = [0]*(N+1)
# for i,a in enumerate(A,1):
#     pref[i] = pref[i-1] + a
# maxA = A[-1]

# def sum_min(t):
#     k = bisect.bisect_right(A, t) 
#     small = pref[k]
#     big = t * (N - k)
#     return small + big

# ans = []
# for _ in range(Q):
#     B = int(input())
#     if B > maxA:
#         ans.append("-1")
#         continue
#     t = B - 1
#     val = sum_min(t) + 1
#     ans.append(str(val))
# print("\n".join(ans))


def count_beautiful(T: str) -> int:
    even = 1 
    odd = 0
    parity = 0 
    for ch in T:
        if ch == '0':
            parity ^= 1
        if parity == 0:
            even += 1
        else:
            odd += 1
        # print(odd, even, parity)
    return even*(even-1)//2 + odd*(odd-1)//2

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    T = sys.stdin.readline().strip()
    print(count_beautiful(T))


