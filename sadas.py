import networkx as nx
colors_of_nodes={}
def initialize(nodes,edges):
  G=nx.Graph()
  colors = range(len(nodes))

  G.add_nodes_from(nodes)
  G.add_edges_from(edges)

  return G,colors

def coloring(node, color, graph):
   for neighbor in graph.neighbors(node):
       color_of_neighbor = colors_of_nodes.get(neighbor, None)
       if color_of_neighbor == color:
          return False

   return True

def get_color_for_node(node,colors, graph):
    for color in colors:
       if coloring(node, color,graph):
          return color