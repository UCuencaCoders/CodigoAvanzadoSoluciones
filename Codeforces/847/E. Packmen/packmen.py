def can_eat(m, p, a):
    i = 0
    j = 0
    while j < len(a) and i < len(p):
        if a[j] < p[i]:
            if p[i] - a[j] > m:
                return False
            else:
                r1 = p[i] + m - 2*(p[i] - a[j])
                r2 = p[i] + (m - (p[i] - a[j])) // 2
                r3 = p[i]
                max_range = max(r1, r2, r3)
                
                while j < len(a) and a[j] <= max_range:
                    j += 1
        else:
            max_range = p[i] + m
                
            while j < len(a) and a[j] <= max_range:
                j += 1
        i += 1
    return j == len(a)

n = int(input())
field = list(input())

p = []
a = []

for i in range(n):
    if field[i] == 'P':
        p.append(i)
    elif field[i] == '*':
        a.append(i)

r = 2 * n
l = 0

while l < r:
    m = (l + r) // 2
    if can_eat(m, p, a): 
        r = m
    else:
        l = m + 1

print(r)
