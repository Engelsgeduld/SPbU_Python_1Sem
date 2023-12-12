from dataclasses import dataclass


@dataclass
class State:
    transfers: dict[str, int]


@dataclass
class FSMachine:
    states: list[State]
    start_state: int
    end_states: list[int]


def create_state(state_and_condition: dict[str, int]) -> State:
    return State(state_and_condition)


def create_fs_machine(
    input_states: list[dict[str, int]], start_state, end_states: list[int]
):
    states = list(map(create_state, input_states))
    return FSMachine(states, start_state, end_states)


def state_move(current_state_index: int, token: str, fsm: FSMachine) -> int | None:
    current_state_transfers = fsm.states[current_state_index].transfers
    next_state = None
    for condition in current_state_transfers:
        if token in condition:
            next_state = current_state_transfers.get(condition)
            break
    return next_state


def iterator(fsm: FSMachine, tokens: list[str]) -> int:
    start_state = fsm.start_state
    for token in tokens:
        next_state = state_move(start_state, token, fsm)
        if next_state is None:
            return start_state
        start_state = next_state
    return start_state


def validate_string(fsm: FSMachine, string: str) -> bool:
    tokens = list(string)
    end_state = iterator(fsm, tokens)
    return end_state in fsm.end_states
