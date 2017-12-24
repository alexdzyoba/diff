# diff

Simple diff utility written in Python. It's based on a trivial solution of the
Longest Common Subsequence problem.

Launch it via `diff.py` script.

```
$ python3 diff.py f1 f2
+ """Simple diff based on LCS solution"""
+ 
+ import sys
  from lcs import lcslen
  
  def print_diff(c, x, y, i, j):
+     """Print the diff using LCS length matrix by backtracking it"""
+ 
       if i >= 0 and j >= 0 and x[i] == y[j]:
           print_diff(c, x, y, i-1, j-1)
           print("  " + x[i])
       elif j >= 0 and (i == 0 or c[i][j-1] >= c[i-1][j]):
           print_diff(c, x, y, i, j-1)
-          print("+ " +  y[j])
+          print("+ " + y[j])
       elif i >= 0 and (j == 0 or c[i][j-1] < c[i-1][j]):
           print_diff(c, x, y, i-1, j)
           print("- " + x[i])
       else:
-          print("")
- 
+         print("")  # pass?
```
