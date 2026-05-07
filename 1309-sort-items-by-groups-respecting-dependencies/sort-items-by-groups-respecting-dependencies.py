class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topsort(graph,indeg):
            q = deque()

            for i in range(len(indeg)):
                if indeg[i] == 0:
                    q.append(i)
            res = []
            while q:
                node = q.popleft()
                res.append(node)
                for lij in graph[node]:
                    indeg[lij] -= 1
                    if indeg[lij] == 0:
                        q.append(lij)
            if len(res) == len(indeg):
                return res
            return []

        groupid = m
        for i in range(n):
            if group[i] == -1:
                group[i] = groupid
                groupid += 1
        adj_item = [[] for _ in range(n)]
        adj_grp = [[] for _ in range(groupid)]
        indeg_item = [0] * n
        indeg_grp = [0] * (groupid)

        for i in range(n):
            for first in beforeItems[i]:
                adj_item[first].append(i)
                indeg_item[i] += 1
                if group[i] != group[first]:
                    adj_grp[group[first]].append(group[i]) # for the grps 
                    indeg_grp[group[i]] += 1
        
        itemorder = topsort(adj_item, indeg_item)
        grouporder = topsort(adj_grp, indeg_grp)

        if not itemorder or not grouporder:
            return []


        srted_grp = [[] for _ in range(groupid)]

        for i in itemorder:
            srted_grp[group[i]].append(i)

        final_res = []

        for i in grouporder:
            final_res.extend(srted_grp[i])

        return final_res






                





        # values = [[] for _ in range(m + 1)]
        # for i in range(n):
        #     if group[i] == -1:
        #         values[0].append(i)
        #     else:
        #         values[group[i] + 1].append(i)
        # print(values)
        # # for childs in values:
        # #     for child in childs:
        # #         if beforeItems[child] != [] and beforeItems[child] in childs :
        # #             child = beforeItems[child]

        