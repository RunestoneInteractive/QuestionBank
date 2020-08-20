.. activecode:: completeheap
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Trees
    :subchapter: BinaryHeapImplementation
    :topics: Trees/BinaryHeapImplementation
    :from_source: T
    :caption: The Complete Binary Heap Example
    :hidecode:

    class BinaryHeap:
        def __init__(self):
            self._heap = []

        def _perc_up(self, cur_idx):
            while (cur_idx - 1) // 2 >= 0:
                parent_idx = (cur_idx - 1) // 2
                if self._heap[cur_idx] < self._heap[parent_idx]:
                    self._heap[cur_idx], self._heap[parent_idx] = (
                        self._heap[parent_idx],
                        self._heap[cur_idx],
                    )
                cur_idx = parent_idx

        def _perc_down(self, cur_idx):
            while 2 * cur_idx + 1 < len(self._heap):
                min_child_idx = self._get_min_child(cur_idx)
                if self._heap[cur_idx] > self._heap[min_child_idx]:
                    self._heap[cur_idx], self._heap[min_child_idx] = (
                        self._heap[min_child_idx],
                        self._heap[cur_idx],
                    )
                else:
                    return
                cur_idx = min_child_idx

        def _get_min_child(self, parent_idx):
            if 2 * parent_idx + 2 > len(self._heap) - 1:
                return 2 * parent_idx + 1
            if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            return 2 * parent_idx + 2

        def heapify(self, not_a_heap):
            self._heap = not_a_heap[:]
            cur_idx = len(self._heap) // 2 - 1
            while cur_idx >= 0:
                self._perc_down(cur_idx)
                cur_idx = cur_idx - 1

        def get_min(self):
            return self._heap[0]

        def insert(self, item):
            self._heap.append(item)
            self._perc_up(len(self._heap) - 1)

        def delete(self):
            self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
            result = self._heap.pop()
            self._perc_down(0)
            return result

        def is_empty(self):
            return not bool(self._heap)

        def __len__(self):
            return len(self._heap)

        def __str__(self):
            return str(self._heap)

    a_heap = BinaryHeap()
    a_heap.heapify([9, 5, 6, 2, 3])

    while not a_heap.is_empty():
        print(a_heap.delete())