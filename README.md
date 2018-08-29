# Turing Machine Simulator
> A simple Python Turing machine simulator with an *infinite* tape

This is an easy-to-use Python package for simulating a Turing Machine with an *infinite* tape. The simulator allows a 
Turing machine to execute transition functions / rules and trace their execution, the package also checks whether a 
Turing machine accepts or rejects a particular input.

## Features

### Overview
- [x] Execute a Turing machine given an initial tape input
- [x] Check whether a Turing machine moves into an accepting state given an initial tape input (A value is only returned if the Turing machine halts)
- [x] Check whether a Turing machine moves into a rejecting state given an initial tape input (A value is only returned if the Turing machine halts)

### Turing Machine Entity
- [x] `initial_state`
- [x] `accepting_states`
- [x] `rejecting_states`
- [x] `states`
- [x] `alphabet`
- [x] `execute(tape: str) -> None`
- [x] `accepts(tape: str) -> bool`
- [x] `rejects(tape: str) -> bool`

## Installation
```sh
python -m pip install --no-cache-dir --index-url https://test.pypi.org/simple/ turing-machine
```

## Usage
### Overview
The `turing_machine` package contains a `TuringMachine` class which can be instantiated with a particular set of `states`,
a `alphabet`, a `initial_state`, a set of `accepting_states`, a set of `rejecting_states`, a set of `transition_function` 
and a `trace_flag` which is used to indicated whether a turing machine trace should be printed. 

Once a Turing machine has been instantiated it can be executed using the `execute` method or the Turing machine can use the 
`accepts` or `rejects` methods to check whether the machine moves into an accepting state or rejecting state, respectively, 
given a particular input *and* if the Turing machine successfully halts.

For example:
```python
from turing_machine import Movement, TuringMachine, BLANK

initial_state = 0
accepting_states = [3]
rejecting_states = []
states = [0, 1, 2, 3]
alphabet = ["0", "1"]

transition_functions = {
    (0, "0"): (0, "0", Movement.RIGHT),
    (0, "1"): (0, "1", Movement.RIGHT),
    (0, BLANK): (1, BLANK, Movement.LEFT),

    (1, "0"): (1, "0", Movement.LEFT),
    (1, "1"): (2, "1", Movement.LEFT),

    (2, "0"): (2, "1", Movement.LEFT),
    (2, "1"): (2, "0", Movement.LEFT),
    (2, BLANK): (3, BLANK, Movement.RIGHT)
}

t = TuringMachine(
    states, alphabet, initial_state, accepting_states,
    rejecting_states, transition_functions, trace_flag=True
)
t.execute("0110110")
```

Printing:

```
Current state: 0
Tape:
0110110
^

Current state: 0
Tape:
0110110
 ^

Current state: 0
Tape:
0110110
  ^

Current state: 0
Tape:
0110110
   ^

Current state: 0
Tape:
0110110
    ^

Current state: 0
Tape:
0110110
     ^

Current state: 0
Tape:
0110110
      ^

Current state: 0
Tape:
0110110
       ^

Current state: 1
Tape:
0110110_
      ^

Current state: 1
Tape:
0110110_
     ^

Current state: 2
Tape:
0110110_
    ^

Current state: 2
Tape:
0110010_
   ^

Current state: 2
Tape:
0111010_
  ^

Current state: 2
Tape:
0101010_
 ^

Current state: 2
Tape:
0001010_
^

Current state: 2
Tape:
1001010_
^

Current state: 3
Tape:
_1001010_
^

Turing Machine: Halted
Reason for halting: moved into accepting state
```

### Arguments Syntax
The `TuringMachine` class has 7 arguments:
- `states`
- `alphabet`
- `initial_state`
- `accepting_states`
- `rejecting_states`
- `transition_functions`
- `trace_flag` (Optional: default=`False`)

### States
The list of states of the Turing machine can be described using the following BNF:
```
<states> ::= [<states_list>];
<states_list> ::= <state>, <states_list> | <state>;
<state> ::= INTEGER | STRING;
```
To ensure the Turing machine executes correctly, the described list / set of states syntax must be used.

### Alphabet
The list / set of acceptable symbols of the Turing machine, known as the alphabet, can be described using the following BNF:
```
<alphabet> ::= [<symbols_list>];
<symbols_list> ::= <symbol>, <symbols_list> | <symbol>;
<symbol> ::= STRING;
```
To ensure the Turing machine executes correctly, the described alphabet syntax must be used.

The alphabet can be used to describe the set of acceptable symbols of the Turing machine, by default, the alphabet also 
contains the `BLANK` symbol (`_`) which can be accessed using `turing_machine.BLANK`.

For example:
```python
from turing_machine import BLANK

print(BLANK)
```

Printing
```python
"_"
```

### Initial State
The initial state of the Turing machine can be described using the following BNF:
```
<initial_state> ::= <state>;
```
To ensure the Turing machine executes correctly, the described initial state syntax must be used.
Furthermore the `initial_state` must be a member of the set of `states`, this condition will be checked upon instantiation.

### Accepting States
The list / set of accepting states of the Turing machine can be described using the following BNF:
```
<accepting_states> ::= <states>;
```
To ensure the Turing machine executes correctly, the described list / set of accepting states syntax must be used. 
Furthermore the `accepting_states` must be a subset of `states`, this condition will be checked upon instantiation.

### Rejecting States
The list / set of rejecting states of the Turing machine can be described using the following BNF:
```
<rejecting_states> ::= <states>;
```
To ensure the Turing machine executes correctly, the described list / set of rejecting states syntax must be used. 
Furthermore the `rejecting_states` must be a subset of `states`, this condition will be checked upon instantiation.

### Transition Functions
The list / set of transition functions of the Turing machine can be described using the following BNF:
```
<transition_functions> ::= {<transition_functions_list>};
<transition_functions_list> ::= <transition_function>, <transition_function_list> | <transition_function>;
<transition_function> ::= <transition_function_domain> : <transition_function_range>;
<transition_function_domain> ::= (<state>, <symbol>);
<transition_function_range> ::= (<state>, <symbol>, <movement>);
<movement> ::= LEFT | RIGHT;
```
To ensure the Turing machine executes correctly, the described list / set of transition functions syntax must be used.
Furthermore the syntax for `transition_functions` will be checked upon instantiation.

## Errors
If you discover an error within this package, please email [me](mailto:alistair.o'brien@ellesmere.com).

## Credits
- [Alistair O'Brien](https://github.com/johnyob)
