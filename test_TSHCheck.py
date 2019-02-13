def test_SepFirstLast():

    from TSHCheck import SeparateFirstLast
    sep = SeparateFirstLast("Bob Smith")
    out = ["Bob", "Smith"]
    assert sep == out


def test_SepFirstLast2():

    from TSHCheck import SeparateFirstLast
    sep = SeparateFirstLast("Bob Smith\n")
    out = ["Bob", "Smith"]
    assert sep == out


def test_TSHConversion():

    from TSHCheck import TSHConversion
    raw = "TSH, 1, 2.2, 3, 4, 5\n"
    soln = [1., 2.2, 3., 4., 5.]
    out = TSHConversion(raw)
    assert soln == out
