"""Longest common subsequence module"""

def lcslen(x, y):
    """Build a matrix of LCS length.

    This matrix will be used later to backtrack the real LCS.
    """

    # This is our matrix comprised of list of lists.
    # We allocate extra row and column with zeroes for the base case of empty
    # sequence. Extra row and column is appended to the end and exploit
    # Python's ability of negative indices: x[-1] is the last elem.
    c = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            if xi == yj:
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i][j-1], c[i-1][j])
    return c

def backtrack(c, x, y, i, j):
    """Backtrack the LCS length matrix to get the actual LCS"""
    if i == -1 or j == -1:
        return ""
    elif x[i] == y[j]:
        return backtrack(c, x, y, i-1, j-1) + x[i]
    elif c[i][j-1] >= c[i-1][j]:
        return backtrack(c, x, y, i, j-1)
    elif c[i][j-1] < c[i-1][j]:
        return backtrack(c, x, y, i-1, j)

def lcs(x, y):
    """Get the longest common subsequence of x and y"""
    c = lcslen(x, y)
    return backtrack(c, x, y, len(x)-1, len(y)-1)
