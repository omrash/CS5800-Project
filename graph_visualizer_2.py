'''
Status: WIP: Need to work on the j iteration and use the def visualize call
from graph_visualizer

Failing to install Basemap to draw out US map

'''

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
# from mpl_toolkits.basemap import Basemap as Basemap
from top48 import *

G = nx.Graph()

# set up canvas figure size
plt.figure(figsize=(50, 40))

for i in range(len(top48)):
    G.add_node(top48[i][0], pos=(top48[i][6], top48[i][5]), weight=g[0][i])

for j in range(len(g)):
    w = round(g[0][j])
    # need to work on the j iteration. Trying to scale out nodes first.
    G.add_edge(top48[j-1][0], top48[j][0], weight=w)
    nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), with_labels=True,
                     edge_color="lightblue", node_size=800, width=2, font_size=25,
                     node_color="orange")

    nx.draw_networkx_edge_labels(G, nx.get_node_attributes(G, 'pos'),
                                 edge_labels=nx.get_edge_attributes(G, 'weight'),
                                 label_pos=0.2,
                                 font_color="black",
                                 font_size=20)

# Making a legend
legend1 = mlines.Line2D(range(1), range(1), color="white", marker='o',
                        markerfacecolor="orange")
legend2 = mlines.Line2D(range(1), range(1), marker='',
                        markerfacecolor="lightblue")
plt.legend((legend1, legend2), ('Cities', 'Route'), loc=3, fontsize=40)

plt.title('Connecting 48 Most Populous Cities in the US', fontsize=40)
plt.xlabel("West    ---------   Longitude   ---------     East ", fontsize=40)
plt.ylabel("South    ---------   Latitude   ---------     North ", fontsize=40)
plt.savefig("visual.png", dpi=100)
print("Visual saved\n")

