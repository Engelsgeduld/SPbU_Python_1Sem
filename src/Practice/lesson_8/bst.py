from dataclasses import dataclass
from typing import Generic, TypeVar, Optional, Callable, Iterable

V = TypeVar("V")
Key = TypeVar("Key")
Data_type = TypeVar("Data_type")


@dataclass
class Node(Generic[Key, V]):
    key: Optional[Key]
    data: Optional[V]
    right_children: Optional["Node[V]"] = None
    left_children: Optional["Node[V]"] = None


@dataclass
class Pair:
    first: Node[Key, V]
    second: Node[Key, V]


@dataclass
class Tree:
    size: int = 0
    root: Optional[Node[Key, V]] = None
    type: Optional[Data_type] = None


def _valid_input_key(map: Tree, key: Key) -> bool:
    return type(key) == map.type


def create_tree_map() -> Tree:
    return Tree()


def _extract_max(root: Node[Key, V]) -> Pair:
    if root.right_children is not None:
        pair = _extract_max(root.right_children)
        root.right_children = pair.second
        return Pair(pair.first, root)
    return Pair(root, root.left_children)


def delete_tree_map(mapp: Tree) -> None:
    def delete_recursion(cur_node: Node[V, Key]):
        if cur_node.left_children is not None:
            delete_recursion(cur_node.left_children)
        if cur_node.right_children is not None:
            delete_recursion(cur_node.right_children)

        del cur_node
        mapp.size -= 1

    delete_recursion(mapp.root)


def _find(root: Node[V, Key], key: Key) -> Node[V, Key] | None:
    if root is None:
        return None
    if key > root.key:
        return _find(root.right_children, key)
    elif key < root.key:
        return _find(root.left_children, key)
    return root


def has_key(map: Tree, key) -> bool:
    if _find(map.root, key) is not None:
        return True
    return False


def get(map: Tree, key) -> V:
    maybe_node = _find(map.root, key)
    if maybe_node is None:
        raise ValueError("Key not in BST")
    return maybe_node.data


def put(map: Tree, key: Key, value: V) -> ():
    if map.type is not None and not _valid_input_key(map, key):
        raise ValueError("Keys must be one type")
    _insert(map.root, key, value) if map.size != 0 else _insert_main_root(
        map, key, value
    )
    map.size += 1


def _insert_main_root(map: Tree, key: Key, value: V):
    map.root = Node(key, value)
    if key is not None:
        map.type = type(key)
    else:
        raise ValueError("Key can not be None")


def _insert(root: Node[V, Key], key: Key, value: V) -> Node[V, Key]:
    if root is None:
        return Node(key, value)
    if root.key > key:
        root.left_children = _insert(root.left_children, key, value)
    elif root.key < key:
        root.right_children = _insert(root.right_children, key, value)
    return root


def remove(map: Tree, key: Key) -> V:
    old_value = get(map, key)
    _delete(map.root, key)
    map.size -= 1
    return old_value


def _create_new_root(root: Node[V, Key]) -> Node[V, Key]:
    if root.left_children is None:
        new_root = root.right_children
    elif root.right_children is None:
        new_root = root.left_children
    else:
        pair = _extract_max(root.left_children)
        new_root = pair.first
        new_root.left_children = pair.second
        new_root.right_children = root.right_children
    return new_root


def _delete(root: Node, key: Key) -> Node[V, Key]:
    if root is None:
        raise ValueError("This key not exist")
    if root.key > key:
        root.left_children = _delete(root.left_children, key)
        return root
    elif root.key < key:
        root.right_children = _delete(root.right_children, key)
        return root
    root = _create_new_root(root)
    return root


def _preorder_comparator(node: Node[V, Key]) -> Iterable[Node[V, Key]]:
    return filter(None, (node, node.left_children, node.right_children))


def _inorder_comparator(node: Node[V, Key]) -> Iterable[Node[V, Key]]:
    return filter(None, (node.left_children, node, node.right_children))


def _postorder_comparator(node: Node[V, Key]) -> Iterable[Node[V, Key]]:
    return filter(None, (node.left_children, node.right_children, node))


def traverse(map: Tree, order: str) -> list[V]:
    nodes = []

    def traverse_recursion(cur_node: Node[V, Key], order_func: Callable):
        node_order = order_func(cur_node)
        for node in node_order:
            if node is not cur_node:
                traverse_recursion(node, order_func)
            else:
                nodes.append(node.data)

    match order:
        case "pre-order":
            traverse_recursion(map.root, _preorder_comparator)
        case "in-order":
            traverse_recursion(map.root, _inorder_comparator)
        case "post-order":
            traverse_recursion(map.root, _postorder_comparator)

    return nodes
