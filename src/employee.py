from abc import ABC, abstractmethod


class Employee(ABC):
    """
    Employee abstract class
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address

    @abstractmethod
    def __str__(self):
        return (
            f"Employee(name='{self.name}', "
            f"address='{self.address}')"
        )

    @staticmethod
    def validate_number(number):
        if not type(number) in (int, float):
            raise TypeError
        if number <= 0:
            raise ValueError

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, address, salary, load_factor):
        super().__init__(name, address)
        self.salary = salary
        self.validate_number(load_factor)
        self.__load_factor = load_factor

    def __str__(self):
        return (
            f"FullTimeEmployee(name='{self.name}', "
            f"address='{self.address}', "
            f"salary={self.salary}, "
            f"load_factor={self.__load_factor})"
        )

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.validate_number(salary)
        self.__salary = salary

    def set_load_factor(self, load_factor):
        self.validate_number(load_factor)
        self.__load_factor = load_factor

    def calculate_salary(self):
        return self.__salary * self.__load_factor


class HourlyEmployee(Employee):
    def __init__(self, name, address, hours_worked, hourly_rate):
        super().__init__(name, address)
        self.validate_number(hours_worked)
        self.__hours_worked = hours_worked
        self.validate_number(hourly_rate)
        self.__hourly_rate = hourly_rate

    def __str__(self):
        return (
            f"HourlyEmployee(name='{self.name}', "
            f"address='{self.address}', "
            f"hours_worked={self.__hours_worked}, "
            f"hourly_rate={self.__hourly_rate})"
        )

    def set_hours_worked(self, hours_worked):
        self.validate_number(hours_worked)
        self.__hours_worked = hours_worked

    def set_hourly_rate(self, hourly_rate):
        self.validate_number(hourly_rate)
        self.__hourly_rate = hourly_rate

    def calculate_salary(self):
        return float(self.__hours_worked * self.__hourly_rate)


class ContractEmployee(Employee):
    def __init__(self, name, address, contract_value, contract_duration):
        super().__init__(name, address)
        self.validate_number(contract_value)
        self.__contract_value = contract_value
        self.validate_number(contract_duration)
        self.__contract_duration = contract_duration

    def __str__(self):
        return (
            f"ContractEmployee(name='{self.name}', "
            f"address='{self.address}', "
            f"contract_value={self.__contract_value}, "
            f"contract_duration={self.__contract_duration})"
        )

    def set_contract_value(self, contract_value):
        self.validate_number(contract_value)
        self.__contract_value = contract_value

    def set_contract_duration(self, contract_duration):
        self.validate_number(contract_duration)
        self.__contract_duration = contract_duration

    def calculate_salary(self):
        return self.__contract_value / self.__contract_duration


class PayrollManager:
    def __init__(self):
        self.employees = []

    def __str__(self):
        employees_list = []
        for employee in self.employees:
            employees_list.append(f"\n  {employee.__str__()}")
        return "PayrollManager([" + ",".join(employees_list) + "\n])"

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.calculate_salary()
        return total_salary

    def calculate_total_taxes(self):
        total_taxes = 0
        for employee in self.employees:
            total_taxes += self.tax_rate(employee) * employee.calculate_salary()
        return total_taxes

    @staticmethod
    def tax_rate(employee):
        return 0.1 if isinstance(employee, ContractEmployee) else 0.2

    def generate_payroll_report(self):
        payroll_report = [("Name", "Type", "Salary", "Taxes"),]
        for employee in self.employees:
            salary = employee.calculate_salary()
            taxes = self.tax_rate(employee) * salary
            payroll_report.append(
                (employee.name, type(employee).__name__, salary, taxes)
            )
        return payroll_report

    def print_payroll_report(self):
        table_width = 70
        print("Payroll Report:")
        for index, row in enumerate(self.generate_payroll_report()):
            if index == 0:
                print("-" * table_width)
            print("|{:<25}|{:<20}|{:>10}|{:>10}|".format(*row))
            if index == 0:
                print("-" * table_width)
        print("-" * table_width)
        print(f"Total salary: {self.calculate_total_salary()}")
        print(f"Total taxes: {self.calculate_total_taxes()}")


if __name__ == "__main__":
    # Приклад використання
    payroll_manager = PayrollManager()

    full_time_employee = FullTimeEmployee(
        "John Doe", "123 Main St", 5000, 0.9)
    print(full_time_employee.salary)
    full_time_employee.salary = 10000
    print(full_time_employee.salary)
    print(full_time_employee.__dict__)
    print(full_time_employee._FullTimeEmployee__load_factor)

    hourly_employee = HourlyEmployee(
        "Jane Doe", "456 Oak St", 160, 15)
    contract_employee = ContractEmployee(
        "Bob Smith", "789 Pine St", 12000, 12)

    payroll_manager.add_employee(full_time_employee)
    payroll_manager.add_employee(hourly_employee)
    payroll_manager.add_employee(contract_employee)
    print(payroll_manager, "\n")

    payroll_manager.print_payroll_report()
