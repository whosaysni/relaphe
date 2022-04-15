
def test_modulo():
    from relaphe.util.modulo import Modulo
    from itertools import cycle
    modulo10_ean13 = Modulo(cycle([1, 3]), 10)
    modulo10_ean14 = Modulo(cycle([3, 1]), 10)
    modulo10_code25 = Modulo(cycle([3, 1]), 10)
    modulo10_leitcode = modulo10_identcode = Modulo(cycle([4, 9]), 10)
    assert modulo10_ean13([4,0,0,7,6,3,0,0,0,0,1,1]) == 6
    assert modulo10_ean14([0,4,0,0,7,6,3,0,0,0,1,1]) == 6
    assert modulo10_code25([1,2,3,4,5]) == 7
    assert modulo10_leitcode([2,3,6,6,9,0,1,2,0,1,2,3,0]) == 5

    
