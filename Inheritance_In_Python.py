"""Implement the following classes to understand inheritance in Python:

Class Name: Employee
Attributes:
id (int)
salary (int)
Constructor: __init__(self, id, salary) — Initializes the values to respective variables.
Class Name: SalesEmployee (Subclass of Employee)
Attributes:
Inherited from Employee: id, salary
New attribute: sales (int)
Constructor: __init__(self, id, salary, sales) — Calls super().__init__(id, salary) to initialize id and salary, and initializes the sales attribute.
Examples:

Input: id = 14, salary = 30000, sales = 20
Output: 
14 30000
14 30000 20"""

                                                        #CODE HERE:-

# Implement Employee and SalesEmployee classes here
class Employee:
    def __init__(self,id,salary):
        self.id = id
        self.salary = salary
    
class SalesEmployee(Employee):
    def __init__(self,id,salary,sales):
        self.id = id
        self.salary = salary
        self.sales = sales
        