from collections import defaultdict
class Graph(object):

    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologicalSortHelper(self,vertex,visited,stack):
        # Mark the current node as visited.
        visited[vertex] = True

        # Recur for all the vertices adjacent to this vertex
        for nbh in self.graph[vertex]:
            if visited[nbh] == False:
                self.topologicalSortHelper(nbh,visited,stack)
        # Push current vertex to stack which stores result
        stack.append(vertex)

    def topologicalSort(self):
        stack = []
        visited = [False] * (self.V)

        # Call the recursive helper function to store Topological Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortHelper(i,visited,stack)

        # Now print the order of words.
        while stack:
            print(chr(ord('a')+stack.pop()),end=" ")

# TC = O(N * |S| + K) , where |S| denotes maximum length.
# SC = O(K)
def printOrderOfCharacters(words,total_char):

    # Make a Graph
    graph = Graph(total_char)
    n = len(words)

    # Find Mismatching char between two consecutive words and make graph from that.
    for i in range(0,n-1):
        word1 = words[i]
        word2 = words[i+1]

        for i in range(0,min(len(word1),len(word2))):
            if word1[i] != word2[i]:
                # Make 0 based graph from words that's why - ord('a')
                source = ord(word1[i]) - ord('a')
                dest = ord(word2[i]) - ord('a')
                # Add the graph edge is not exist prior
                if dest not in graph[source]:
                    graph.addEdge(source,dest)
                    break

    # Run topological sort once the graph is built completely.
    graph.topologicalSort()





# Driver Program
words = ["caa", "aaa", "aab"]
printOrderOfCharacters(words,3)

