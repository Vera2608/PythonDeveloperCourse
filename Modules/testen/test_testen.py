from functies import tel_op

# assert is een manier om te testen

def test_tel_op():
    assert tel_op(1,2) == 3
    assert tel_op(-1,2) == 1
    assert tel_op(11,2) == 13
    assert tel_op(0,0) == 0