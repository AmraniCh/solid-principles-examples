
class TimeSheetReport:

    def print(self, employee) -> None:
        print("time sheet report printing for employee {} ...".format(employee.name))
        return

class Employee:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role

employee1 = Employee("Shakir", "Software Developer")
timeSheetReport = TimeSheetReport()
timeSheetReport.print(employee1)
