.. activecode:: fnm
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: Functions
    :subchapter: mainfunction
    :topics: Functions/mainfunction
    :from_source: None
    :nocodelens:

    def squareit(n):

        return n * n

    def cubeit(n):

        return n*n*n

    def main():
        anum = int(input("Please enter a number"))
        print(squareit(anum))
        print(cubeit(anum))

    if __name__ == "__main__":
        main()
        import test
        print('testing squareit')
        test.testEqual(squareit(5), 25)
        print('testing cubeit')