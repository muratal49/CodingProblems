#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:55:24 2022

@author: murat
"""


def generate_all_subsets(s):
    output = []

    # recursive function to generate subsets
    def _generate_all_subsets(so_far, idx):
        if idx == len(s):
            # Base case. We reached the end of the string.
            # Some characters were included into list so_far, others were not.
            # This combination/subset of characters is unique.
            # Let us convert this list of characters to a string, store it in the output.
            output.append(''.join(so_far))
            return

        # recurse after adding current and not adding current to so_far
        _generate_all_subsets(so_far, idx+1)
        _generate_all_subsets(so_far + [s[idx]], idx+1)
        

    _generate_all_subsets([], 0)

    return print(output)

s='abc'
generate_all_subsets(s)
