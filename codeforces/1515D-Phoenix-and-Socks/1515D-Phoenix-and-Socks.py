from collections import Counter

t = int(input())
for _ in range(t):
    n, l_count, r_count = map(int, input().split())
    colors = list(map(int, input().split()))

    L = Counter(colors[:l_count])
    R = Counter(colors[l_count:])
    for c in list(L.keys()):
        if c in R:
            mn = min(L[c], R[c])
            L[c] -= mn
            R[c] -= mn
            l_count -= mn
            r_count -= mn

    if l_count > r_count:
        L, R = R, L
        l_count, r_count = r_count, l_count

    diff = (r_count - l_count) // 2

    rem_pairs = 0
    for c in R:
        rem_pairs += R[c] // 2

    can_fix_by_flipping = min(diff, rem_pairs)

    ans = diff + (l_count + (diff - can_fix_by_flipping))
    print(ans)