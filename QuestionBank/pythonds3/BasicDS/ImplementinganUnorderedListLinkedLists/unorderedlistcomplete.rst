.. activecode:: unorderedlistcomplete
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: ImplementinganUnorderedListLinkedLists
    :topics: BasicDS/ImplementinganUnorderedListLinkedLists
    :from_source: T
    :caption: The Complete UnorderedList Class
    :hidecode:
    :nocodelens:

    class Node:
        """A node of a linked list"""

        def __init__(self, node_data):
            self._data = node_data
            self._next = None

        def get_data(self):
            """Get node data"""
            return self._data

        def set_data(self, node_data):
            """Set node data"""
            self._data = node_data

        data = property(get_data, set_data)

        def get_next(self):
            """Get next node"""
            return self._next

        def set_next(self, node_next):
            """Set next node"""
            self._next = node_next

        next = property(get_next, set_next)

        def __str__(self):
            """String"""
            return str(self._data)


    class UnorderedList:
        def __init__(self):
            self.head = None

        def is_empty(self):
            return self.head == None

        def add(self, item):
            temp = Node(item)
            temp.set_next(self.head)
            self.head = temp

        def size(self):
            current = self.head
            count = 0
            while current is not None:
                count = count + 1
                current = current.next

            return count

        def search(self, item):
            current = self.head
            while current is not None:
                if current.data == item:
                    return True
                current = current.next

            return False

        def remove(self, item):
            current = self.head
            previous = None

            while current is not None:
                if current.data == item:
                    break
                previous = current
                current = current.next

            if current is None:
                raise ValueError("{} is not in the list".format(item))
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next


    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))

    try:
        my_list.remove(27)
    except ValueError as ve:
        print(ve)