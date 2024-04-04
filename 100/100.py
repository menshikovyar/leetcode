'''
    Условие:
        Учитывая корни двух двоичных деревьев p и q, напишите функцию, проверяющую, совпадают они или нет.
        Два двоичных дерева считаются одинаковыми, если они структурно идентичны и узлы имеют одинаковое значение.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if (p and p.val) != (q and q.val):
            return False

        return (self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right))

