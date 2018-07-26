class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary


emp1 = Employee("Zz", 2000)
print(getattr(emp1, 'name'))
emp1.displayEmployee()
delattr(emp1, 'name')
setattr(emp1, 'name', 'Zzz')
print(getattr(emp1, 'name'))
