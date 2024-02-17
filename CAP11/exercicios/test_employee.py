import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.calvin = Employee('Calvin', 'Klaus', 7200)

    def test_give_default_raise(self):
        self.calvin.give_raise()
        self.assertEqual(self.calvin.annual_salary, 12200)
    
    def test_give_custom_raise(self):
        self.calvin.give_raise(3000)
        self.assertEqual(self.calvin.annual_salary, 10200)

unittest.main()
