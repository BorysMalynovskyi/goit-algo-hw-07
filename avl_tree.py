from typing import Any, Iterator, Optional

from base_tree import BaseNode, BaseTree


class AVLNode(BaseNode):
    def __init__(self, key: Any):
        super().__init__()
        self.key = key
        self.height = 1

    def display_value(self) -> Any:
        return self.key


class AVLTree(BaseTree[AVLNode]):
    def __init__(self):
        super().__init__()

    def insert(self, key: Any) -> AVLNode:
        self.root = self._insert(self.root, key)
        return self.root

    def delete(self, key: Any) -> Optional[AVLNode]:
        self.root = self._delete(self.root, key)
        return self.root

    def search(self, key: Any) -> Optional[AVLNode]:
        return self._search(self.root, key)

    def _height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def _balance(self, node: Optional[AVLNode]) -> int:
        return self._height(node.left) - self._height(node.right) if node else 0

    def _left_rotate(self, node: AVLNode) -> AVLNode:
        right_child = node.right
        moved_subtree = right_child.left

        right_child.left = node
        node.right = moved_subtree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_child.height = 1 + max(self._height(right_child.left), self._height(right_child.right))
        return right_child

    def _right_rotate(self, node: AVLNode) -> AVLNode:
        left_child = node.left
        moved_subtree = left_child.right

        left_child.right = node
        node.left = moved_subtree

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_child.height = 1 + max(self._height(left_child.left), self._height(left_child.right))
        return left_child

    def _min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _insert(self, root: Optional[AVLNode], key: Any) -> AVLNode:
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._balance(root)

        if balance > 1:
            if key < root.left.key:
                return self._right_rotate(root)
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return self._left_rotate(root)
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _delete(self, root: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self._height(root.left), self._height(root.right))
        balance = self._balance(root)

        if balance > 1:
            if self._balance(root.left) >= 0:
                return self._right_rotate(root)
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        if balance < -1:
            if self._balance(root.right) <= 0:
                return self._left_rotate(root)
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _search(self, root: Optional[AVLNode], key: Any) -> Optional[AVLNode]:
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def _inorder(self, root: Optional[AVLNode]) -> Iterator[Any]:
        if root:
            yield from self._inorder(root.left)
            yield root.key
            yield from self._inorder(root.right)

    def _value(self, node: AVLNode) -> Any:
        return node.key

    def __str__(self) -> str:
        if not self.root:
            return "<empty AVL tree>"
        return self.root.__str__()
