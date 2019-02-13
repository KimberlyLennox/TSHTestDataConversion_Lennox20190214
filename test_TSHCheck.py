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
