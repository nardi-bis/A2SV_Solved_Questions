n,k=map(int,input().split())
a=list(map(int,input().split()))
gap=[]
cost=0
for i in range(n-1):
    gap.append(a[i+1]-a[i])
gap.sort(reverse=True)
for i in range(k-1):
    cost+=gap[i]
initial=a[-1]-a[0]
print(initial-cost)

