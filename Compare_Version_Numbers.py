#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1_len = version1.count('.')
        v2_len = version2.count('.')
        max_len = max(v1_len, v2_len)
        # 补齐
        v1 = version1 + '.0' * (max_len - v1_len)
        v1 = [int(x) for x in v1.split('.')]
        v2 = version2 + '.0' * (max_len - v2_len)
        v2 = [int(x) for x in v2.split('.')]
        for i in range(len(v1)):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
            else:
                continue
        return 0
