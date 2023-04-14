"""- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)

- Analise o problema do empregado e o cálculo do seu salário.

- A superclasse Employee representa um funcionário em tempo integral ou por hora.
A classe Employee deve ser uma classe abstrata porque existem apenas funcionários
em tempo integral e funcionários horistas, não existem empregados gerais.
A classe Employee deve ter um método concreto que retorne o nome completo de
um funcionário. Além disso, deve ter um método que calcule o salário. O método
cálcula salário deve ser um método abstrato.

Implemente:
1- A classe Employee com os atributos first_name e Last_name
- O Construtor e os métodos gets e sets
- O método concreto full_name
- O método abstrato compute_salary
5- Um objeto da classe Employee
- A classe FulltimeEmployee com os atributos first_name, Last_name e salary
- O Construtor e os métodos gets e sets
- A RN do salário é o salário fixo mais um bônus de 200 reais
- Um objeto da classe FulltimeEmployee
- A classe HourlyEmployee com os atributos first_name, Last_name, worked_hours, value
- O Construtor e os métodos gets e sets
- A RN do salário é worked_hours vezes value
- Um objeto da classe HourlyEmployee
- A classe Payroll com o atributo employee_list
- O construtor não recebe nada e o método get_employee_list
- O método add para adicionar um empregado a lista
- Adicione os obejtos criados (os empregados) a lista de Payroll
- O método print_payroll que mostra a folha de pagamento com o nome completo e
o salário do funcionário."""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, f_name):
        self.first_name = f_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, l_name):
        self.last_name = l_name

    def full_name(self):
        full_name = self.get_first_name() + " " + self.get_last_name()
        return full_name

    @abstractmethod
    def compute_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        self.salary = salary
        super().__init__(first_name, last_name)

    def get_salary(self):
        return self.salary

    def set_salary(self, n_salary):
        self.salary = n_salary

    def compute_salary(self):
        return self.salary + 200

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, worked_hours, value):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.value = value

    def get_worked_hours(self):
        return self.worked_hours

    def set_worked_hours(self, n_worked_hours):
        if isinstance(n_worked_hours, int) and n_worked_hours > 0:
            self.worked_hours = n_worked_hours
        else:
            print("Essa hora não é válida")

    def get_value(self):
        return self.value

    def set_value(self, n_value):
        if isinstance(n_value, float) and n_value > 0:
            self.value = n_value

    def compute_salary(self):
        salario = self.get_worked_hours() * self.get_value()
        return salario

class Payroll(object):
    def __init__(self):
        self.employee_list = []

    def get_employee_list(self):
        return self.employee_list

    def add(self, employee):
        self.employee_list.append(employee)

    def print_payroll(self):
        print("Employees list:\n")
        payroll_list = self.get_employee_list()
        total = 0
        for employee in payroll_list:
            print(f"Employee Name: {employee.full_name()}\nEmployee Salary: {employee.compute_salary()}")
            total += employee.compute_salary()

        print(f"Total: {total} ")




if __name__ == '__main__':
    #employee1 = Employee("Robert", "Martins")
    fulltime1 = FullTimeEmployee("Pedro", "Jaber", 800)
    hourly1 = HourlyEmployee("Bruno", "Henrique", 160, 25.0)
    lista1 = Payroll()
    print(f"First Name: {fulltime1.get_first_name()}\nLastname: {fulltime1.get_last_name()}\nSalary: {fulltime1.get_salary()}")
    print(f"{fulltime1.full_name()}")
    print(f"Salário com bônus: {fulltime1.compute_salary()}")
    print(f"Name: {hourly1.full_name()}\nWorked hours: {hourly1.get_worked_hours()}\nValue per hour: {hourly1.get_value()}")
    print(f"Salário total do {hourly1.full_name()}: {hourly1.compute_salary()}")
    lista1.add(hourly1)
    lista1.add(fulltime1)
    print("")
    lista1.print_payroll()



