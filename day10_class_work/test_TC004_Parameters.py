import tests_suite

@tests_suite.mark.parametrize("a,b,res", [(1, 2, 3), (4, 5, 9)])

def test_add(a,b,res):
    print(a+b)
    assert a+b==res

@tests_suite.mark.smoke
def test_smoke():
    assert True

#@tests_suite.mark.skip(reason="Not ready")
def test_skip():
    pass