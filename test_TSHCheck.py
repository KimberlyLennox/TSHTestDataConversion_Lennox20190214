import pytest


@pytest.fixture
def load_class():
    import TSHCheck
    from TSHCheck import read_file
    Person_List = read_file()
    i = 0
    return Person_List


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


def test_Diagnosis1(load_class):
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[0].Diagnosis == "normal thyroid function"


def test_Diagnosis2(load_class):
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[1].Diagnosis == "hyperthyroidism"


def test_Diagnosis3(load_class):
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[3].Diagnosis == "hypothyroidism"
