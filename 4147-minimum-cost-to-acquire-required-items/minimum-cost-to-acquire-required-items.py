class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        costSingles = need1*cost1 + need2*cost2
        costDoubles = max(need1, need2) * costBoth
        common = min(need1, need2)
        costCombination = common*costBoth + (need1-common)*cost1 + (need2-common)*cost2
        return min(costSingles, costDoubles, costCombination)
        