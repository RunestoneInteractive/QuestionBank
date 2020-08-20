.. activecode:: tree_list1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Trees
    :subchapter: ListofListsRepresentation
    :topics: Trees/ListofListsRepresentation
    :from_source: T
    :caption: Using Indexing to Access Subtrees
    :optional:

    myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
    print(myTree)
    print('left subtree = ', myTree[1])
    print('root = ', myTree[0])
    print('right subtree = ', myTree[2])