class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = income_dict


income_dict = {"wage": 100, "bonus": 200}


class Position(Worker):
    def get_full_name(self):
        fullname = self.name + ' ' + self.surname
        print(fullname)

    def get_total_income(self):
        total_income = income_dict["wage"] + income_dict['bonus']
        print(total_income)


misha = Position('Миша', 'Семенов', 'упаковщик')
misha.get_full_name()
misha.get_total_income()
