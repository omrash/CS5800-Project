'''
Status: WIP, cities are bunched up, figuring out how to space out nodes

Need to work on the j iteration
'''

import networkx as nx
import matplotlib.pyplot as plt
from top48 import *

G = nx.Graph()

for i in range(len(top48)):
    G.add_node(top48[i][0], pos=(top48[i][6], top48[i][5]), weight=g[0][i])
    nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), with_labels=True,
                     node_size=300, width=2, edge_color="darkgrey")

for j in range(len(g)):
    w = g[0][j]
    # need to work on the j iteration. Trying to scale out nodes first.
    G.add_edge(top48[j-1][0], top48[j][0], weight=w)
    nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), with_labels=True)

    nx.draw_networkx_edge_labels(G,nx.get_node_attributes(G, 'pos'),
                                 edge_labels=nx.get_edge_attributes(G, 'weight'),
                                 label_pos=1, font_color="lightblue")

    # edge_labels={(top48[j-1][0], top48[j][0]): w}

plt.title('Top 48 Most Populous Cities in the US')
plt.xlabel("West    ---   Longitude   ---     East ")
plt.ylabel("South    ---   Latitude   ---     North ")
plt.savefig("visual.png", dpi=500)

