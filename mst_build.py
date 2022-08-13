from top48 import *

from graph_visualizer import visualize

def prim(graph):
    n = len(graph)
    included = {0}
    mst = [[0 for x in range(n)] for y in range(n)]

    while len(included) < n:
        minimum = 999999999
        x, y = 0, 0
        for u in included:
            for v in range(n):
                if v not in included and graph[u][v] < minimum:
                    minimum = graph[u][v]
                    x, y = u, v
        included.add(y)
        mst[x][y] = minimum
        mst[y][x] = minimum

    return mst
                

def main():

    mst = prim(g)

    data = []

    for i in range(len(top48)):
        data.append((top48[i][0], top48[i][5], top48[i][6]))

    visualize(mst, data)

if __name__=="__main__":
    main()
