import argparse
import logging
from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        cls._validate_author(author)
        instance = super(MyStr, cls).__new__(cls, value)
        instance.author = author
        instance.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return instance

    @staticmethod
    def _validate_author(author):
        if not (author.isalpha() and author.istitle()):
            raise ValueError(f'Invalid author: {author}. Автор должен состоять из букв и начинаться с заглавной буквы.')

    def __str__(self):
        return f"{super().__str__()} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr('{super().__str__()}', '{self.author}')"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MyStr operations")
    parser.add_argument("--value", type=str, help="Value for MyStr instance")
    parser.add_argument("--author", type=str, help="Author for MyStr instance")

    args = parser.parse_args()

    logging.basicConfig(level=logging.NOTSET)

    try:
        mystr_instance = MyStr(args.value, args.author)
        logging.info("Создан экземпляр MyStr: %s", mystr_instance)
    except ValueError as e:
        logging.error(str(e))

# Введите в терминал:
# python lesson_15_task_1.py --value "123132" --author "John Doe9"
