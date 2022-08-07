from top48 import *

def prim(graph):
    n = len(graph)
    included = {0}
    mst = [[0 for x in range(n)] for y in range(n)]

    while len(included) < n:
        minimum = 999999
        x, y = 0, 0
        for u in included:
            for v in range(u + 1, n):
                if v not in included and graph[u][v] < minimum:
                    minimum = graph[u][v]
                    x, y = u, v
        included.add(y)
        mst[x][y] = minimum
        mst[y][x] = minimum

    print(mst)
                

def main():

    mst = prim(g)

if __name__=="__main__":
    main()
