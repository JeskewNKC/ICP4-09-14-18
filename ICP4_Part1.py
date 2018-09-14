class Employee:
   empCount = 0
   salary = 0

   def __init__(self, name, family, salary, department):
      self.name = name
      self.family = family
      self.salary = salary
      self.department = department
      Employee.empCount += 1
      Employee.salary = Employee.salary + salary

   def displayCount(self):
     print ("Total Employee %d") % Employee.empCount

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, ", Department: ", self.department)

class Fulltime_Employee(Employee):

    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def displayFulltimeEmp(self):
         print ("Name : ", self.name,  ", Salary: ", self.salary, ", Department: ", self.department)


emp1 = Employee("John", "Smith", 70000, "IT")
emp2 = Employee("Mike", "Jones", 85000, "HR")
emp3 = Employee("Sarah", "Johnson", 65000, "Sales")
emp1 = Fulltime_Employee("Jim", "Rose", 120000, "IT")
print('Part-time Employees:')
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print('\nFull-time Employees:')
emp1.displayFulltimeEmp()
print ('\nTotal Employee',Employee.empCount)
print ('Average salary is: $',(Employee.salary//Employee.empCount))
# print ('Total Employee', {}).format(Employee.empCount)



