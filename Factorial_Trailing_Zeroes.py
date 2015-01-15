#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        x = 5
        ans = 0
        while n >= x:
            ans += n / x
            x *= 5
        return ans