.. activecode:: lst_change2
    :author: bmiller
    :difficulty: 3.0
    :basecourse: pythonds3
    :chapter: Recursion
    :subchapter: DynamicProgramming
    :topics: Recursion/DynamicProgramming
    :from_source: T
    :caption: Recursively Counting Coins with Table Lookup
    :nocodelens:

    def make_change_2(coin_value_list, change, known_results):
        min_coins = change
        if change in coin_value_list:
            known_results[change] = 1
            return 1
        elif known_results[change] > 0:
            return known_results[change]
        else:
            for i in [c for c in coin_value_list if c <= change]:
                num_coins = 1 + make_change_2(coin_value_list, change - i, known_results)
                if num_coins < min_coins:
                    min_coins = num_coins
                known_results[change] = min_coins
        return min_coins

    print(make_change_2([1, 5, 10, 25], 63, [0] * 64))