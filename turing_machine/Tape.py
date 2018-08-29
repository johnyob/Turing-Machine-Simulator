import turing_machine.helpers.Exceptions as Exceptions
from turing_machine.helpers.Constants import BLANK


class Tape:

    def __init__(self, tape):
        """
        Tape constructor

        :param tape: initial tape contents (string)
        """

        if not isinstance(tape, str):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid data type for tape",
                "expected data type": "string",
                "data type": type(tape)
            })

        self._tape = dict(enumerate(tape))

    def __str__(self):
        """
        Fetches the string representation of the contents of the tape

        :return: (string)
        """

        return "".join([
            self[i] for i in range(
                min(self._tape.keys()),
                max(self._tape.keys()) + 1
            )
        ])

    def __getitem__(self, key):
        """
        Fetches the symbol stored in position :param key in the type.
        If no symbol is stored in position :param key then the BLANK symbol is returned

        :param key: (integer)
        :return: (string)
        """

        return self._tape.get(key, BLANK)

    def __setitem__(self, key, value):
        """
        Sets the symbol stored at position :param key to :param value

        :param key: (integer)
        :param value: (string)
        :return: (None)
        """

        self._tape[key] = value
