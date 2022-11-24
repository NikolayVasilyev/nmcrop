#!/usr/bin/python3
"""
file: microp_1.py
author: Nikolai S. Vasil'ev
description: solving a work test from micropsi:
    Please implement a Python module, which can be installed using pip**,
    including tests, with the following functionality: Given an array of
    elements that provide a less than operator, find the minimum using as few
    comparisons as possible. The array shall be given such that the first few
    elements are strictly monotonically decreasing, the remaining elements are
    strictly monotonically increasing. The less than operator be defined as the
    operator that works on such vectors where a < b if min(a,b) == a.
"""

#  pylint: disable=C0103

from typing import List, Tuple, TypeVar
from random import randint
from logging import getLogger

LOG = getLogger("micropsi_work_test")

T = TypeVar("T")


def find_min(x: List[T]) -> T:
    """
    Find the minimum elemint in `x` using a comparison operator `op`
    """

    assert x
    x = x[:] # side effects are not welcome

    while True:
        LOG.debug("x=%r", x)

        # exit conditions
        if len(x) == 1:
            return x[0]
        if len(x) == 2:
            return x[0] if x[0] < x[1] else x[1]

        # len(x) >=3

        # base element
        m = randint(1, len(x)-2)
        LOG.debug("m=%r", m)

        # check what part is to be used in continuation
        if x[m] < x[m+1]:
            # at least we are not descending now
            if x[m+1] < x[m]:
                # x_m+1 and x_m are equal, get rid of it and start again
                x.pop(m+1)
                continue
            # increasing, the target is on the left
            x = x[:m+1]
            continue
        # descending, the target is on the right
        x = x[m+1:]


class A:
    """
    class implements a finite partial ordered objects with the formula:
    `min(a,b) == a => a < b`.
    """
    instances = {}
    compare_counter = 0

    def __new__(cls):
        val = randint(0, 9)
        if val in cls.instances:
            return cls.instances[val]

        # inst = type("A", (A, ), {"_val": val})
        inst = super(A, cls).__new__(cls)
        inst.__dict__.update({"_val": val})
        cls.instances.update({val: inst})

        return inst

    def get_val(self):
        """getter"""
        return self._val

    def __lt__(self, other):
        A.compare_counter += 1
        return min(self._val, other.get_val()) == self._val

    def __str__(self):
        return f"A:{self._val}"

    def __repr__(self):
        return str(self)


def create_sequence(L: int) -> Tuple[T, List[T]]:
    """
    generate an array match the task requirements
    NOTE:
      there are some difficulties with creating
      `strictly monotonically` sequences when a comparison operator gives us
      partially ordered units only;
    Return a tuple with two elements: a minimum element and a list of objects
    """
    left, right = (
        sorted(
            (x_:=[A()for _ in range(L)])[:(i:=randint(0, L-1))],
            reverse=True),
        sorted(x_[i:]))
    LOG.debug("left = %r, right = %r", left, right)

    x_ast = min(*[ ([left[-1]] if left else []) + ([right[0]] if right else []) ])
    LOG.debug("x_ast = %r", x_ast)

    return (x_ast, left + right)


def main():
    """playground"""

    A.compare_counter = 0
    L = 100

    for L in [10, 100, 1000, 10000]:
        stats = []
        for _ in range(1000):

            x_ast, x = create_sequence(L)
            LOG.debug("x=%r", x)

            A.compare_counter = 0
            res = find_min(x)
            assert res is x_ast, f"{res=}, {x_ast=}"

            LOG.debug("min(x=%r) = %r", x, res)

            del x, res, x_ast
            stats.append(A.compare_counter)
            A.compare_counter = 0

        LOG.info("mean compares: %r, vector of sizes: %r", sum(stats)/len(stats), L)
