"""Simple hierarchical comment system."""


class Comment:
    deleted_placeholder = "This comment was deleted."

    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies: list["Comment"] = []
        self.is_deleted = False

    def add_reply(self, comment: "Comment") -> None:
        """Attach a reply to this comment."""
        self.replies.append(comment)

    def remove_reply(self) -> None:
        """Mark this comment as deleted, leaving its replies intact."""
        self.text = self.deleted_placeholder
        self.is_deleted = True

    def display(self, indent: int = 0) -> None:
        """Recursively print this comment and its replies with indentation."""
        prefix = " " * indent
        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 4)


if __name__ == "__main__":
    root = Comment("What a great book!", "Bohdan")
    reply1 = Comment("Total disappointment.", "Andriy")
    reply2 = Comment("What is great about it?", "Maryna")

    root.add_reply(reply1)
    root.add_reply(reply2)

    reply1_1 = Comment("Not worth the paper it's printed on.", "Serhiy")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root.display()
