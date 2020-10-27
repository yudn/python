class Solution:
    def merge(self, A, m, B, n):

        A[:] = A[:m]+B
        A.sort()
        print(A)
        Solution.merge(self, A, m,B, n)
