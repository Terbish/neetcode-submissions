class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        

        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j) - ord('a')] += 1                
            key = tuple(count)
            print(key)
            if key not in dic:
                dic[key] = []
            dic[key].append(i)
        
        return list(dic.values())