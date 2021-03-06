.. activecode:: completeheappy
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Trees
    :subchapter: BinaryHeapImplementation
    :topics: Trees/BinaryHeapImplementation
    :from_source: T
    :caption: The Complete Binary Heap Example Python
    :language: python
    :optional:

    # uses a vector to creat a Binar Heap
    class BinHeap:
        """initializes the vector and an attribute currentSize
        as 0 to allow for interger division."""
        def __init__(self):
            self.heapList = [0]
            self.currentSize = 0


        """ prelocates and item as far up in the
        tree as possible to maintain
        the Heap property """
        def percUp(self,i):
            while i // 2 > 0:
                if self.heapList[i] < self.heapList[i // 2]:
                    tmp = self.heapList[i // 2]
                    self.heapList[i // 2] = self.heapList[i]
                    self.heapList[i] = tmp
                i = i // 2

        # appends item to the end of the vector
        def insert(self,k):
            self.heapList.append(k)
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)

        """ prelocates and item as far down in the
        tree as possible to maintain
        the Heap property """
        def percDown(self,i):
            while (i * 2) <= self.currentSize:
                mc = self.minChild(i)
                if self.heapList[i] > self.heapList[mc]:
                    tmp = self.heapList[i]
                    self.heapList[i] = self.heapList[mc]
                    self.heapList[mc] = tmp
                i = mc

        def minChild(self,i):
            if i * 2 + 1 > self.currentSize:
                return i * 2
            else:
                if self.heapList[i*2] < self.heapList[i*2+1]:
                    return i * 2
                else:
                    return i * 2 + 1

        """ restores full complince with the heap structure
        and heap order properties after the root is removed
        by  taking the last item and moving it to the root position
        and pushing the new root node down the tree to its proper postion."""
        def delMin(self):
            retval = self.heapList[1]
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.percDown(1)
            return retval

        def buildHeap(self,alist):
            i = len(alist) // 2
            self.currentSize = len(alist)
            self.heapList = [0] + alist[:]
            while (i > 0):
                self.percDown(i)
                i = i - 1

    def main():

        bh = BinHeap()
        bh.buildHeap([9,5,6,2,3])

        print(bh.delMin())
        print(bh.delMin())
        print(bh.delMin())
        print(bh.delMin())
        print(bh.delMin())

    main()