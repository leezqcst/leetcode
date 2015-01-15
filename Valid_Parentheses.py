#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return a boolean
    def isValid(self, s):
        open_chars = ['(', '[', '{']
        close_chars = [')', ']', '}']
        status = []
        for x in s:
            if x in open_chars:
                status.append(x)
            elif x in close_chars:
                if len(status) == 0:
                    return False
                else:
                    y = status.pop()
                    if open_chars.index(y) == close_chars.index(x):
                        continue
                    else:
                        return False
        return len(status) == 0
