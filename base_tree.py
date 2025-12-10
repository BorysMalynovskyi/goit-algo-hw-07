"""Common helpers for binary search tree variants."""

from abc import ABC, abstractmethod
from typing import Any, Generic, Iterator, Optional, TypeVar

class BaseNode:
    """Base node with shared string rendering."""

    def __init__(self) -> None:
        self.left: Optional["BaseNode"] = None
        self.right: Optional["BaseNode"] = None

    @abstractmethod
    def display_value(self) -> Any:
        """Return the value to display for this node."""
        raise NotImplementedError

    def __str__(self, level: int = 0, prefix: str = "Root: ") -> str:
        ret = "\t" * level + prefix + str(self.display_value()) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret


NodeT = TypeVar("NodeT", bound="BaseNode")


class BaseTree(Generic[NodeT], ABC):
    def __init__(self) -> None:
        self.root: Optional[NodeT] = None

    def inorder(self) -> Iterator[Any]:
        """Yield values in-order (ascending for a BST)."""
        yield from self._inorder(self.root)

    def find_max(self) -> Optional[Any]:
        """Return the largest value stored in the tree (None if empty)."""
        if self.root is None:
            return None

        node = self.root
        while node.right:
            node = node.right
        return self._value(node)

    def find_min(self) -> Optional[Any]:
        """Return the smallest value stored in the tree (None if empty)."""
        if self.root is None:
            return None

        node = self.root
        while node.left:
            node = node.left
        return self._value(node)

    def sum_values(self) -> Any:
        """Return the sum of all node values in the tree (0 if empty)."""
        return sum(self.inorder())

    @abstractmethod
    def _value(self, node: NodeT) -> Any:
        """Extract the stored value from a node (implemented by subclasses)."""
        raise NotImplementedError

    def _inorder(self, node: Optional[NodeT]) -> Iterator[Any]:
        if node:
            yield from self._inorder(node.left)
            yield self._value(node)
            yield from self._inorder(node.right)
