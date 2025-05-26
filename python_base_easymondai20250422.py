# 1〜Nまでの数について、3の倍数→Fizz、5の倍数→Buzz、両方→FizzBuzz、それ以外→数値
# num = int(input())
# for i in range(1, num+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# 整数列を受け取り、合計が偶数ならEven、奇数ならOddを出力
# nums = map(int, input().split())
# total = sum(nums)
# if total % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# 文字列中の文字が何回出たかを表示（順不同）
# s = input()
# counter = {}
# for c in s:
#     if c in counter:
#         counter[c] += 1
#     else:
#         counter[c] = 1

# for k,v in counter.items():
#     print(k, ":", v)

# 数列の中で最大の数と、そのインデックス（位置）を出力
# nums = list(map(int, input().split()))
# max_index = 0
# max_num = nums[0]

# for i in range(1, len(nums)):
#     if  nums[i] > max_index:
#         max_index = i+1
#         max_num = nums[i]

# print(f"Max: {max_num} at index {max_index}")

# リスト内の重複を削除して出力
# nums = list(map(int, input().split()))
# unique_num = list(set(nums))
# print(unique_num)

# 整数nが素数ならTrue、そうでなければFalseを返す関数を作れ
# def is_prime(num):
#     if num < 2:
#         False
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# print(is_prime(7))

# "racecar" や "abcba" のように前から読んでも後ろから読んでも同じ文字列かを判定
# def is_reverseword(n):
#     if n == n[::-1]:
#         return True
#     else:
#         return False
    
# print(is_reverseword("hello"))
# print(is_reverseword("aabbaa"))

# 2つの整数a, bの最大公約数（GCD）を求める関数
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# print(gcd(32,8))

# def char_counter(s):
#     counter = {}
#     for c in s:
#         if c in counter:
#             counter[c] += 1
#         else:
#             counter[c] = 1
#     return counter
# print(char_counter("couunter"))

# 数値のリストを受け取り、降順にソートして返す関数
# def sort_descending(list):
#     sort_list = sorted(list, reverse= True)
#     return sort_list
# print(sort_descending([3, 1, 4, 1, 5]))

# def sum_even(numbers):
#     even_index = 0
#     even_index_sum_num = 0
#     for i in range(0, len(numbers)):
#         if numbers[i] % 2 == 0:
#             even_index_sum_num += numbers[i]
#     return even_index_sum_num

# # テスト例
# print(sum_even([1, 2, 3, 4, 5, 8]))  # 6

# def count_vowels(s):
#     vowels = ['a', 'i', 'u', 'e', 'o']
#     vowles_count = 0
#     for c in s:
#         if c in vowels:
#             vowles_count += 1
#     return vowles_count

# # テスト
# print(count_vowels("hello"))   # 2
# print(count_vowels("rhythm"))  # 0

# def common_elements(list1, list2):
#     common_element_num = []
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 common_element_num.append(i)
#     common_element_num = list(set(common_element_num))
#     return common_element_num
    
# # テスト
# print(common_elements([1,2,3,3], [2,3,4]))  # [2, 3]

# def reverse_digits(n):
#     n_str = str(n)
#     if n_str.startswith('-'):
#         return int('-'+n_str[1:][::-1])
#     else:
#         return int(n_str[::-1])

# # テスト
# print(reverse_digits(123))    # 321
# print(reverse_digits(-456))   # -654

# def median(lst):
#     sorted_list = sorted(lst)
#     if len(sorted_list) % 2 == 0:
#         half_num = (len(sorted_list)/2 + len(sorted_list)/2+1)/2
#     else:
#         half_num = (len(sorted_list)/2 - 0.5)
#     return half_num

# # テスト
# print(median([3,1,2]))     # 2
# print(median([1,2,4,5]))   # 3.0

# 1〜9のかけ算結果を表のように出力
# def print_multiplication_table():
#     for i in range(1, 10):
#         row = []
#         for j in range(1, 10):
#             row.append(i * j)
#         print(row)

# # 実行
# print_multiplication_table()

# def sum_matrix(matrix):
#     total = 0
#     for i in matrix:
#         for j in i:
#             total += j
#     return total

# # テスト
# print(sum_matrix([[1,2,3],[4,5,6]]))  # 21

# 入力：2次元リスト
# 出力：最大値, 行番号, 列番号（例: 9, 1, 2）
# def max_in_matrix(matrix):
#     max_value = 0
#     max_value_row = 0
#     max_value_column = 0
#     for row in range(len(matrix)):
#         for column in range(len(matrix[row])):
#             if matrix[row][column] > max_value:
#                 max_value = matrix[row][column]
#                 max_value_row = row
#                 max_value_column = column
#     return max_value, max_value_row, max_value_column


# # テスト
# print(max_in_matrix([[1,2,3],[4,9,6],[7,8,5]]))  # 9, 1, 1（行・列は0始まりでもOK）

# 入力：2次元リスト（0と1のみ）
# 出力：1の合計数（例: 5）
# def count_ones(grid):
#     total = 0
#     for row in grid:
#         for value in row:
#             if value == 1:
#                 total += 1
#     return total

# # テスト
# grid = [[0,1,0],[1,1,1],[0,0,1]]
# print(count_ones(grid))  # 5

