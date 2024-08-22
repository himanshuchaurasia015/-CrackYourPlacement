
def graphColoring(graph, k, V):
    def check(i,c,graph,colors):
        for x in range(V):
            if x!=i and graph[i][x]==1 and colors[x]==c:
                return 0
        return 1        
    def solve(i,graph,colors):
        if i==V:
            return 1

        for c in range(1,k+1):
            if check(i,c,graph,colors):
                colors[i]=c
                if solve(i+1,graph,colors):
                    return 1
                colors[i]=0
        return 0
        
    colors=[0]*V
    return solve(0,graph,colors)
  

