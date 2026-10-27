class Solution(object):
    def createGrid(self, m, n):
        result=[["#"] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0:
                    result[i][j]="."
                if j==n-1:
                    result[i][j]="."
        main_result=[]
        for i in range(m):
            new_list=""
            for j in range(n):
                new_list+=result[i][j]
            main_result.append(new_list)
        return main_result