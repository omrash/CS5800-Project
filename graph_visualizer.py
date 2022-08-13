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
from mpl_toolkits.basemap import Basemap as Basemap

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

    # Set up basemap
    m = Basemap(
        projection='merc',
        ellps = 'WGS84',
        llcrnrlon=-130,
        llcrnrlat=25,
        urcrnrlon=-60,
        urcrnrlat=50,
        lat_ts=0,
        resolution='i',
        suppress_ticks=True)

    for u in range(n):
        # calculate position
        x = (array[u][2] * scale) + x_offset
        y = (array[u][1] * scale) + y_offset

        # Basemap converts lat and long to map coordinates
        x,y = m(x, y)

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


    

    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#888888')


    nx.draw_networkx(G,
                     pos=pos,
                     labels=name,
                     font_size=8,
                     node_size=20,
                     node_color='#33ccff',
                     edge_color='white')
    plt.show()

    '''
    TO DO:
    * City name overlapping in eastern corridor
    * Color scheme?
    * Automate output to image file
    '''
