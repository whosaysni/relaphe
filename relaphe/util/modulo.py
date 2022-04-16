# Modulo checksum algorithms
from itertools import cycle
from typing import List


MAX_DIGITS = 128  # prevents endless input digits


class Modulo:
    """Modulo algorithm

    >>> weights = [w for i, w in zip(cycle([1, 3]), range(5))]
    >>> code25_checksum = Modulo(weights, 10)
    >>> code25_checksum([1, 2, 3, 4, 5])
    7
    """

    def __init__(self, weights: List[int], divisor: int, use_subtract=True):
        """Creates modulo checksum function

        Weights are repeated if shorter than input digits.
        (ex. 1,3,1,3,1,3,1,3... can be expressed as [1,3].

        :param weights: Weight vector
        :param divisor: Divisor for divmod operation
        :param subtract: If true, use subtract from divisor instead of remains
        """
        self.weights = weights
        self.divisor = divisor
        self.use_subtract = use_subtract

    def weighted_sum(self, digits: List[int]) -> int:
        """Calculate weighted sum for given digits

        :param digits: Input digit sequence
        """
        return sum(
            d * w for d, w, i in zip(digits, cycle(self.weights), range(MAX_DIGITS))
        )

    def __call__(self, digits: List[int]):
        """Caluculate checksum

        :param digits: Input digit sequence
        """
        remains = self.weighted_sum(digits) % self.divisor
        return (self.divisor - remains) % self.divisor if self.use_subtract else remains
