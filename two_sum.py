#!/usr/bin/env python
# -*- coding: utf-8 -*-

# problem:https://oj.leetcode.com/problems/two-sum/

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num_dic = {}
        for i, x in enumerate(num):
            if target-x in num_dic:
                return num_dic[target-x], i
            else:
                num_dic[x] = i
