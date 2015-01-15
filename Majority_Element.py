#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        threshold = len(num) / 2
        s = {}
        for x in num:
            s[x] = s.get(x, 0) + 1
            if s[x] > threshold:
                r = x
                break
        return r
