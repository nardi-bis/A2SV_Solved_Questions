t = int(input())

for _ in range(t):
    n = int(input())
    a = list(input().strip())
    b = list(input().strip())

    zeros = 0
    once = 0
    can_flip = [False] * n

    for i in range(n):
        if a[i] == '1':
            once += 1
        else:
            zeros += 1

        if once == zeros:
            can_flip[i] = True

    flip = False
    possible = True   

    for i in range(n - 1, -1, -1):
        bit = a[i]

        if flip:
            bit = '1' if bit == '0' else '0'

        if bit == b[i]:
            continue

        if not can_flip[i]:
            possible = False
            break

        flip = not flip

    if possible:
        print("YES")
    else:
        print("NO")