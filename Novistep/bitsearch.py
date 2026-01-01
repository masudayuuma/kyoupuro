# Enumeration of Subsets I
n = int(input())

for d in range(1 << n):
    elements = []
    for i in range(n):
        if (d >> i) & 1:
            elements.append(i)
    if elements:
        print(f"{d}: {' '.join(map(str, elements))}")
    else:
        print(f"{d}:")

