import argparse
import logging


class InvalidNameError(ValueError):
    pass


class InvalidAgeError(ValueError):
    pass


class InvalidIdError(ValueError):
    pass


class Person:
    def __init__(self, last_name, first_name, middle_name, age):
        try:
            self._validate_name(last_name, "Фамилия")
            self._validate_name(first_name, "Имя")
            self._validate_name(middle_name, "Отчество")
            self._validate_age(age)
        except (InvalidNameError, InvalidAgeError) as e:
            logging.error(str(e))
            raise e

        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.age = age

    def _validate_name(self, name, field_name):
        if not isinstance(name, str) or not name:
            raise InvalidNameError(f'Неверное {field_name.lower()}: {name}. {field_name} должно быть непустой строкой.')

    def _validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f'Неверный возраст: {age}. Возраст должен быть положительным целым числом.')

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def __str__(self):
        return f'Person: {{"Фамилия": "{self.last_name}", "Имя": "{self.first_name}", "Отчество": "{self.middle_name}", "Возраст": {self.age}}}'


class Employee(Person):
    def __init__(self, last_name, first_name, middle_name, age, employee_id):
        try:
            super().__init__(last_name, first_name, middle_name, age)
            self._validate_id(employee_id)
        except (InvalidIdError, InvalidNameError, InvalidAgeError) as e:
            raise e

        self.employee_id = employee_id

    def _validate_id(self, employee_id):
        if not isinstance(employee_id, int) or not (100000 <= employee_id <= 999999):
            raise InvalidIdError(f'Неверный идентификатор: {employee_id}. Идентификатор должен быть положительным 6-значным целым числом от 100000 до 999999.')

    def get_level(self):
        return sum(int(digit) for digit in str(self.employee_id)) % 7

    def __str__(self):
        return f'Employee: {{"Фамилия": "{self.last_name}", "Имя": "{self.first_name}", "Отчество": "{self.middle_name}", "Возраст": {self.age}, "Идентификатор": {self.employee_id}}}'


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Операции с лицом и сотрудником")
    parser.add_argument("--last_name", type=str, help="Фамилия")
    parser.add_argument("--first_name", type=str, help="Имя")
    parser.add_argument("--middle_name", type=str, help="Отчество")
    parser.add_argument("--age", type=int, help="Возраст")
    parser.add_argument("--employee_id", type=int, help="Идентификатор сотрудника")

    args = parser.parse_args()

    logging.basicConfig(level=logging.NOTSET)

    try:
        logging.info("Создание объекта Person...")
        person_instance = Person(args.last_name, args.first_name, args.middle_name, args.age)
        logging.info("Объект Person создан: %s", person_instance)
        logging.info("Процесс завершен успешно!\n")

        logging.info("Создание объекта Employee...")
        employee_instance = Employee(args.last_name, args.first_name, args.middle_name, args.age, args.employee_id)
        logging.info("Объект Employee создан: %s", employee_instance)
        logging.info("Процесс завершен успешно!")
    except (InvalidNameError, InvalidAgeError, InvalidIdError) as e:
        logging.error(str(e))

# Введите в терминал:
# python lesson_15_task_2.py --last_name "Doe" --first_name "" --middle_name "Smith" --age 30 --employee_id 123
