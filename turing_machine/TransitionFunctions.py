from turing_machine.helpers.Constants import STATE_TYPES, SYMBOL_TYPES, MOVEMENT_TYPES
import turing_machine.helpers.Exceptions as Exceptions


class TransitionFunctions:

    def __init__(self, transition_functions):
        """
        TransitionFunctions constructor

        :param transition_functions: (dict)
        """
        if not isinstance(transition_functions, dict):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid transition functions data type",
                "expected data type": "dictionary",
                "transition functions": transition_functions
            })

        if not transition_functions:
            raise Exceptions.TuringMachineDataTypeException({
                "message": "transition functions must contains at least 1 transition function",
                "transition functions": transition_functions
            })

        for transition_function_domain, transition_function_range in transition_functions.items():
            self._validate_transition_function(transition_function_domain, transition_function_range)

        self._transition_functions = transition_functions

    def _validate_transition_function(self, transition_function_domain, transition_function_range):
        """
        Validates the structure of the transition function according to the designed context free language.

        BNF:
          <transition_function> ::= <transition_function_domain> : <transition_function_range>;
          <transition_function_domain> ::= (<state>, <symbol>);
          <transition_function_range> ::= (<state>, <symbol>, <movement>);

          <state> ::= <string> | <integer>;
          <symbol> ::= <integer>;
          <movement> ::= LEFT | RIGHT;

        :param transition_function_domain: (tuple)
        :param transition_function_range: (tuple)
        :return: (None)
        """

        if not isinstance(transition_function_domain, tuple):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid transition function domain data type",
                "expected data type": "tuple",
                "transition function domain": transition_function_domain
            })

        if len(transition_function_domain) != 2:
            raise Exceptions.TuringMachineTransitionFunctionException({
                "message": "invalid transition function domain",
                "expected format": "(in_state, in_symbol)",
                "transition function domain": transition_function_domain
            })

        in_state, in_symbol = transition_function_domain

        if not isinstance(in_state, STATE_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid input state data type in transition function",
                "expected data type": "string or integer",
                "input state": in_state
            })

        if not isinstance(in_symbol, SYMBOL_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid input symbol data type in transition function",
                "expected data type": "string",
                "input symbol": in_symbol
            })

        if not isinstance(transition_function_range, tuple):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid transition function range data type",
                "expected data type": "tuple",
                "transition function range": transition_function_range
            })

        if len(transition_function_range) != 3:
            raise Exceptions.TuringMachineTransitionFunctionException({
                "message": "invalid transition function range",
                "expected format": "(out_state, out_symbol, movement)",
                "transition function range": transition_function_range
            })

        out_state, out_symbol, movement = transition_function_range

        if not isinstance(out_state, STATE_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid output state data type in transition function",
                "expected data type": "string or integer",
                "output state": out_state
            })

        if not isinstance(out_symbol, SYMBOL_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid output symbol data type in transition function",
                "expected data type": "string",
                "output symbol": out_symbol
            })

        if not isinstance(movement, MOVEMENT_TYPES):
            raise Exceptions.TuringMachineDataTypeException({
                "message": "invalid movement data type in transition function",
                "expected data type": "turing_machine.Movement",
                "movement": movement
            })

    def __getitem__(self, transition_function):
        """
        Fetches the transition function co-domain based on transition function domain.
        \delta (state_0, symbol_0) -> (state_1, symbol_1, movement)

        :param transition_function: (tuple)
        :return: (tuple)
        """

        if transition_function not in self._transition_functions:
            raise Exceptions.TuringMachineTransitionFunctionException({
                "message": "unknown transition function",
                "transition functions": self._transition_functions,
                "transition function": "delta{0}".format(transition_function)
            })

        return self._transition_functions[transition_function]
