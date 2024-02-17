class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, aumento=5000):
        """Soma 5000 dólares ao salario anual."""
        self.annual_salary += aumento
