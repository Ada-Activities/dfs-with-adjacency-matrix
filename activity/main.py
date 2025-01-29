def dfs_helper(g, s, visited):
    if s not in visited:
        visited.append(s)

        # Line 7 IS MODIFIED
        # original: for neighbor in g[s]:
        for neighbor in range(len(g[s])):
            # LINE 9 IS NEW
            if g[s][neighbor] == 1:
                dfs_helper(g, neighbor, visited)

        # # Alternative
        # for neighbor, e in enumerate(g[s]):
        #     # LINE 9 IS NEW
        #     if e:
        #         dfs_helper(g, neighbor, visited)
        
def adj_matrix_dfs(g, s):
    """Below is a sample implementation of the basic recursive version of depth first search from Learn. Alter the code below so that it correctly performs depth first  search when `g` is an adjacency matrix instead of an adjacency list.
g : an adjacency matrix
s : index of node from which traversal starts
Returns a list of visited nodes in DFS order"""

    if len(g) == 0:
        return []

    visited = []

    dfs_helper(g, s, visited)
    
    return visited