#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num == 0:
            return ''
        else:
            last = chr((num - 1) % 26 + ord('A'))
            head = self.convertToTitle((num - 1) / 26)
            return head + last
