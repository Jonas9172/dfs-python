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


迷宫答案：
n, m = list(map(int, input().split()))
maze = []
for i in range(n):
    maze.append(input().split())

path = [(0,0)]
d = ((1,0),(-1,0),(0,1),(0,-1))
p = []
def dfs(x,y):
    maze[x][y] = '1'
    if x == n-1 and y == m-1:
        for i in range(len(path)):
            print('({},{})'.format(path[i][0],path[i][1]))
        return 
    for x_d, y_d in d:
        new_x = x + x_d
        new_y = y + y_d
        if 0 <= new_x < n and 0 <= new_y < m and maze[new_x][new_y] == '0':
            path.append((new_x,new_y))
            dfs(new_x,new_y)
            path.pop()
            maze[new_x][new_y] = '0'

dfs(0,0)
