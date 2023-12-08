from dataclasses import dataclass


@dataclass
class State:
    transfers: dict[str:int]


@dataclass
class FSMachine:
    states: list[State]
    start_state: int
    end_states: list[int]


def create_state(state_and_condition: dict[str:int]) -> State:
    return State(state_and_condition)


def create_fs_machine(
    input_states: list[dict[str, int]], start_state, end_states: list[int]
):
    states = list(map(create_state, input_states))
    return FSMachine(states, start_state, end_states)


def state_move(current_state_index: int, token: str, fsm: FSMachine) -> int | None:
    current_state = fsm.states[current_state_index].transfers
    transfer = list(
        map(
            lambda condition: current_state[condition] if token in condition else None,
            list(current_state),
        )
    )
    next_state = list(filter(lambda x: x is not None, transfer))
    if len(next_state) == 0:
        return None
    return next_state[0]


def iterator(fsm: FSMachine, tokens: list[str]) -> int:
    def iterator_recursion(state_index, token_index):
        if token_index == len(tokens) or state_index is None:
            return state_index
        next_state = state_move(state_index, tokens[token_index], fsm)
        return iterator_recursion(next_state, token_index + 1)

    return iterator_recursion(fsm.start_state, 0)


def validate_string(fsm: FSMachine, string: str) -> bool:
    tokens = [*string]
    end_state = iterator(fsm, tokens)
    return end_state in fsm.end_states
