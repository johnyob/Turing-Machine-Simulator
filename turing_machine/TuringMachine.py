from turing_machine.helpers.Constants import STATE_TYPES, SYMBOL_TYPES, MOVEMENT_TYPES, BLANK
from turing_machine.TransitionFunctions import TransitionFunctions
import turing_machine.helpers.Exceptions as Exceptions
from turing_machine.State import State
from turing_machine.Tape import Tape


class TuringMachine:

    def __init__(
            self, states, alphabet, initial_state, accepting_states,
            rejecting_states, transition_functions, trace_flag=False
    ):
        """
        Turing Machine constructor

        :param states: set of states in the turing machine (list: (string|integer))
        :param alphabet: set of symbols in the turing machine's alphabet (list: string)
        :param initial_state: initial state of the turing machine. initial_state \in states (string|integer)
        :param accepting_states: accepting states of the turing machine. accepting_states \subseteq states (list: (string|integer))
        :param rejecting_states: rejecting states of the turing machine. rejecting_states \subseteq states (list: (string|integer))
        :param transition_functions: (dict)
        """

        if not isinstance(states, list):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid states data type",
                "expected data type": "list",
                "states": states
            })

        if not all(isinstance(state, STATE_TYPES) for state in states):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid data type for states element",
                "expected data type": "string or integer",
                "states": states
            })

        self._states = states

        if not isinstance(alphabet, list):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid alphabet data type",
                "expected data type": "list",
                "alphabet": alphabet
            })

        if not all(isinstance(symbol, SYMBOL_TYPES) for symbol in alphabet):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid data type for alphabet element",
                "expected data type": "string",
                "alphabet": alphabet
            })

        if BLANK not in alphabet:
            alphabet.append(BLANK)

        self._alphabet = alphabet

        if not isinstance(initial_state, STATE_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid initial state data type",
                "expected data type": "string or integer",
                "initial state": initial_state
            })

        if initial_state not in self._states:
            raise Exceptions.TuringMachineStateException({
                "message": "invalid initial state",
                "valid states": self._states,
                "initial state": initial_state
            })

        self._initial_state = initial_state

        if not isinstance(accepting_states, list):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid accepting states data type",
                "expected data type": "list",
                "accepting states": accepting_states
            })

        if not all(isinstance(state, STATE_TYPES) for state in accepting_states):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid data type for accepting states element",
                "expected data type": "string or integer",
                "accepting states": accepting_states
            })

        if not set(accepting_states).issubset(self._states):
            raise Exceptions.TuringMachineStateException({
                "message": "accepting states set is not a subset of states",
                "valid states": self._states,
                "accepting states": accepting_states
            })

        self._accepting_states = accepting_states

        if not isinstance(rejecting_states, list):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid rejecting states data type",
                "expected data type": "list",
                "rejecting states": rejecting_states
            })

        if not all(isinstance(state, STATE_TYPES) for state in rejecting_states):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid data type for rejecting states element",
                "expected data type": "string or integer",
                "rejecting states": rejecting_states
            })

        if not set(rejecting_states).issubset(self._states):
            raise Exceptions.TuringMachineStateException({
                "message": "rejecting states set is not a subset of states",
                "valid states": self._states,
                "rejecting states": rejecting_states
            })

        self._rejecting_states = rejecting_states
        self._transition_functions = TransitionFunctions(transition_functions)
        self._trace_flag = trace_flag

    def _trace(self, current_state, tape, head_location):
        """
        Displays tracing for the turing machine. Outputs the current state, the contents of the tape and the visual
        position of the read/write head along the tape.

        :param current_state: the current state of the turing machine (integer|string)
        :param tape: infinite tape for the turing machine (Tape)
        :param head_location: read/write head location pointer (integer)
        :return: (None)
        """

        print("\nCurrent state: {0}".format(current_state))
        print("Tape:")
        print(tape)
        print(" " * head_location + "^")

    def _accepted(self, current_state):
        """
        Returns whether the :param current_state is a member of the accepting states set

        :param current_state: (integer|string)
        :return: (boolean)
        """

        return current_state in self._accepting_states

    def _rejected(self, current_state):
        """
        Returns whether the :param current_state is a member of the rejecting states set

        :param current_state: (integer|string)
        :return: (boolean)
        """

        return current_state in self._rejecting_states

    def _run(self, tape):
        """
        Run method for turing machine.
        Executes transition functions based on :param tape

        :param tape: initial tape string(string)
        :return: (State)
        """

        tape = Tape(tape)
        current_state = self._initial_state
        head_location = 0

        while True:

            if self._trace_flag:
                self._trace(current_state, tape, head_location)

            if self._accepted(current_state):
                return State.ACCEPTED

            if self._rejected(current_state):
                return State.REJECTED

            symbol = tape[head_location]
            out_state, out_symbol, movement = self._transition_functions[(
                current_state, symbol
            )]

            if out_state not in self._states:
                raise Exceptions.TuringMachineStateException({
                    "message": "invalid output state",
                    "valid states": self._states,
                    "output state": out_state
                })

            if out_symbol not in self._alphabet:
                raise Exceptions.TuringMachineSymbolException({
                    "message": "output symbol not in alphabet",
                    "alphabet": self._alphabet,
                    "output symbol": out_symbol
                })

            if not isinstance(movement, MOVEMENT_TYPES):
                raise Exceptions.TuringMachineMovementException({
                    "message": "invalid read/write head movement",
                    "movement": movement
                })

            tape[head_location] = out_symbol
            current_state = out_state
            head_location += movement

    def execute(self, tape):
        """
        Executes the turing machine using the contents of :param tape and displays the reason why the turing machine
        halts, if it halts

        :param tape: initial tape contents (string)
        :return: (None)
        """

        accepted = self.accepts(tape)

        print("\nTuring Machine: Halted")
        print("Reason for halting: moved into {0} state".format(
            "accepting" if accepted else "rejecting"
        ))

    def accepts(self, tape):
        """
        Displays whether turing machine moves into an accepting state

        :param tape: initial tape string (string)
        :return: (boolean)
        """

        return self._run(tape) == State.ACCEPTED

    def rejects(self, tape):
        """
        Returns whether turing machine moves into a rejecting state

        :param tape: initial tape string (string)
        :return: (boolean)
        """

        return self._run(tape) == State.REJECTED



