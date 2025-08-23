from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
c = Counter(nums)

s = "banana"
print(Counter(s))

c = 'banana'
print(c['a'])  # 3 （'a'の出現回数）
print(c['x'])  # 0 （存在しないキーでも0を返す）

print(c.most_common())      # [('a', 3), ('n', 2), ('b', 1)]
print(c.most_common(1))     # [('a', 3)] 上位1件
print(c.most_common(2))     # [('a', 3), ('n', 2)]

print(list(c.elements()))  # ['b', 'a', 'a', 'a', 'n', 'n']
