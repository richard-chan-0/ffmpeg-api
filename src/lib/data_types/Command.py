from typing import Iterable


class Command:
    __command: Iterable[str] = []

    def __init__(self):
        pass

    def __init__(self, command):
        self.__command = command

    def __str__(self):
        return " ".join(self.__command)

    def get_command(self):
        return self.__command
