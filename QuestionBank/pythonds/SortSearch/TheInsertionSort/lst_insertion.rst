.. activecode:: lst_insertion
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds
    :chapter: SortSearch
    :subchapter: TheInsertionSort
    :topics: SortSearch/TheInsertionSort
    :from_source: T
    :caption: Insertion Sort

    def insertionSort(alist):
       for index in range(1,len(alist)):

         currentvalue = alist[index]
         position = index

         while position>0 and alist[position-1]>currentvalue:
             alist[position]=alist[position-1]
             position = position-1

         alist[position]=currentvalue

    alist = [54,26,93,17,77,31,44,55,20]
    insertionSort(alist)
    print(alist)