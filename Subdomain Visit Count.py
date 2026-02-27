class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        table=defaultdict(int)
        for i in range(len(cpdomains)):
           num,domain=cpdomains[i].split(" ")
           table[domain]=table.get(domain,0)+int(num)
           while '.' in domain:
            domain=domain.split(".",1)[1]
            table[domain]=table.get(domain,0)+int(num)
        res=[]
        for k,v in table.items():
            ans=str(v)+" "+k
            res.append(ans)
        return res

        
