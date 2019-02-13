class Person:
    def __init__(self, first, last, age, gender, diagnosis, TSH):
        self.first = first
        self.last = last
        self.age = age
        self.Gender = gender
        self.Diagnosis = diagnosis
        self.TSH = TSH


def read_file():
    """
    This function reads the file "test_data.txt", parses each line,
    and returns the data in class Person.
    No input required
    Outputs class array Person_List
    """
    Person_List = []
    info = open("test_data.txt", "r")
    str1 = "Hi"
    count = 0
    while str1 != "END":
        str1 = info.readline()
        if str1 == "END":
            break
        Name = str1
        [First, Last] = SeparateFirstLast(Name)
        Age = info.readline()
        Gender = info.readline()
        TSHraw = info.readline()
        TSH = TSHConversion(TSHraw)
        Diagnosis = "normal thyroid function"  # Placeholder until diagnosis
        Person_List.append(Person(First, Last, Age, Gender, Diagnosis, TSH))
    info.close()
    return Person_List


def SeparateFirstLast(Name):
    """
    This function accepts input in the format "Firstname Lastname\n" and
    separates the string into two separate strings, "Firstname" and "Lastname"
    """
    FullName = Name.split(" ")
    First = FullName[0]
    Last = FullName[1]
    Last = Last.rstrip("\n")
    return [First, Last]


def TSHConversion(TSHraw):
    """
    This function takes a string input in the form TSH, 1, 2, 3...
    and converts into an array of floats.
    """
    TSHstr = TSHraw[4:]
    TSHarray = TSHstr.split(",")
    i = 0
    while i < len(TSHarray):
        TSHarray[i] = TSHarray[i].rstrip("\n")
        i = i+1
    import numpy as np
    TSH = [float(i) for i in TSHarray]
    return TSH


def DiagnoseThyroid(Person_List):
    """
    This function takes the class Person and diagnoses the thyroid function of
    the individual based on the variable TSH in the class Person

    Hypothyroidism:
    TSH > 4.0

    Hyperthyroidism:
    TSH < 1.0

    Otherwise: normal thyroid function
    """
    i = 0
    while i < len(Person_List):
        TSH = Person_List[i].TSH
        Diagnosis = Person_List[i].Diagnosis
        TSHmax = max(TSH)
        TSHmin = min(TSH)
        if TSHmax > 4.0:
            Diagnosis = "hypothyroidism"
        elif TSHmin < 1.0:
            Diagnosis = "hyperthyroidism"
        Person_List[i].Diagnosis = Diagnosis
        i = i+1
    return Person_List


if __name__ == "__main__":
    Person_List = read_file()
    Person_List = DiagnoseThyroid(Person_List)
