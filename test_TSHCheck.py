import pytest


@pytest.fixture
def load_class():
    import TSHCheck
    from TSHCheck import read_file
    Person_List = read_file()
    i = 0
    return Person_List


def test_SepFirstLast():
    """
    Tests the ability of the function to separate first and last name

    Args: none

    Returns:
    Confirms that the test string has been separated into two separate strings
    """
    from TSHCheck import SeparateFirstLast
    sep = SeparateFirstLast("Bob Smith")
    out = ["Bob", "Smith"]
    assert sep == out


def test_SepFirstLast2():
    """
    Tests the ability of the function to remove newline characters

    Args: none

    Returns:
    Confirms that newline character from test case is no longer present
    """
    from TSHCheck import SeparateFirstLast
    sep = SeparateFirstLast("Bob Smith\n")
    out = ["Bob", "Smith"]
    assert sep == out


def test_TSHConversion():
    """
    Tests the ability of TSHConversion() to convert string into float

    Args: none

    Returns:
        Confirms that output is a list of floats with no special characters
    """
    from TSHCheck import TSHConversion
    raw = "TSH, 1, 2.2, 3, 4, 5\n"
    soln = [1., 2.2, 3., 4., 5.]
    out = TSHConversion(raw)
    assert soln == out


def test_Diagnosis1(load_class):
    """
    Tests accuracy of diagnosis returned by DiagnoseThyroid()

    Args: load_class, fixture created from test_data.txt

    Returns:
    Confirms diagnosis of first patient
    """
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[0].Diagnosis == "normal thyroid function"


def test_Diagnosis2(load_class):
    """
    Tests accuracy of diagnosis returned by DiagnoseThyroid()

    Args: load_class, fixture created from test_data.txt

    Returns:
    Confirms diagnosis of second patient
    """
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[1].Diagnosis == "hyperthyroidism"


def test_Diagnosis3(load_class):
    """
    Tests accuracy of diagnosis returned by DiagnoseThyroid()

    Args: load_class, fixture created from test_data.txt

    Returns:
    Confirms diagnosis of fourth patient
    """
    from TSHCheck import DiagnoseThyroid
    load_class = DiagnoseThyroid(load_class)
    assert load_class[3].Diagnosis == "hypothyroidism"
