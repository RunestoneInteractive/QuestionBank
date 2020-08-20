.. activecode:: stack_1ac
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: ImplementingaStackinPython
    :topics: BasicDS/ImplementingaStackinPython
    :from_source: T
    :caption: Implementing a Stack class using Python lists
    :nocodelens:

    class Stack:
        """Stack implementation as a list"""

        def __init__(self):
            """Create new stack"""
            self._items = []

        def is_empty(self):
            """Check if the stack is empty"""
            return not bool(self._items)

        def push(self, item):
            """Add an item to the stack"""
            self._items.append(item)

        def pop(self):
            """Remove an item from the stack"""
            return self._items.pop()

        def peek(self):
            """Get the value of the top item in the stack"""
            return self._items[-1]

        def size(self):
            """Get the number of items in the stack"""
            return len(self._items)