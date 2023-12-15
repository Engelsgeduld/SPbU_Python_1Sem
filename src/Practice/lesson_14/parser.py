import sys
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

# Я ВЕЛИКИЙ ГРЕШНИК И ПРОШУ У ВАС И ВАШИХ ГЛАЗ ПРОЩЕНИЯ

Value = TypeVar("Value")


@dataclass
class Node(Generic[Value]):
    terminal: bool
    value: Value
    children: Optional[list["Node[Value]"]] = None


@dataclass
class ParseTree(Generic[Value]):
    root: Optional[Node[Value]] = None


def parse(tokens: list[str]) -> ParseTree:
    root = start(tokens, 0)[0]
    parsed_tree = create_tree_map()
    parsed_tree.root = root
    return parsed_tree


def create_tree_map() -> ParseTree:
    return ParseTree()


def start(tokens: list[str], index: int):
    t_node, switch = func_t(tokens, index)
    sum_node, result_switch = func_sum(tokens, switch)
    return Node(False, "START", [t_node, sum_node]), result_switch


def func_t(tokens: list[str], index: int):
    token_node, switch = func_token(tokens, index)
    prod_node, res_switch = func_prod(tokens, switch)
    return (
        Node(
            False,
            "T",
            [token_node, prod_node],
        ),
        res_switch,
    )


def func_token(tokens: list[str], index: int):
    if index >= len(tokens):
        return ValueError(f"Error: Wrong operation pattern"), index
    if tokens[index].isdigit():
        return Node(False, "TOKEN", [Node(True, tokens[index])]), index + 1
    elif tokens[index] == "(":
        start_node, switch = start(tokens, index + 1)
        if switch >= len(tokens) or tokens[switch] != ")":
            return ValueError("Error: expected )"), switch
        return (
            Node(
                False,
                "Token",
                [Node(True, "("), start_node, Node(True, ")")],
            ),
            switch + 1,
        )
    elif tokens[index] == ")":
        return Node(False, "TOKEN", [Node(True, tokens[index])]), index
    return ValueError(f"Error: Unexpected token {tokens[index]}"), index


def func_prod(tokens: list[str], index: int):
    if index < len(tokens) and tokens[index] == "*":
        token_node, switch = func_token(tokens, index + 1)
        prod_node, res_switch = func_prod(tokens, switch)
        return (
            Node(
                False,
                "PROD",
                [
                    Node(True, "*"),
                    token_node,
                    prod_node,
                ],
            ),
            res_switch,
        )
    else:
        return Node(False, "PROD", [Node(True, "eps")]), index


def func_sum(tokens: list[str], index: int):
    if index < len(tokens) and tokens[index] == "+" and tokens[index] != ")":
        t_node, t_switch = func_t(tokens, index + 1)
        sum_node, sum_switch = func_sum(tokens, t_switch)
        return (
            Node(
                False,
                "SUM",
                [Node(True, "+"), t_node, sum_node],
            ),
            sum_switch,
        )
    else:
        return Node(False, "SUM", [Node(True, "eps")]), index


def pretty_print(tree: ParseTree):
    res_line = ""
    exceptions = []

    def print_recursion(cur_node, tab: int):
        nonlocal res_line
        nonlocal exceptions
        if type(cur_node) is ValueError:
            exceptions.append(cur_node)
            return
        res_line += f"{'.'*tab}{cur_node.value}\n"
        if cur_node.children is None:
            return
        for child in cur_node.children:
            print_recursion(child, tab + 3)

    print_recursion(tree.root, 0)
    if exceptions:
        for error in exceptions:
            print(error, file=sys.stderr)
    else:
        print(res_line)
