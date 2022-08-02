import collections
rows = []
columns = []

rows, cols = (10, 10)
# generate grid
array_grid = [[True for i in range(cols)] for j in range(rows)]

start_point = (input("enter start point as x,y (range is from 0-9)"))
start_point = tuple(map(int, start_point.split(",")))
end_point = (input("enter end point as x,y (range is from 0-9)"))
end_point = tuple(map(int, end_point.split(",")))


def generate_obstacles():
    array_grid[0][5] = array_grid[2][3] = array_grid[3][4] = array_grid[6][7] = array_grid[8][9] = False


def find_a_way(start, end):
    queue = collections.deque([[start]])
    already_checked = set(start)

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if y == end[1] and x == end[0]:
            print("You are lucky, your final path is ", path)
            return path
        # checking top,bottom, right and left of node if there is obstacle
        for x1, y1 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if 0 <= x1 < len(array_grid) and 0 <= y1 < len(array_grid) and array_grid[x1][y1] != False and (x1, y1) not in already_checked:
                queue.append(path + [(x1, y1)])
                already_checked.add((x1, y1))
    print("no way out, sorry !!!")


generate_obstacles()
find_a_way(start_point, end_point)



