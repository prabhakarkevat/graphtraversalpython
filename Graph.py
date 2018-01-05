from Stack import Stack

class Graph(object):
	"""docs for Graph"""
	def __init__(self, n=0):
		super(Graph, self).__init__()
		self.n = n
	
	def dfs(self, adj_mat, source=0):
		path = "";
		stack = Stack();
		visited = [0] * self.n
		stack.push(source)
		visited[source] = 1
		path = path + str(source)

		while not stack.isEmpty():
			v = stack.peek()
			stack.pop()
			for i, w in enumerate(adj_mat[v]):
				if w == 1 and visited[i] != 1:
					stack.push(i)
					path = path + str(i)
					visited[i] = 1

		return path
