class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])   # sort by second element

        a = float('-inf')  # last selected chain end
        b = 0

        for i in pairs:
            if i[0] > a:   # check if current pair can be chained
                a = i[1]   # update end
                b += 1

        return (b)
