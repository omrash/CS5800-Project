'''
Status: WIP, non-functioning

This script uses the NetworkX library to visualize the input graph.
Just import the visualize() function from this file to use.

'graph' should be an adjacency matrix for all n vertices.
'array' should be an array for n vertices with
[n][0] = city_name, [n][1] = latitude, and [n][2] = longitude.
'''

import networkx as nx
import matplotlib.pyplot as plt

def visualize(graph, array, x_offset=0, y_offset=0, scale=1):
    '''
    x_offset: shifts all points along the x axis
    y_offset: shifts all points along the y axis
    scale: scales the distance from the origin (0,0) by input
    '''

    n = len(graph)
    G = nx.Graph()
    pos = {}
    name = {}

    for u in range(n):
        # calculate position
        x = (array[u][2] * scale) + x_offset
        y = (array[u][1] * scale) + y_offset

        # populate dicts
        pos[u] = x,y
        name[u] = array[u][0]
        
        # adds nodes with array data as attributes
        G.add_node(u, pos=(x,y), name=graph[u][0], lat=graph[u][1], long=graph[u][2])
        

    for u in range(n):
        for v in range(u+1, n):
            # add edges from matrix if > 0
            if graph[u][v]:
                G.add_edge(u, v, weight=graph[u][v])


    nx.draw_networkx(G, pos=pos, labels=name)
    plt.show()

    '''
    TO DO: Need to figure out basemap points relative to real world coordinates
    '''
