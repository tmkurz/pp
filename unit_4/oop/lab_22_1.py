class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def getsalary(self):
        return self.__salary

    def getfullname(self):
        return self.__firstname + " " + self.__lastname

    def getage(self):
        return self.__age

    def risesalary(self, x = 0.1):
        return self.__salary + (self.__salary * x)



employees = []
employees.append(Employee("Jan", "Kowalski", 25, 3800))
employees.append(Employee("Edmund", "Kaczmarczyk", 45, 7000))
employees.append(Employee("Natalia", "Nowak", 60, 15200))

print("Lista płac")
print("-" * 50)

for e in employees:
    print(e.getfullname(), "wiek: ", e.getage(), "lat, pensja: ", e.getsalary(), "zł.")
print()
for e in employees:
    print(e.getfullname(), "podniesiona pensja: ", e.risesalary(), "zł.")