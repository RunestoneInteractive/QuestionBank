.. activecode:: palchecker
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: PalindromeChecker
    :topics: BasicDS/PalindromeChecker
    :from_source: T
    :caption: A Palindrome Checker Using Deque
    :nocodelens:

    from pythonds3.basic import Deque


    def pal_checker(a_string):
        char_deque = Deque()

        for ch in a_string:
            char_deque.add_rear(ch)

        while char_deque.size() > 1:
            first = char_deque.remove_front()
            last = char_deque.remove_rear()
            if first != last:
                return False

        return True

    print(pal_checker("lsdkjfskf"))
    print(pal_checker("radar"))