# def surround_with_hash(grid):
#     width = len(grid)+2
#     border = ["#" * width]
#     for i in range (len(grid)):
#         border.append("#"+grid[i]+"#")
#     border.append("#" * width)
#     return border
            

# # テスト
# print(surround_with_hash(["abc", "def", "ghi"]))
# # ['#####', '#abc#', '#def#', '#ghi#', '#####']

# def is_step_array(arr):
#     for i in range(1, len(arr)):
#         if abs(arr[i] != arr[i-1] + 1):
#             return False
#     return True

# # テスト
# print(is_step_array([1, 2, 3, 4]))   # True
# print(is_step_array([1, 3, 4]))      # False

# def mode(arr):
#     num = {}
#     for i in range(len(arr)):
#         if arr[i] in num:
#             num[arr[i]] += 1
#         else:
#             num[arr[i]] = 1
#     max_num_count = 0
#     max_num = 0
#     for i in num:
#         if num[i] > max_num_count:
#             max_num_count = num[i]
#             max_num = i
#     return max_num

# # テスト
# print(mode([1,2,2,3,1,2]))  # 2

# def run_length_encode(s):
#     encoded_data = ""
#     counter = {}
#     for i in range(len(s)):
#         if s[i] in counter:
#             counter[s[i]] += 1
#         else:
#             counter[s[i]] = 1
#     for i in counter:
#         encoded_data += i+str(counter[i])

#     return encoded_data

# # テスト
# print(run_length_encode("aaabbc"))  # a3b2c1
    
# def final_position(commands):
#     moved = [[0],[0]]
#     for c in range(len(commands)):
#         if commands[c] == 'U':
#             moved[1][0] += 1
#         elif commands[c] == 'D':
#             moved[1][0] -= 1
#         elif commands[c] == 'L':
#             moved[0][0] -= 1
#         elif commands[c] == 'R':
#             moved[0][0] += 1
#     return moved

# # テスト
# print(final_position("UUDDLRLR"))  # (0, 0)
# print(final_position("UUU"))       # (0, 3)

# def can_escape(grid):
#     from collections import deque

#     h, w = len(grid), len(grid[0])
#     visited = [[False]*w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             if grid[i][j] == "S":
#                 start = (i, j)

#     q = deque([start])
#     visited[start[0]][ start[1]] = True
#     directions = [(-1,0), (1,0), (0,-1), (0,1)]

#     while q:
#         x, y = q.popleft()
#         if x == 0 or y == 0 or x == h-1 or y == w-1:
#             return True
#         for dx, dy in directions:
#             nx, ny =x+dx, y+dy
#             if 0 <= nx < h and 0 <= ny < w:
#                 if grid[nx][ny] == "."and not visited[nx][ny]:
#                     visited[nx][ny] = True
#                     q.append((nx,ny))
#     return False
    
# # テスト
# grid1 = [
#     "XXX",
#     "XS.",
#     "XXX"
# ]
# print(can_escape(grid1))  # True

# grid2 = [
#     "XXX",
#     "XSX",
#     "XXX"
# ]
# print(can_escape(grid2))  # False


# def throw_order(arr):
#     from collections import deque
#     q = deque(arr)
    
#     pop_num = q.popleft()
#     q.append(pop_num)
#     return q


# # テスト
# print(throw_order([3, 1, 2]))  # [1, 2, 3]

# def second_smallest(arr):
#     sort_nums = list(set(arr))
#     return sort_nums[1]

# # テスト
# print(second_smallest([5, 1, 4, 2]))  # 2

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# # テスト
# print(fibonacci(6))  # 8

#二分探索
# def binary_search(arr, target):
#     left, right = 0, len(arr)-1
#     while left <= right:
#         mid = int(left+right/2)
#         if target == arr[mid]:
#             return True
#         elif target > arr[mid]:
#             left = mid+1
#         else:
#             right = mid-1
#     return False


# # テスト
# print(binary_search([1, 3, 5, 7, 9], 5))  # True
# print(binary_search([1, 3, 5, 7, 9], 4))  # False

# def find_not_3_or_5():
#     i = 1
#     while i%3 == 0 or i%5 == 0:
#         i += 1
#     return i
# # テスト
# print(find_not_3_or_5())  # 1

#DFS（深さ優先探索）概念理解できたけどそもそも答え違う
# def can_visit_all(grid):
#     h, w = len(grid), len(grid[0])
#     visited = [[False] * w for _ in range(h)]
    
#     # スタート地点を探す
#     for i in range(h):
#         for j in range(w):
#             if grid[i][j] == 2:
#                 start = (i, j)
                
#     def dfs(x, y):
#         if x < 0 or x >= h or y < 0 or y >= w:
#             return
#         if grid[x][y] == 0 or visited[x][y]:
#             return
#         visited[x][y] = True
#         for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
#             dfs(x+dx, y+dy)
    
#     # 探索開始
#     dfs(start[0], start[1])
    
#     # 全ての1または2が訪問済みならTrue
#     for i in range(h):
#         for j in range(w):
#             if grid[i][j] in (1,2) and not visited[i][j]:
#                 return False
#     return True

        
    

# # テスト例
# grid1 = [
#     [2,1,0],
#     [0,1,1],
#     [1,0,0]
# ]
# print(can_visit_all(grid1))  # True


