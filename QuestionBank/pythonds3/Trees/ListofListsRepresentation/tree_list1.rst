.. activecode:: tree_list1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Trees
    :subchapter: ListofListsRepresentation
    :topics: Trees/ListofListsRepresentation
    :from_source: T
    :caption: Using Indexing to Access Subtrees

    my_tree = ["a", ["b", ["d", [], []], ["e", [], []]], ["c", ["f", [], []], []]]
    print(my_tree)
    print("left subtree = ", my_tree[1])
    print("root = ", my_tree[0])
    print("right subtree = ", my_tree[2])