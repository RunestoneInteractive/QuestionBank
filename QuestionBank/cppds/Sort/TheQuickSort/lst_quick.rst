.. activecode:: lst_quick
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cppds
    :chapter: Sort
    :subchapter: TheQuickSort
    :topics: Sort/TheQuickSort
    :from_source: T
    :caption: Quick Sort
    :optional:

    #recursive function that calls itself to quicksort through a given list of values
    def quickSort(alist,first,last):
      if first<last:

        splitpoint = partition(alist,first,last)

        quickSort(alist,first,splitpoint-1)
        quickSort(alist,splitpoint+1,last)

    #function partitions vector depending on pivot value
    def partition(alist,first,last):
      pivotvalue = alist[first]

      leftmark = first+1
      rightmark = last

      done = False
      while not done:
        while alist[leftmark]<=pivotvalue and leftmark<=rightmark:
          leftmark += 1

        while alist[rightmark]>=pivotvalue and rightmark>=leftmark:
          rightmark -= 1

        if rightmark < leftmark:
          done = True

        else:
          temp = alist[rightmark]
          alist[rightmark] = alist[leftmark]
          alist[leftmark] = temp

      temp = alist[rightmark]
      alist[rightmark] = alist[first]
      alist[first] = temp

      return rightmark



    def main():

      alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
      quickSort(alist,0,len(alist)-1)
      print(alist)

    main()