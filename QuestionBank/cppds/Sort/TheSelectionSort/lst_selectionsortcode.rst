.. activecode:: lst_selectionsortcode
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Sort
    :subchapter: TheSelectionSort
    :topics: Sort/TheSelectionSort
    :from_source: T
    :caption: Selection Sort
    :optional:

    #function sorts through values in list using selection sort
    def selectionSort(alist):
       for fillslot in range(len(alist)-1,0,-1):
           positionOfMax=0
           for location in range(1,fillslot+1):
               if alist[location]>alist[positionOfMax]:
                   positionOfMax = location

           temp = alist[fillslot]
           alist[fillslot] = alist[positionOfMax]
           alist[positionOfMax] = temp

    def main():
        alist = [54,26,93,17,77,31,44,55,20]
        selectionSort(alist)
        print(alist)
    main()