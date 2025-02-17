
class Employee:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role

    def printTimeSheetReport(self) -> None:
        print("time sheet report printing for employee {} ...".format(self.name))
        return

employee1 = Employee("Shakir", "Software Developer")
employee1.printTimeSheetReport()
