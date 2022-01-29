class User:
    base_salary = 20000

    def __init__(self, firstName, lastName, salary) -> None:
        self.first_name = firstName
        self.last_name = lastName
        self.salary = salary + self.base_salary

    @classmethod
    def update_base_salary(cls, updated_base_salary):
        cls.base_salary = updated_base_salary
        return cls.base_salary

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


print(User.update_base_salary(30000))

u1 = User("paritosh","sharma",20000)
print(u1.salary)
print(u1.get_full_name())

