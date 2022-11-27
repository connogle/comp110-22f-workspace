from __future__ import annotations
from typing import Optional

class Node:
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"


def sum(node: Optional[Node]) -> int:
    if node is None:
        return 0
    else:
        return node.data + sum(node.next)

def count(node: Optional[Node], current: int = 0) -> int:
    if node is None:
        return current
    else:
        return count(node.next, current + 1)


head: Node = Node(3, None)
head: Node = Node(2, head)
head = Node(1, head)

print(sum(head))
print(count(head))
print(head)