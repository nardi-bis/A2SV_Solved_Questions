n,s=map(int,input().split())
a=list(map(int,input().split()))
l=0
window=0
res=0
for r in range(n):
    window+=a[r]
    while window>s:
        window-=a[l]
        l+=1
    res+=r-l+1
print(res)

