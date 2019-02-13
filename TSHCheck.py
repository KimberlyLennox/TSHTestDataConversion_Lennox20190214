class Person:
    def __init__(self, FullName, age, gender, TSH):
        # self.first=firstname
        # self.last=lastname
        self.FullName=FullName
        self.age = age
        self.Gender = gender
        self.TSH = TSH


def read_file():
    Person_List = []
    info=open("test_data.txt", "r")
    str1="Hi";
    count=0
    while str1!="END":
        str1 = info.readline()
        if str1 == "END":
            break
        Name = str1
        FullName=Name.split(" ")

        Age = info.readline()
        Gender = info.readline()
        TSHraw = info.readline()
        TSH = TSHraw[4:]
        Person_List.append(Person(FullName, Age, Gender, TSH))
    info.close()
    return Person_List

if __name__ == "__main__":
    Person_List=read_file()
    vec=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in vec:
        print(Person_List[i].FullName)
        print(Person_List[i].age)
        print(Person_List[i].TSH)