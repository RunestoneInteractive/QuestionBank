.. activecode:: itp
    :author: jenkins
    :difficulty: 3.0
    :basecourse: msumoorhead
    :chapter: MoreAboutIteration
    :subchapter: SentinelValuesAndValidation
    :topics: MoreAboutIteration/SentinelValuesAndValidation
    :from_source: None
    :timelimit: 60000

    def checkout():
        total = 0
        count = 0
        moreItems = True
        while moreItems:
            price = float(input('Enter price of item (0 when done): '))
            if price != 0:
                count = count + 1
                total = total + price
                print('Subtotal: $', total)
            else:
                moreItems = False

        print('Total items:', count)
        print('Total $', total)
        average = total / count
        print('Average price per item: $', average)

    checkout()