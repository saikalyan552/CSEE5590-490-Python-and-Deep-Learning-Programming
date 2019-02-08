class Employee():

    empCount = 0
    SumSalary =0
    Avg =0

    def __init__(self, eid, name, salary, dep):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.dep = dep
        Employee.empCount += 1
        Employee.SumSalary += self.salary

    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", dep: ", self.dep)


# Create a Fulltime Employeeclass and it should inherit the properties of Employee classe
class FullTimeEmp(Employee):
    def __init__(self, eid, name, salary, dep, exp):
        Employee.__init__(self, eid, name, salary, dep)
        self.exp = exp
    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", dep: ", self.dep, ",Experience:", self.exp)


# below This would create first object of Employee class"
emp1 = Employee(1, "kalyan", 10000, 10)
# below This would create second object of Employee class"
emp2 = Employee(2, "sai", 6000, 20)
emp3=FullTimeEmp(3, "vytla", 3000, 20, 6)


# Total employee and average salary
print("Total Employees %d" % Employee.empCount)
print("Average salary of the employees is", (Employee.SumSalary/Employee.empCount))
print(emp1.displayEmployee())
print(emp2.displayEmployee())
print(emp3.displayEmployee())
