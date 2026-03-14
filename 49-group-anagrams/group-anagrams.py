class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for elem in strs:
            tmp = tuple(sorted(elem))
            if tmp not in res:
                res[tmp] = []
            res[tmp].append(elem) 
        
        return list(res.values())