.. activecode:: heap1
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Trees
    :subchapter: BinaryHeapOperations
    :topics: Trees/BinaryHeapOperations
    :from_source: T
    :caption: Using the Binary Heap
    :nocodelens:

    from pythonds3.trees import BinaryHeap

    my_heap = BinaryHeap()
    my_heap.insert(5)
    my_heap.insert(7)
    my_heap.insert(3)
    my_heap.insert(11)

    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())
    print(my_heap.delete())