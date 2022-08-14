from mst_build import prim
from analysis_tools import *
from graph_visualizer import visualize
from top48 import *

def railgorithm(graph, complete_graph):
    '''
    O(n^5), lol
    '''
    if len(graph) != len(complete_graph):
        raise ValueError("Graph lengths must be equal")
    n = len(graph)
    curr_sum = track_length(floyd_warshall(graph))


    
    travel_saved = 0
    x = 0
    y = 0
    for u in range(n):
        for v in range(u + 1, n):
            if graph[u][v] == 0:
                graph[u][v] = complete_graph[u][v]
                delta = curr_sum - track_length(floyd_warshall(graph))
                graph[u][v] = 0
                if delta > travel_saved:
                    travel_saved = delta
                    x,y = u,v
    
    graph[x][y] = complete_graph[x][y]

    return graph

def main():
    '''
    This took 10 minutes to produce an output with the current parameters
    '''

    mst = prim(g)

    new = mst

    while(track_length(new) < 20000):
        new = railgorithm(mst, g)

    visualize(new, top48)

if __name__=="__main__":
    main()
