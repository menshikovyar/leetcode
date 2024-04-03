'''
    Условие:
        Учитывая заголовки двух односвязных списков headA и headB, верните узел,
        в котором эти два списка пересекаются. Если два связанных списка вообще
        не пересекаются, верните null.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pointerA, pointerB = headA, headB
        while pointerA != pointerB:
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA

        return pointerA


