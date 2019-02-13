class Person:
    def __init__(self, first, last, age, gender, TSH):
        self.first = first
        self.last = last
        self.age = age
        self.Gender = gender
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
        TSH = TSHraw[4:]
        Person_List.append(Person(First, Last, Age, Gender, TSH))
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

if __name__ == "__main__":
    Person_List = read_file()
    vec = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in vec:
        print(Person_List[i].first)
        print(Person_List[i].last)
        print(Person_List[i].age)
        print(Person_List[i].TSH)
