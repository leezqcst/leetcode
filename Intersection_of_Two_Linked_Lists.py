#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = lenB = 0
        tempA = headA
        tempB = headB
        while tempA:
            lenA += 1
            tempA = tempA.next
        while tempB:
            lenB += 1
            tempB = tempB.next

        longer_head = headA if lenA >= lenB else headB
        shorter_head = headA if lenA < lenB else headB
        len_dif = abs(lenA - lenB)
        for i in range(len_dif):
            longer_head = longer_head.next
        while longer_head:
            if longer_head.val == shorter_head.val:
                return longer_head
            else:
                longer_head = longer_head.next
                shorter_head = shorter_head.next
        return None
