

"""
1.House Robber 2

"""

def exploreSubmatrices(grid):
    M, N = len(grid), len(grid[0])
    
    def print_submatrix(r1, c1, r2, c2):
        # Print the submatrix bounded by (r1, c1) to (r2, c2)
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                print(grid[i][j], end=' ')
            print()
        print("----")
    
    def explore(r2, c2):
        # Print the current submatrix
        print_submatrix(0, 0, r2, c2)
        
        # Attempt to expand the submatrix to the right if within bounds
        if c2 + 1 < N and r2 == 0:
            explore(r2, c2 + 1)
        
        # Attempt to expand the submatrix downward if within bounds
        if r2 + 1 < M:
            explore(r2 + 1, c2)
    
    # Start the recursive exploration from the top-left corner (0, 0)
    if M > 0 and N > 0:
        explore(0, 0)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
exploreSubmatrices(matrix)


