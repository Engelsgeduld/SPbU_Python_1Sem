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


def _create_tree_root(root):
    return Tree(root=root, size=1)


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
        return 0
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
    curr_node = root
    res = root
    while curr_node.right_children is not None:
        res = (
            curr_node.right_children if res.key < curr_node.right_children.key else res
        )
        curr_node = curr_node.right_children
    return res


def _extract_min(root: Node[Key, Value]) -> Node[Key, Value]:
    curr_node = root
    res = root
    while curr_node.left_children is not None:
        res = curr_node.left_children if res.key > curr_node.left_children.key else res
        curr_node = curr_node.left_children
    return res


def get_maximum(tree: Tree[Key, Value]) -> Key:
    return _extract_max(tree.root).key


def get_minimum(tree: Tree[Key, Value]) -> Key:
    return _extract_min(tree.root).key


def get_lower_bound(tree: Tree[Key, Value], key: int) -> Key | None:
    root = tree.root
    res = None
    while root is not None:
        if root.key >= key:
            res = min(root.key, res) if res is not None else root.key
            root = root.left_children
        else:
            root = root.right_children
    return res


def get_upper_bound(tree: Tree[Key, Value], key: Key) -> Key:
    root = tree.root
    res = None
    while root is not None:
        if root.key > key:
            res = root.key
            root = root.left_children
        else:
            root = root.right_children
    return res


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
        return _balance_tree(root)
    elif root.key < key:
        root.right_children = _delete(root.right_children, key)
        return _balance_tree(root)
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


# За logn работает, но кидает ошибки в тестах ко 2 задаче, которые я ещё не отловил
def merge(left_tree: Tree, right_tree: Tree) -> Optional[Tree[Key, Value]]:
    if left_tree.root is None or right_tree.root is None:
        return left_tree if right_tree.root is None else right_tree
    if left_tree.root.height <= right_tree.root.height:
        return _merge_with_low_height_or_equal(left_tree, right_tree)
    return _merge_with_bigger_height(left_tree, right_tree)


def _merge_with_low_height_or_equal(left_tree: Tree, right_tree: Tree):
    most_right_node = _extract_max(left_tree.root)
    remove(left_tree, most_right_node.key)
    if left_tree.root is None:
        put(right_tree, most_right_node.key, most_right_node.data)
        return right_tree
    if left_tree.root.height == right_tree.root.height:
        left_node = right_tree.root
    else:
        left_node = _find_left_node_with_set_height(
            right_tree.root, left_tree.root.height
        )
    most_right_node.left_children = left_tree.root
    most_right_node.right_children = left_node.left_children
    most_right_node = _balance_tree(most_right_node)
    left_node.left_children = most_right_node
    right_tree.root = _balance_tree(right_tree.root)
    return right_tree


def _merge_with_bigger_height(left_tree: Tree, right_tree: Tree):
    most_left_node = _extract_min(right_tree.root)
    remove(right_tree, most_left_node.key)
    if right_tree.root is None:
        put(left_tree, most_left_node.key, most_left_node.data)
        return left_tree
    right_node = _find_right_node_with_set_height(
        left_tree.root, right_tree.root.height
    )
    most_left_node.left_children = right_node.right_children
    most_left_node.right_children = right_tree.root
    most_left_node = _balance_tree(most_left_node)
    right_node.right_children = most_left_node
    left_tree.root = _balance_tree(left_tree.root)
    return left_tree


def _find_left_node_with_set_height(root: Node[Key, Value], height: int):
    curr_node_left = root
    while curr_node_left.height != height + 1:
        curr_node_left = root.left_children
    return curr_node_left


def _find_right_node_with_set_height(root: Node[Key, Value], height: int):
    curr_node_right = root
    while curr_node_right.height != height + 1:
        curr_node_right = root.right_children
    return curr_node_right


# Заботает за logn, но без работающего merge юзлесс :(
def split(
    tree: Tree[Key, Value], key: int
) -> tuple[Tree[Key, Value], Tree[Key, Value]]:
    if tree.root is None:
        return Tree(), Tree()

    left_tree, right_tree = _split_recursion(tree, key)
    return left_tree, right_tree


def _split_recursion(curr_tree: Tree, key):
    if curr_tree.root.key == key:
        left_part = _create_tree_root(curr_tree.root.left_children)
        right_part = _create_tree_root(curr_tree.root.right_children)
        put(right_part, curr_tree.root.key, curr_tree.root.data)
        return left_part, right_part
    elif curr_tree.root.key > key:
        if curr_tree.root.left_children is None:
            return Tree(), curr_tree
        left_part = _create_tree_root(curr_tree.root.left_children)
        left_tree, right_tree = _split_recursion(left_part, key)
        put(right_tree, curr_tree.root.key, curr_tree.root.data)
        right_part = _create_tree_root(curr_tree.root.right_children)
        return left_tree, merge(right_tree, right_part)
    else:
        if curr_tree.root.right_children is None:
            return curr_tree, Tree()
        right_part = _create_tree_root(curr_tree.root.right_children)
        left_tree, right_tree = _split_recursion(right_part, key)
        put(left_tree, curr_tree.root.key, curr_tree.root.data)
        left_part = _create_tree_root(curr_tree.root.left_children)
        return merge(left_part, left_tree), right_tree


def get_all(tree: Tree[Key, Value], left: Key, right: Key) -> list[Key]:
    if tree.type == str:
        right += "$"
    splited_tree = split(split(tree, left)[1], right)[0]
    if splited_tree.root is None:
        return []
    return list(map(lambda pair: pair[0], traverse(splited_tree, 1)))


def remove_keys(tree: Tree[Key, Value], left: Key, right: Key):
    tree.root = merge(split(tree, left)[0], split(tree, right)[1]).root
