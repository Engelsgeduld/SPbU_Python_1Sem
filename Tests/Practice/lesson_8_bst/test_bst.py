from src.Practice.lesson_8.bst import *
import pytest

from src.Practice.lesson_8.bst import _valid_input_key, _insert_main_root


@pytest.fixture()
def empy_tree_initialization():
    empty_tree = create_tree_map()
    return empty_tree


@pytest.fixture()
def tree_initialization_with_values():
    keys = [5, 3, 4, 6, 8, 9, 2, 7]
    values = list(map(str, keys))
    tree = create_tree_map()
    for i in range(len(keys)):
        put(tree, keys[i], values[i])
    return tree


def test_creation_tree():
    actual = create_tree_map()
    assert actual == Tree(0)


@pytest.mark.parametrize("tree_type, key, result", ((int, 8, True), (str, 8, False)))
def test_valid_input_key(tree_type, key, result, empy_tree_initialization):
    empy_tree_initialization.type = tree_type
    assert _valid_input_key(empy_tree_initialization, key) is result


@pytest.mark.parametrize(
    "key, tree_type", ((8, str), ([1, 2], tuple), ({2, 3}, list), (1, bool))
)
def test_put_exception(key, tree_type, empy_tree_initialization):
    empy_tree_initialization.type = tree_type
    with pytest.raises(ValueError):
        put(empy_tree_initialization, key, 1)


@pytest.mark.parametrize(
    "key, values", ((5, "5"), (3, "3"), (4, "4"), (6, "6"), (8, "8"), (9, "9"))
)
def test_get_function(key, values, tree_initialization_with_values):
    actual = get(tree_initialization_with_values, key)
    assert actual == values


@pytest.mark.parametrize(
    "key, result",
    (
        (5, True),
        (3, True),
        (4, True),
        (6, True),
        (8, True),
        (9, True),
        (25, False),
        (1024, False),
    ),
)
def test_has_key(key, result, tree_initialization_with_values):
    actual = has_key(tree_initialization_with_values, key)
    assert actual == result


def test_get_exception(tree_initialization_with_values):
    with pytest.raises(ValueError):
        get(tree_initialization_with_values, 12)


def test_insert_main_root(empy_tree_initialization):
    _insert_main_root(empy_tree_initialization, 8, 12)
    assert empy_tree_initialization.root == Node(8, 12)


def test_insert_main_root_exception(empy_tree_initialization):
    with pytest.raises(ValueError):
        _insert_main_root(empy_tree_initialization, None, [1, 2])


@pytest.mark.parametrize(
    "key, order",
    [
        (8, ["2", "4", "3", "9", "7", "6", "5"]),
        (3, ["4", "2", "7", "9", "8", "6", "5"]),
    ],
)
def test_remove(tree_initialization_with_values, key, order):
    print(traverse(tree_initialization_with_values, "post-order"))
    remove(tree_initialization_with_values, key)
    print(tree_initialization_with_values)
    actual = traverse(tree_initialization_with_values, "post-order")
    assert actual == order


@pytest.mark.parametrize("key, value", [(8, "8"), (3, "3")])
def test_remove_value(tree_initialization_with_values, key, value):
    actual = remove(tree_initialization_with_values, key)
    assert actual == value


def test_preorder(tree_initialization_with_values):
    actual = traverse(tree_initialization_with_values, "pre-order")
    assert actual == ["5", "3", "2", "4", "6", "8", "7", "9"]


def test_inorder(tree_initialization_with_values):
    actual = traverse(tree_initialization_with_values, "in-order")
    assert actual == ["2", "3", "4", "5", "6", "7", "8", "9"]


def test_postorder(tree_initialization_with_values):
    actual = traverse(tree_initialization_with_values, "post-order")
    assert actual == ["2", "4", "3", "7", "9", "8", "6", "5"]
