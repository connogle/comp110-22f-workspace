from ex11.linked_list import Node, value_at, max, linkify

linked_list: Node = Node(3, Node(5, Node(7, Node(2, None))))

print(value_at(linked_list, 0))

print(max(linked_list))

print(linkify([1, 2, 3, 4]))

print(Node(1, Node(2, Node(3, Node(4, None)))))