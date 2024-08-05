class Solution(object):
    def allPathsSourceTarget(self, graph):
        end = len(graph) - 1
        def dfs(node, path):
            if node == end:
                output.append(path)
            for n in graph[node]:
                dfs(n,path + [n])
        
        output = []
        dfs(0,[0])
        return output
