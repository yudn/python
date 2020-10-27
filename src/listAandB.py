class Solution:
    def merge(self, A, m, B, n):

        A[:] = A[:m]+B
        A.sort()
        print(A)
调用类        Solution.merge(self, A, m,B, n)
