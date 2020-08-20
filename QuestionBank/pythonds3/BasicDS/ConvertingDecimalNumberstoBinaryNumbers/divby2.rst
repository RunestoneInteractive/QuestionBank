.. activecode:: divby2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: BasicDS
    :subchapter: ConvertingDecimalNumberstoBinaryNumbers
    :topics: BasicDS/ConvertingDecimalNumberstoBinaryNumbers
    :from_source: T
    :caption: Converting from Decimal to Binary
    :nocodelens:

    pythonds3.basic import Stack


    def divide_by_2(decimal_num):
        rem_stack = Stack()

        while decimal_num > 0:
            rem = decimal_num % 2
            rem_stack.push(rem)
            decimal_num = decimal_num // 2

        bin_string = ""
        while not rem_stack.is_empty():
            bin_string = bin_string + str(rem_stack.pop())

        return bin_string

    print(divide_by_2(42))
    print(divide_by_2(31))