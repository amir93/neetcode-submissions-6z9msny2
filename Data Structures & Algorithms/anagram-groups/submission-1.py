class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}
        for i in range(len(strs)):
            d, sl= {}, []
            for k in strs[i]:
               d[k] = d.get(k, 0) + 1    
            for k, v in d.items():
                sl.append(str(v) + k)
            e =frozenset(sl)
            v = l.get(e, [])
            v.append(strs[i])
            l[e] = v
        return list(l.values())



