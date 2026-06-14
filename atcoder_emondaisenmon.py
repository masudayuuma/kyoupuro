# E - Alternating Costs
T = int(input())

for i in range(T):
    a, b, x, y = map(int, input().split())
    cost = 0
    x = abs(x)
    y = abs(y)
    diff = min(x, y)
    cost += diff*min(a, b)*2
    x -= diff
    y -= diff

    cnt = 0
    min_cost_A = min(a, b*3)
    min_cost_B = min(b, a*3)

    if x > 0:
        x_2 = x //2
        if x % 2 == 1:
            cost += min_cost_A*(x_2+1)+min_cost_B*x_2
        else:
            cost += min_cost_A*x_2+min_cost_B*x_2
    else:
        y_2 = y // 2
        if y % 2 == 1:
            cost += min_cost_A*y_2+min_cost_B*(y_2+1)
        else:
            cost += min_cost_A*y_2+min_cost_B*y_2

    print(cost)