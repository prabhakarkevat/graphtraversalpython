from Graph import Graph

class MainClass(object):
	"""docstring for MainClass"""
	def __init__(self):
		super(MainClass, self).__init__()
			
	def main(self):
		adj_mat = [
			[0, 1, 1, 0, 0, 0, 1],
			[1, 0, 0, 0, 1, 0, 1],
			[1, 0, 0, 1, 0, 0, 1],
			[0, 0, 1, 0, 0, 1, 1],
			[0, 1, 0, 0, 0, 1, 1],
			[0, 0, 0, 1, 1, 0, 1],
			[1, 1, 1, 1, 1, 1, 0],
		]

		graph = Graph(7)
		print(graph.dfs(adj_mat, 0))

if __name__ == '__main__':
	MainClass().main()