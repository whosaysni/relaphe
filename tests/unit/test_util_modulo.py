import pytest
from relaphe.util.modulo import Modulo
from itertools import cycle

d = lambda s: [int(c) for c in s]


modulo_cases = [
    # label, weights, divisor, use_subtract, digits, result
    # modulo 10
    ('ean13', [1, 3], 10, True, d('400763000011'), 6),
    ('ean14', [3, 1], 10, True, d('0400763000011'), 6),
    ('code25', [3, 1], 10, True, d('12345'), 7),
    ('leitcode', [4, 9], 10, True, d('2366901201230'), 5),
    # modulo 11
    ('pzn', [2,3,4,5,6,7], 11, False, d('631942'), 9),
    ('isbn10', [10, 9, 8, 7, 6, 5, 4, 3, 2], 11, True, d('392844404'), 2),
    ('isbn10', [10, 9, 8, 7, 6, 5, 4, 3, 2], 11, True, d('392844400'), 10),
    # modulo 16
    ('codabar', [1], 16, True, [16, 7, 8, 9, 16], 8),
    # modulo 43
    ('code39', [1], 43, False, [1, 5, 9, 10, 35], 17),
    # modulo 47
    ('code93', [7, 6, 5, 4, 3, 2, 1], 47, False, [12, 24, 13, 14, 38, 9, 3], 14),
    ('code93e', [8, 7, 6, 5, 4, 3, 2, 1], 47, False, [12, 24, 13, 14, 38, 9, 3, 14], 0),
]
@pytest.mark.parametrize(
    'label, weights, divisor, use_subtract, digits, result',
    modulo_cases
)
def test_modulo(label, weights, divisor, use_subtract, digits, result):
    checksum_func = Modulo(weights, divisor, use_subtract)
    assert checksum_func(digits) == result

