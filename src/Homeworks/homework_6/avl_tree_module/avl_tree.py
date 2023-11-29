from dataclasses import dataclass
from typing import Generic, TypeVar, Optional, Callable, Iterable, Any

Value = TypeVar("Value")
Key = TypeVar("Key")


@dataclass
class Node(Generic[Key, Value]):
    key: Key
    data: Value
    height: int = 1
    right_children: Optional["Node[Key ,Value]"] = None
    left_children: Optional["Node[Key ,Value]"] = None


@dataclass
class Tree(Generic[Key, Value]):
    root: Optional[Node[Key, Value]] = None
    size: int = 0
    type: type = None


def _valid_input_key(map: Tree, key: Key) -> bool:
    return key is not None if map.type is None else type(key) == map.type


def create_tree_map() -> Tree:
    return Tree()


def _get_height(root: Node[Key, Value]) -> int:
    return root.height if root is not None else 0


def get(map: Tree, key) -> Value:
    maybe_node = _find(map.root, key)
    if maybe_node is None:
        raise ValueError("Key not in BST")
    return maybe_node.data


def _get_balance_factor(root: Node[Key, Value]) -> int:
    return _get_height(root.right_children) - _get_height(root.left_children)


def _update_height(root: Node[Key, Value]):
    if root is None:
        raise Exception("Root is None")
    root.height = (
        max(_get_height(root.right_children), _get_height(root.left_children)) + 1
    )


def _rotate_right(root: Node[Key, Value]) -> Node[Key, Value]:
    child = root.left_children
    root.left_children = child.right_children
    child.right_children = root
    _update_height(root)
    _update_height(child)
    return child


def _rotate_left(root: Node[Key, Value]) -> Node[Key, Value]:
    child = root.right_children
    root.right_children = child.left_children
    child.left_children = root
    _update_height(root)
    _update_height(child)
    return child


def _balance_tree(node: Node[Key, Value]) -> Node[Key, Value]:
    _update_height(node)
    balance_factor = _get_balance_factor(node)
    if balance_factor == 2:
        if _get_balance_factor(node.right_children) < 0:
            node.right_children = _rotate_right(node.right_children)
        return _rotate_left(node)
    if balance_factor == -2:
        if _get_balance_factor(node.left_children) > 0:
            node.left_children = _rotate_left(node.left_children)
        return _rotate_right(node)
    return node


def _insert_main_root(map: Tree, key: Key, value: Value):
    if key is None:
        raise ValueError("Key can not be None")
    map.type = type(key)
    map.root = Node(key, value)
    map.size += 1


def _insert(root: Node[Key, Value], key: Key, value: Value) -> Node[Value, Key]:
    if root is None:
        return Node(key, value)
    if root.key > key:
        root.left_children = _insert(root.left_children, key, value)
    elif root.key < key:
        root.right_children = _insert(root.right_children, key, value)
    else:
        root.data = value
    return _balance_tree(root)


def _extract_max(root: Node[Key, Value]) -> Node[Key, Value]:
    if root.right_children is not None:
        maximum = _extract_max(root.right_children)
        return maximum
    return root


def _extract_min(root: Node[Key, Value]) -> Node[Key, Value]:
    if root.left_children is not None:
        minimum = _extract_min(root.left_children)
        return minimum
    return root


def get_maximum(tree: Tree[Key, Value]) -> Key:
    return _extract_max(tree.root).key


def get_minimum(tree: Tree[Key, Value]) -> Key:
    return _extract_min(tree.root).key


def get_lower_bound(tree: Tree[Key, Value], key: int) -> Key | None:
    height_root = split(tree, key)[1]
    return get_minimum(height_root) if height_root.root is not None else None


def get_upper_bound(tree: Tree[Key, Value], key: Key) -> Key:
    height_root = split(tree, key + 1)[1]
    return get_minimum(height_root) if height_root.root is not None else None


def _find(root: Node[Value, Key], key: Key) -> Node[Value, Key] | None:
    if root is None:
        return None
    if root.key == key:
        return root
    if key > root.key:
        return _find(root.right_children, key)
    else:
        return _find(root.left_children, key)


