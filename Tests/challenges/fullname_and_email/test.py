import unittest

from Fullname_and_Email import Employee

class TestEmployee(unittest.TestCase):
    def test_fullname_and_email(self):
        emp_1 = Employee("John", "Smith")
        emp_2 = Employee("Mary",  "Sue")
        emp_3 = Employee("Antony", "Walker")
        emp_4 = Employee("Joshua", "Senoron")

        self.assertEquals(emp_1.firstname, "John")
        self.assertEquals(emp_1.lastname, "Smith")
        self.assertEquals(emp_1.fullname, "John Smith")
        self.assertEquals(emp_1.email, "john.smith@company.com")
        
        self.assertEquals(emp_2.firstname, "Mary")
        self.assertEquals(emp_2.lastname, "Sue")
        self.assertEquals(emp_2.fullname, "Mary Sue")
        self.assertEquals(emp_2.email, "mary.sue@company.com")
        
        self.assertEquals(emp_3.firstname, "Antony")
        self.assertEquals(emp_3.lastname, "Walker")
        self.assertEquals(emp_3.fullname, "Antony Walker")
        self.assertEquals(emp_3.email, "antony.walker@company.com")
        
        self.assertEquals(emp_4.firstname, "Joshua")
        self.assertEquals(emp_4.lastname, "Senoron")
        self.assertEquals(emp_4.fullname, "Joshua Senoron")
        self.assertEquals(emp_4.email, "joshua.senoron@company.com")
        

if __name__ == "__main__":
    unittest.main()
    