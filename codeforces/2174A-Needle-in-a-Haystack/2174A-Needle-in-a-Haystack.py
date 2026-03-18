from collections import Counter

T= int(input())

for _ in range(T):
    s = list(input().strip())
    t = list(input().strip())
    
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Check if all letters of s exist in t
    possible = True
    for c in count_s:
        if count_t[c] < count_s[c]:
            possible = False
        count_t[c] -= count_s[c]  # remove letters used by s
    
    if not possible:
        print("Impossible")
        continue
    
    # Build sorted leftover letters
    leftover = []
    for c in sorted(count_t.keys()):
        leftover.extend([c] * count_t[c])
    
    # Merge leftover letters and s to get lexicographically smallest result
    result = []
    i = j = 0
    while i < len(leftover) and j < len(s):
        if leftover[i] < s[j]:
            result.append(leftover[i])
            i += 1
        else:
            result.append(s[j])
            j += 1
    
    # Add remaining letters
    result.extend(s[j:])
    result.extend(leftover[i:])
    
    print("".join(result))