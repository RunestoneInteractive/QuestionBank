.. activecode:: address_py
    :author: bmiller
    :difficulty: 3.0
    :basecourse: cpp4python
    :chapter: AtomicData
    :subchapter: AtomicData
    :topics: AtomicData/AtomicData
    :from_source: T
    :caption: Memory identifier in Python

    # Outputs the value & memory address of
    # variable titled varN.
    def main():
        varN = 101;
        print(varN)
        print(id(varN)) # ID function returns the memory address in Python.

    main()