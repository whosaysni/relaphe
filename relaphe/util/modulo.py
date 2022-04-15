# Modulo checksum algorithms
from typing import Generator


class Modulo:
    """Modulo algorithm

    >>> code25_checksum = Modulo(cycle([1, 3]), 10)
    >>> code25_checksum([1,2,3,4,5])
    7
    """

    def __init__(self, wgen: Generator, mod: int):
        """Creates modulo checksum function

        :param wgen: weight sequence generator
        :param mod: modulator
        """
        self.wgen = wgen
        self.mod = mod

    def __call__(self, digits):
        """Caluculate checksum

        :param digits: input digit sequence
        """
        return self.mod - sum(d*w for d, w in zip(digits, self.wgen))%self.mod
