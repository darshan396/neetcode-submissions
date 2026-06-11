class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = []
        for i in strs:
            sorted_word = "".join(sorted(i))
            strs1.append(sorted_word)
        vis = [0] * len(strs)
        ans = []
        for j in range(len(strs)):
            if vis[j] == 0:
                temp = []
                temp.append(strs[j])
                vis[j] = 1
                for k in range(j+1, len(strs)):
                    if strs1[j] == strs1[k]:
                        temp.append(strs[k])
                        vis[k] = 1
                ans.append(temp)
        

        return ans