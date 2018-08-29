from enum import Enum


class State(Enum):
    ACCEPTED = 1
    REJECTED = 2
    REACHED_STEP_LIMIT = 3

