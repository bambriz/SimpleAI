import collections
map = [
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2]
]

mapA = [
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 0, 2, 0, 0, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2]
]


#code will go here


#manhattan distance
def heuristic(s, d):
    sx, sy = s
    dx, dy = d
    return abs(dx - sx) + abs(dy - sy)


def neigh(v, m):
    n = []
    if v[0] > 0:
        node = (v[0]-1, v[1])
        if m[v[0]-1][v[1]] != 2:
            n.append(node)
    if v[1] > 0:
        node = (v[0], v[1]-1)
        if m[v[0]][v[1] - 1] != 2:
            n.append(node)
    if v[0] < row -1:
        node = (v[0]+1, v[1])
        if m[v[0]+1][v[1]] != 2:
            n.append(node)
    if v[1]<col-1:
        node = (v[0], v[1]+1)
        if m[v[0]][v[1] + 1] != 2:
            n.append(node)
    return n


def prpath(path, m):
    copM = m
    for point in path:
        copM[point[0]][point[1]] = 1
    for i in range(0, len(copM)):
        print(copM[i])

    pass


def bfs(strt, dest, m):
    pass



def astar(strt, dest, m):
    pass


def main():
    flag = True
    clist = []
    olist = []
    while(flag):
        print("Enter a valid starting coord: ")
        clist = input().split()
        if(len(clist) != 2):
            print("Invalid input try again:")
            continue
        clist = [int(x) for x in clist]
        if(map[clist[0]][clist[1]] == 2):
            print("That is a wall, try again:")
            continue
        break
    while (flag):
        print("Enter a valid ending coord: ")
        olist = input().split()
        if (len(clist) != 2):
            print("Invalid input try again:")
            continue
        olist = [int(x) for x in olist]
        if (map[olist[0]][olist[1]] == 2):
            print("That is a wall, try again:")
            continue
        break
    start = (clist[0], clist[1])
    end = (olist[0], olist[1])
    bfirst = bfs(start, end, map)
    afirst = astar(start, end, mapA)
    prpath(bfirst, map)
    print(" ")
    prpath(afirst, mapA)


if __name__ == '__main__':
    main()




