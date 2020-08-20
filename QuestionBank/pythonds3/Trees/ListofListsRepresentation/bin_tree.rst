.. activecode:: bin_tree
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Trees
    :subchapter: ListofListsRepresentation
    :topics: Trees/ListofListsRepresentation
    :from_source: T
    :caption: A Python Session to Illustrate Basic Tree Functions

    def make_binary_tree(root):
        return [root, [], []]


    def insert_left(root, new_child):
        old_child = root.pop(1)
        if len(old_child) > 1:
            root.insert(1, [new_child, old_child, []])
        else:
            root.insert(1, [new_child, [], []])
        return root


    def insert_right(root, new_child):
        old_child = root.pop(2)
        if len(old_child) > 1:
            root.insert(2, [new_child, [], old_child])
        else:
            root.insert(2, [new_child, [], []])
        return root


    def get_root_val(root):
        return root[0]


    def set_root_val(root, new_value):
        root[0] = new_value


    def get_left_child(root):
        return root[1]


    def get_right_child(root):
        return root[2]


    a_tree = make_binary_tree(3)
    insert_left(a_tree, 4)
    insert_left(a_tree, 5)
    insert_right(a_tree, 6)
    insert_right(a_tree, 7)
    left_child = get_left_child(a_tree)
    print(left_child)

    set_root_val(left_child, 9)
    print(a_tree)
    insert_left(left_child, 11)
    print(a_tree)
    print(get_right_child(get_right_child(a_tree)))