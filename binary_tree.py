from typing import Any, Optional

from base_tree import BaseNode, BaseTree


class Node(BaseNode):
    def __init__(self, key: Any):
        super().__init__()
        self.val = key

    def display_value(self) -> Any:
        return self.val


class BinaryTree(BaseTree[Node]):
    def __init__(self):
        super().__init__()

    def insert(self, key: Any) -> Node:
        self.root = self._insert(self.root, key)
        return self.root

    def search(self, key: Any) -> Optional[Node]:
        return self._search(self.root, key)

    def delete(self, key: Any) -> Optional[Node]:
        self.root = self._delete(self.root, key)
        return self.root

    def _insert(self, root: Optional[Node], key: Any) -> Node:
        if root is None:
            return Node(key)
        if key < root.val:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def _search(self, root: Optional[Node], key: Any) -> Optional[Node]:
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def _delete(self, root: Optional[Node], key: Any) -> Optional[Node]:
        if not root:
            return root

        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp
            root.val = self._min_value_node(root.right).val
            root.right = self._delete(root.right, root.val)
        return root

    def _value(self, node: Node) -> Any:
        return node.val

    def __str__(self) -> str:
        if not self.root:
            return "<empty tree>"
        return self.root.__str__()
