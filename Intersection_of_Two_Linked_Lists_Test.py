#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Intersection_of_Two_Linked_Lists import Solution
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

# b = ListNode(4)
b = ListNode(1)
b.next= ListNode(2)

s = Solution()
r = s.getIntersectionNode(a, b)
print r.val
