from math import comb

s1 = input()
s2 = input()

s1num = 0
s2num = 0
unknown = 0

for i in range(len(s1)):  # value of s1
    if s1[i] == '+':
        s1num += 1
    else:
        s1num -= 1

for i in range(len(s2)):  # value of s2 + count ?
    if s2[i] == '+':
        s2num += 1
    elif s2[i] == '-':
        s2num -= 1
    else:
        unknown += 1

# required difference
diff = s1num - s2num

# impossible case
if (diff + unknown) % 2 != 0:
    print(0.0)
else:
    x = (diff + unknown) // 2  # number of '+' we need in '?'

    if x < 0 or x > unknown:
        print(0.0)
    else:
        ans = comb(unknown, x) / (2 ** unknown)
        print(ans)