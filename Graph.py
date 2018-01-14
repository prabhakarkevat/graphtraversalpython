from Stack import Stack
from Queue import Queue

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
		stack.push(source)
		visited[source] = 1
		path += str(source)

		while not stack.isEmpty():
			v = stack.pop()
			# v = stack.peek()
			i = 0
			for _ in range(self.n):
				if adj_mat[v][i] == 1:
					if visited[i] != 1:
						stack.push(i)
						path += str(i)
						visited[i] = 1
						v = i
						i = 0
				i+=1
			# stack.pop()

		return path

	def bfs(self, adj_mat, source=0):
		path = ""
		queue = Queue()
		visited = [0] * self.n
		queue.enqueue(source)
		visited[source] = 1
		path += str(source)

		while not queue.isEmpty():
			v = queue.dequeue()
			for i, w in enumerate(adj_mat[v]):
				if w == 1 and visited[i] != 1:
					queue.enqueue(i)
					visited[i] = 1
					path += str(i)

		return path
