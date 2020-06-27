# Improving dfs
# Create a stack for DFS, no need for visited if the graph is acyclic
def dfs(self, node)
    stack = [] 

    # Push the current source node.  
    stack.append(node)  

    while (len(stack)):  
        # Pop a vertex from stack and print it  
        node = stack[-1]  
        stack.pop() 

        # Get all adjacent vertices of the popped vertex s  
        # If a adjacent has not been visited, then push it  
        # to the stack.  
        for node in self.adj[node]:  
            if (not visited[node]):  
                stack.append(node)  



# Simple method that involves O(n) space 
visited = set() # Set to keep track of visited nodes.
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