def _delete(root: Node, key: Key) -> Node[Value, Key]:
    if root is None:
        raise ValueError("This key not exist")
    if key < root.key:
        root.left_children = _delete(root.left_children, key)
        return root
    elif root.key < key:
        root.right_children = _delete(root.right_children, key)
        return root
    else:
        q = root.left_children
        r = root.right_children
        root = None
        if r is None:
            return q
        minimum = _extract_min(r)
        minimum.right_children = _remove_min(r)
        minimum.left_children = q
        return _balance_tree(minimum)


def delete_tree_map(map: Tree) -> None:
    def delete_recursion(cur_node: Node[Value, Key]):
        if cur_node.left_children is not None:
            delete_recursion(cur_node.left_children)
        if cur_node.right_children is not None:
            delete_recursion(cur_node.right_children)

        del cur_node
        map.size -= 1

    delete_recursion(map.root)


def has_key(map: Tree, key) -> bool:
    return _find(map.root, key) is not None


def _remove_min(node: Node[Key, Value]):
    if node.left_children is None:
        return node.right_children
    node.left_children = _remove_min(node.left_children)
    return _balance_tree(node)


def remove(map: Tree, key: Key) -> Value:
    if map.root is None:
        raise ValueError("Tree is empty")
    old_value = get(map, key)
    new_root = _delete(map.root, key)
    map.root = new_root
    map.size -= 1
    return old_value


def put(map: Tree, key: Key, value: Value) -> ():
    if map.type is not None and not _valid_input_key(map, key):
        raise ValueError("Keys must be one type")
    if map.root is not None:
        if not has_key(map, key):
            map.size += 1
        new_root = _insert(map.root, key, value)
        if map.root.key != new_root.key:
            map.root = new_root
    else:
        _insert_main_root(map, key, value)


def _preorder_comparator(node: Node[Value, Key]) -> Iterable[Node[Value, Key]]:
    return filter(None, (node, node.left_children, node.right_children))


def _inorder_comparator(node: Node[Value, Key]) -> Iterable[Node[Value, Key]]:
    return filter(None, (node.left_children, node, node.right_children))


def traverse(map: Tree, order: int) -> list[Value] | None:
    if map.root is None:
        return None

    nodes = []

    def traverse_recursion(cur_node: Node[Value, Key], order_func: Callable):
        node_order = order_func(cur_node)
        for node in node_order:
            if node is not cur_node:
                traverse_recursion(node, order_func)
            else:
                nodes.append((node.key, node.data))

    match order:
        case 0:
            traverse_recursion(map.root, _preorder_comparator)
        case 1:
            traverse_recursion(map.root, _inorder_comparator)
    return nodes


def merge(left_tree: Tree, right_tree: Tree) -> Tree[Key, Value]:
    def merge_recursion(left_root: Node[Key, Value], right_root: Node[Key, Value]):
        if left_root is None:
            return right_root
        right_root = merge_recursion(left_root.left_children, right_root)
        right_root = _insert(right_root, left_root.key, left_root.data)
        right_root = merge_recursion(left_root.right_children, right_root)
        return right_root

    right_tree.root = merge_recursion(left_tree.root, right_tree.root)
    return right_tree


def _split_keys(
    keys: list[tuple[Key, Value]], key: int
) -> tuple[list[tuple[Any, Any]], list[tuple[Any, Any]]]:
    lower_keys, height_keys = [], []
    for pair in keys:
        lower_keys.append(pair) if pair[0] < key else height_keys.append(pair)
    return lower_keys, height_keys


def split(
    tree: Tree[Key, Value], key: int
) -> tuple[Tree[Key, Value], Tree[Key, Value]]:
    if tree.root is None:
        return Tree(), Tree()
    keys = traverse(tree, 0)
    lower_keys, height_keys = _split_keys(keys, key)
    lower_tree = Tree()
    height_tree = Tree()
    for pair in lower_keys:
        put(lower_tree, *pair)
    for pair in height_keys:
        put(height_tree, *pair)
    return lower_tree, height_tree


def get_all(tree: Tree[Key, Value], left: Key, right: Key) -> list[Key]:
    if tree.type == str:
        right += "$"
    splited_tree = split(split(tree, left)[1], right)[0]
    if splited_tree.root is None:
        return []
    return list(map(lambda pair: pair[0], traverse(splited_tree, 1)))


def remove_keys(tree: Tree[Key, Value], left: Key, right: Key):
    tree.root = merge(split(tree, left)[0], split(tree, right)[1]).root
