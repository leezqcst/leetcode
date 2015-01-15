#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = None

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min == None:
            self.min = x
        elif self.min > x:
            self.min = x
        return x

    # @return nothing
    def pop(self):
        poped = self.stack.pop()
        if poped == self.min:
            if self.stack:
                self.min = min(self.stack)
            else:
                self.min = None
        return poped


    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None


    # @return an integer
    def getMin(self):
        return self.min
