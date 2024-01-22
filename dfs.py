direction = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 模拟上下左右四个搜索方向
matrix = [[],[]]
i, j = 0, 0  # 搜索的起始位置

def dfs(i, j):

    if i, j 满足某种条件:    # 有明确终点时使用，可有可无
        // 执行操作如输出路径等
        return


    for direction_X, direction_Y in direction:   #对于一个父端点下的所有子端点
        new_X = i + direction_X
        new_Y = j + direction_Y

        # 可通过改变和筛选matrix[new_X, new_Y]的值来避免重复或逆向搜索
        if new_X, new_Y, matrix[new_X, new_Y] 满足某种条件,例如坐标越界或遇到障碍物等:
            continue
        #执行操作
        dfs(new_X, new_Y)  # 深度遍历
        # 遍历结束恢复操作

dfs(i, j)
