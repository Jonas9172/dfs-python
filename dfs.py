direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 模拟上下左右四个搜索方向
matrix = [[],[]]
i, j = 0, 0  # 搜索的起始位置

def dfs(i, j):

    if i, j, matrix[new_X, new_Y] 满足某种条件:    # 有明确终点时使用，可有可无
        // 执行操作如输出路径等
        return


    for direction_X, direction_Y in direction:   #对于一个父端点下的所有子端点
        new_X = i + direction_X
        new_Y = j + direction_Y

        # 可通过改变和筛选matrix[new_X, new_Y]的值来避免重复或逆向搜索
        if new_X, new_Y 满足某种条件 或 matrix[new_X, new_Y] == 0:  # 如果没有搜索过这个端点
            matrix[new_X, new_Y] == 1  # //将该端点设置为走过
            #执行操作
            dfs(new_X, new_Y)  # 深度遍历，递归下去
            matrix[new_X, new_Y] == 0  # 回溯

dfs(i, j)



考古学家答案：
n = int(input())
s = input().split()
a = set()
path = []
used = [0]*n
def dfs():
    if len(path) == n:
        a.add(''.join(path))
        return
    for i in range(n):
        if used[i]:
            continue
        path.append(s[i])
        used[i] = 1
        dfs()
        path.pop()
        used[i] = 0
dfs()
for each in sorted(list(a)):
    print(each)
