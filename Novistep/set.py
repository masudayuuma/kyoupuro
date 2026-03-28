# A - Five Integers
# A, B, C, D, E = map(int, input().split())

# ans = len(set([A, B, C, D, E]))
# len(set((A, B, C, D, E)))
# len({A, B, C, D, E})
# print(ans)

# B - Count Distinct Integers
# N = int(input())
# A = list(map(int, input().split()))
# print(len(set(A)))

# B - Substring
# S = input()
# ans_set = set()
# tmp = ''
# for i in range(len(S)):
#     tmp = S[i]
#     ans_set.add(tmp)
#     for j in range(i+1, len(S)):
#         tmp += S[j]
#         ans_set.add(tmp)

# print(len(ans_set))

# B - Shiritori 
N = int(input())
ans = set()
before = ''
continue_flag = True
for i in range(N):
    if before == '':
        before = input()
        ans.add(before)
        continue
    else:
        now = input()
        if not before[-1] == now[0] or now in ans:
            continue_flag = False
        else:
            ans.add(now)
            before = now

print('Yes') if continue_flag == True else print('No')