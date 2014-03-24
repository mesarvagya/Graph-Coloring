import networkx as nx
class graphColoring:
	def __init__(self,nodes,edges):
		self.G = nx.Graph()
		self.colors = range(len(nodes))
		self.nodes = self.G.add_nodes_from(nodes)
		self.edges = self.G.add_edges_from(edges)
		self.colors_of_nodes = {}
	
	def result(self):		
		for node in self.G.nodes():
			self.colors_of_nodes[node] = self.get_color_for_node(node)
		return self.colors_of_nodes

	def get_color_for_node(self,node):
		for color in self.colors:
			if self.coloring(node,color):
				return color

	def coloring(self,node,color):
		for neighbor in self.G.neighbors(node):
			colors_of_neighbor = self.colors_of_nodes.get(neighbor,None)
			if colors_of_neighbor == color:
				return False
		return True
