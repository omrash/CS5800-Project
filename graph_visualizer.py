'''
Status: WIP, non-functioning

This script uses the NetworkX library to visualize the input graph.
Just import the visualize() function from this file to use.

'graph' should be an adjacency matrix for all n vertices.
'array' should be an array for n vertices with
[n][0] = city_name, [n][1] = latitude, and [n][2] = longitude.
'''

import networkx as nx

def visualize(graph, array):
    G = nx.Graph()

    '''
    TO DO: Look into NumPy arrays for easier conversion into NX graphs
    pre-visualization. Also need to figure out basemap points relative to
    real world coordinates.
    '''
