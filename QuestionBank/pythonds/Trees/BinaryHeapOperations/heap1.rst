.. activecode:: heap1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: Trees
    :subchapter: BinaryHeapOperations
    :topics: Trees/BinaryHeapOperations
    :from_source: T
    :caption: Using the Binary Heap
    :nocodelens:

    from pythonds.trees import BinHeap

    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)

    print(bh.delMin())

    print(bh.delMin())

    print(bh.delMin())

    print(bh.delMin())