#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s

        array = [''] * nRows
        for i in range(len(s)):
            index = i % (2 * nRows - 2)
            if index < nRows:
                array[index] += s[i]
            else:
                array[2 * nRows - index - 2] += s[i]

        out = ''
        for i in array:
            out = out + i
        return out


'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        n = len(s)
        len_slice = 2 * nRows - 2
        n_slice = (n - 1) / len_slice
        n_tail = n - len_slice * n_slice
        n_column_tail = 1 if n_tail <= nRows else 1 + n_tail % nRows
        n_column = n_slice * (nRows - 1) + n_column_tail

        result_matrix = [[' '] * n_column for i in range(nRows)]
        for i in range(len(s)):
            dif = i % len_slice
            rank = i / len_slice
            if dif < nRows:
                result_matrix[dif][rank * (nRows - 1)] = s[i]
            else:
                result_matrix[len_slice - dif][rank * (nRows - 1) + dif - nRows + 1] = s[i]
        result = ''
        for line in result_matrix:
            result += ''.join(line)
            result += '\n'
        return result
        '''