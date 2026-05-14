from heapq import heappush, heappop


heap = []
ans = []
n = int(input())
for _ in range(n):
    s = input().split()

    if s[0][0] == 'i':
        ans.append(f'insert {s[1]}')
        heappush(heap, int(s[1]))
    elif s[0][0] == 'r':
        if not heap:
            ans.append('insert 1')
        else:
            heappop(heap)
        ans.append('removeMin')
    else:
        mn = int(s[1])
        while heap and heap[0] < mn:
            ans.append('removeMin')
            heappop(heap)
        if not heap or heap[0] > mn:
            heappush(heap, mn)
            ans.append(f'insert {mn}')
        ans.append(f'getMin {mn}')
print(len(ans))
for v in ans:
    print(v)