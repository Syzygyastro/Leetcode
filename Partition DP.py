# Matrix chain multiplication and Burst Balloons

'''
1. (i, j) is the range of arrays
2. Base case: i == j.
3. Try all partitions k in [i, j] and recursively solve the subproblems. for k in range(i,j-1) f(i,k) and f(k+1,j).


'''