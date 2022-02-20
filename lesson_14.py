"getter"
"setter"
"deleter"


class User:
    """
    Class that describes web-site user
    """

    def __init__(self, login):
        self._login = login
        self.__password = ''

    @property
    def password(self):
        hidden = "".join(["*" for _ in range(len(self.__password))])
        return hidden

    @password.setter
    def password(self, p):
        if len(p) < 6:
            raise ValueError("Password can't be shorter then 6 symbols")
        self.__password = p

    @password.deleter
    def password(self):


        raise AttributeError("Password can't be deleted!")


def modify_text(text: str):
    """
    Modify input text.

    """
    modify_text.count = len(text)

    text = text.lower()

    def slice(step):
        return text[::step]

    def lower_last_2():
        return text.lower()[-2:]

    print(text)

    def data():
        return text

    data.slice = slice
    data.lower_last = lower_last_2

    return data


t = "JDfijbfdijsIUABDu"
# lower_text = modify_text(t)
# print(modify_text.count)

T = modify_text(t)

n = [1,2,3,4,5]

from typing import List


def sum_2(numbers: List[int]) -> int:
    return sum(numbers)









