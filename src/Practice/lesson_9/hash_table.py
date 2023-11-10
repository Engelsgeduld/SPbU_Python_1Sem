from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

Key = TypeVar("Key")
Value = TypeVar("Value")
POWER_OF_CAPACITY = 2
INITIAL_CAPACITY = 2**POWER_OF_CAPACITY


@dataclass
class Node(Generic[Key, Value]):
    key: Key
    value: Value


@dataclass
class HashTable(Generic[Key, Value]):
    capacity: int = INITIAL_CAPACITY
    size: int = 0
    buckets: Optional[list[Node[Key, Value]]] = None
    transfer_buckets: Optional[list[Node[Key, Value]]] = None
    allocated_buckets: Optional[list[int]] = None


def resize(table: HashTable):
    def check_load_factor() -> bool:
        return table.size / table.capacity > 0.7

    def move_element(node: Node[Key, Value]):
        table.allocated_buckets.append(
            _insert(table.transfer_buckets, table.capacity * 2, node.key, node.value)
        )
        table.size += 1
        remove(table, node.key)

    if check_load_factor():
        table.transfer_buckets = [None] * (table.capacity * 2)
        for i in filter(None, table.buckets):
            move_element(i)
        table.capacity *= 2
        table.buckets = table.transfer_buckets
        table.transfer_buckets = None


def create_hash_table() -> HashTable[Key, Value]:
    new_hash_table = HashTable()
    new_hash_table.buckets = [None] * INITIAL_CAPACITY
    new_hash_table.allocated_buckets = []
    return new_hash_table


def _hash(key: Key, capacity: int) -> int:
    return hash(key) % capacity


def put(table: HashTable[Key, Value], key: Key, value: Value):
    resize(table)
    table.allocated_buckets.append(_insert(table.buckets, table.capacity, key, value))
    table.size += 1


def _insert(
    buckets: list[Node[Key, Value]], capacity: int, key: Key, value: Value
) -> int:
    index = hash(key)
    if buckets[index % capacity] is None:
        buckets[index % capacity] = Node(key, value)
        return index % capacity
    else:
        for i in range(capacity + 1):
            triangle = int(0.5 * i * (i + 1))
            index = (index + triangle) % capacity
            if buckets[index] is None:
                buckets[index] = Node(key, value)
                return index


def _find(table: HashTable[Key, Value], key: Key) -> int:
    buckets = table.buckets
    capacity = table.capacity
    hash_of_key = hash(key)
    for i in range(capacity * 3):
        triangle = int(0.5 * i * (i + 1))
        index = (hash_of_key + triangle) % capacity
        if buckets[index] is None:
            continue
        bucket_key = buckets[index].key
        if bucket_key == key:
            return index
    return -1


def has_key(table: HashTable[Key, Value], key: Key) -> bool:
    return _find(table, key) != -1


def get(table: HashTable[Key, Value], key: Key) -> Value:
    index = _find(table, key)
    if index == -1:
        raise ValueError("This key not exist")
    return table.buckets[index].value


def remove(table: HashTable[Key, Value], key: Key) -> Value:
    index = _find(table, key)
    if table.size == 0:
        raise ValueError("Table is empty")
    if index == -1:
        raise ValueError("This key not exist")
    old_value = table.buckets[index].value
    table.buckets[index] = None
    table.size -= 1
    return old_value


def get_items(table: HashTable[Key, Value]) -> list[tuple[Key, Value]]:
    verify_allocated_buckets = filter(
        lambda x: table.buckets[x], table.allocated_buckets
    )
    items = list(
        map(
            lambda x: (table.buckets[x].key, table.buckets[x].value),
            verify_allocated_buckets,
        )
    )
    return items


def delete_hash_table(table: HashTable[Key, Value]):
    for node in table.buckets:
        del node
    del table
