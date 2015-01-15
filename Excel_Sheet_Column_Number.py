#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        seq = [ord(x) - ord('A') + 1 for x in s]
        return reduce(lambda x, y: x * 26 + y, seq)