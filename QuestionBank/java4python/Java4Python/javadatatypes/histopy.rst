.. activecode:: histopy
    :author: bmiller
    :difficulty: 3.0
    :basecourse: java4python
    :chapter: Java4Python
    :subchapter: javadatatypes
    :topics: Java4Python/javadatatypes
    :from_source: T
    :language: python

    def main():
        count = [0]*10
        data = open('test.dat')

        for line in data:
            count[int(line)] = count[int(line)] + 1

        idx = 0
        for num in count:
            print(idx, " occured ", num, " times.")
            idx += 1