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

    Args:
        None

    Returns:
        Person_List: A class array containing first name, last name, gender,
        age, TSH levels, and thyroid diagnosis
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
        Gender = Gender.rstrip("\n")  # Remove newline character after gender
        TSHraw = info.readline()
        TSH = TSHConversion(TSHraw)  # Converts string to float
        Diagnosis = "normal thyroid function"  # Placeholder until diagnosis
        Person_List.append(Person(First, Last, Age, Gender, Diagnosis, TSH))
    info.close()
    return Person_List


def SeparateFirstLast(Name):
    """
    This function accepts input in the format "Firstname Lastname\n" and
    separates the string into two separate strings, "Firstname" and "Lastname"

    Args:
        FullName: The full two-word string

    Returns:
        First: First name, the first word in the string
        Last: Last name, the second word in the string
    """
    FullName = Name.split(" ")  # Split string by space
    First = FullName[0]
    Last = FullName[1]
    Last = Last.rstrip("\n")  # Remove newline character after last name
    return [First, Last]


def TSHConversion(TSHraw):
    """
    This function takes a string input and converts
    into an array of floats.

    Args:
        TSHraw: a string with format TSH, 1, 2, 3...

    Returns:
        TSH: The floating point list [1, 2, 3...]

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
    This function takes the class Person and diagnoses the thyroid function
    of the individual based on the variable TSH in the class Person

    Args:
        Person_List: a list containing elements of the class Person. This
        class contains the variable Person.TSH, which will be used for
        diagnosis

    Returns:
        Person_List: the same list containing elements of class Person. Only
        the class variable Person.Diagnosis will be affected

        Person.Diagnosis: A diagnosis of thyroid function based on the values
        of variable Person.TSH:
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


def Export_Data(Person_List):
    """
    Writes patient data to JSON file

    Args:
        Person_List: a list of object type Person containing patient
        information

    Returns:
        None
    """
    import json
    i = 0
    while i < len(Person_List):
        person_dictionary = {"First Name": Person_List[i].first,
                             "Last Name": Person_List[i].last,
                             "Gender": Person_List[i].Gender,
                             "Diagnosis": Person_List[i].Diagnosis,
                             "TSH": Person_List[i].TSH}
        filename = Person_List[i].first + "-" + Person_List[i].last+".json"
        out_file = open(filename, "w")
        json.dump(person_dictionary, out_file)
        out_file.close()
        i = i+1


def main():
    Person_List = read_file()
    Person_List = DiagnoseThyroid(Person_List)
    Export_Data(Person_List)


if __name__ == "__main__":
    main()
