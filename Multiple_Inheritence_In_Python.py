"""Implement the following classes to understand multiple inheritance in Python:

Class Name: Student
Attributes:
sid (int) — Student ID.
deptid (int) — Department ID.
Constructor: __init__(self, sid, deptid) — Initializes the sid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the student ID and department ID, eg., "StudentID:101 DepartmentID:42"
Class Name: Faculty
Attributes:
eid (int) — Employee ID.
deptid (int) — Department ID.
Constructor: __init__(self, eid, deptid) — Initializes the eid and deptid attributes.
Method: get_info(self) — Returns a formatted string with the employee ID and department ID, eg., "EmployeeID:555 DepartmentID:42"
Class Name: PhDStudent (Inherits from both Student and Faculty)
Constructor: __init__(self, sid, eid, deptid) — Calls the constructors of Student and Faculty to initialize sid, eid, and deptid.
Method: get_info(self) — Returns a formatted string with the student ID, employee ID and department ID, eg., "Student ID:101 EmployeeID:555 DepartmentID:42".
Example:

Input: sid = 101, eid = 555, deptid = 42
Output: 
StudentID:101 DepartmentID:42
EmployeeID:555 DepartmentID:42
Student ID:101 EmployeeID:555 DepartmentID:42"""

                                                            #CODE HERE:-

class Student:
    def __init__(self,sid,deptid):
        self.sid = sid
        self.deptid = deptid
    
    def get_info(self):
        return(f"StudentID:{self.sid} DepartmentID:{self.deptid}")

class Faculty(Student):
    def __init__(self,eid,deptid):
        self.eid = eid
        self.deptid = deptid
        
    def get_info(self):
        return(f"EmployeeID:{self.eid} DepartmentID:{self.deptid}")

class PhDStudent(Faculty):
    def __init__(self,sid,eid,deptid):
        self.sid = sid
        self.eid = eid
        self.deptid = deptid
    
    def get_info(self):
        return(f"StudentID:{self.sid} EmployeeID:{self.eid} DepartmentID:{self.deptid}")