#! /usr/bin/env python3

import sys

from typing import (Callable)
import typing
from fractions import (Fraction)


EPSILON = 10e-6
MAX_ITERATIONS = 100

def newtons_method(f, df, x_n, eps=EPSILON):

    n = 0

    next_x_n = x_n + 1000 * eps
    while abs(x_n - next_x_n) > eps and n < MAX_ITERATIONS:
        n += 1

        x_n = next_x_n
        next_x_n = x_n - (f(x_n) / df(x_n))

    return n, x_n


def main():