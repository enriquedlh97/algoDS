"""
Problem:

Given an array of positive integers representing the values of coins in your
possession, wire a function that returns the minimum amount of change (the
minimum sum of money) that you cannot create. The given coins can have any
positive integer value and aren't necessarily unique (i.e., you can have
multiple coins of the same value).

For example, if you're given [1, 2, 5], the minimum amount of change that you
cannot create is 4. If you are given no coins, the minimum amount of change that
you cannot create is 1.

Input:
    coins: [5, 7, 1, 1, 2, 3, 22]

Output:
    20
"""

""" Keeps track of team with most points and replaces it when necessary.

        Keeps track of team with the most points and keeps track of the score
        of every team in a hash table. Teams are only added to the hash table
        once they win a match, otherwise it is assumed they have a score of 0.
        The value sof the hash table for the points of a player are updated every
         time it wins a match.

        Attributes:
            competitions: Non-empty multidimensional array where first dimension
                corresponds to the match number and the second one contains the
                teams that competed in that match.

            results: Non-empty array of the same size as the first dimension of the
                competitions array, corresponding to the match number. The value
                    at a particular index indicates which team won.
    """


# Time O(n), where n is the number of coins
# Space O(1) because we assume we can sort the array in place. Important to verify this in interview, else
# it becomes Space O(n)
def non_constructable_change_optimal(coins):
    """ Keeps track of max constructable change and checks that the next coin is not at most 1 unit bigger.

        It first sorts the array and then traverses it validating each coin.

        With a particular ordered array [1, 2, 3] representing the coins at hand, the max constructable change I can
        make is 1 + 2 + 3 = 6

        current coins: [1, 2, 3]

        1 = 1           6 = 3 + 2 + 1
        2 = 2
        3 = 3
        4 = 3 + 1
        5 = 3 + 2

        If I then get 4 as next coin, then I can now construct change up to 1 + 2 + 3 + 4 = 10

        This change can be constructed as follows. (here left number is change and right number coins)

        current coins: [1, 2, 3, 4]

        1 = 1           6 = 3 + 2 + 1
        2 = 2           7 = 4 + 3
        3 = 3           8 = 4 + 3 + 1
        4 = 3 + 1       9 = 4 + 3 + 2
        5 = 3 + 2       10 = 4 + 3 + 2 + 1

        I we wanted to create the change 11 we have to make sure that the next coin we get is not bigger than 11
        Because if we get 12, then we would not be able to create it. Since the array is sorted, then the minimum
        coin we can get next is the same as the one we currently have, i.e. 4.

        With another 4 we would be able to create up to 1 + 2 + 3 + 4 + 4 = 14

        current coins: [1, 2, 3, 4, 4]

        1 = 1           6 = 3 + 2 + 1           11 = 4 + 4 + 3
        2 = 2           7 = 4 + 3               12 = 4 + 4 + 3 + 1
        3 = 3           8 = 4 + 3 + 1           13 = 4 + 4 + 3 + 2
        4 = 3 + 1       9 = 4 + 3 + 2           14 = 4 + 4 + 3 + 2 + 1
        5 = 3 + 2       10 = 4 + 3 + 2 + 1

        Getting another 4 (no lower value because the coin array is sorted), allows us to increase our current maximum
        constructable change by 1 unit, that is why we can create 11. The same is the case for any new coin we get
        which is at most 1 unit bigger than the maximum change we can currently create (10), that means we can get any
        coin from 4 up to 11.

        current coins: [1, 2, 3, 4, 11]

        1 = 1           6 = 3 + 2 + 1           11 = 11          16 = 11 + 4 + 1         21 = 11 + 4 + 3 + 2 + 1
        2 = 2           7 = 4 + 3               12 = 11 + 1      17 = 11 + 4 + 2
        3 = 3           8 = 4 + 3 + 1           13 = 11 + 2      18 = 11 + 4 + 3
        4 = 3 + 1       9 = 4 + 3 + 2           14 = 11 + 3      19 = 11 + 4 + 3 + 1
        5 = 3 + 2       10 = 4 + 3 + 2 + 1      15 = 11 + 4      20 = 11 + 4 + 3 + 2

        Getting a coin ranging from 4 up to the 11 allows us to have that 1 unit increment needed for going from 10
        to 11 in maximum constructable change. If we instead got a 12 (maximum constructable change + 2) we would not be
        able to generate that 1 unit increment from 10 to 11.

        That is why we have to traverse our coins, and if they are not bigger than our
        "current maximum constructable change + 1", then we add the value of our coin and the max constructable change
        becomes "max constructable change += coin" because of what was explained in the first example with
        [1, 2, 3] and [4]. Else, if it is bigger than "current maximum constructable change + 1", then
        "current maximum constructable change + 1" is the minimum amount of change that we cannot generate.


        Attributes:
            coins: Array of integer values representing the value of a particular coin at hand. It can be empty.
    """
    coins.sort()

    max_change_available = 0

    for coin in coins:
        if coin > max_change_available + 1:
            return max_change_available + 1

        max_change_available += coin

    return max_change_available + 1


# Time O( n^(2) ), where n is the number of coins
# Space O(k), where k is the number of teams (because of hash table)
def non_constructable_change(coins):
    """ Verifies it can construct every change with coins. Iterates over change

        This is the brute force approach, similar to what one would intuitibely do if one were on that case.
        I would ask if I can generate a change of 1 with the current coins, then I would ask if I can generate a change
        of 2 (by seeing if I have either [1, 1] or [2]) and I would continue with all changes until I find a change
        I cannot generate.

        It is clearly more complex and a lot less efficient than the optimal solution.

        This function iterates over the changes (1, 2, 3,...) and for every change it calls the
        verify_change() function. This function starts subtracting the coins from last one seen (coin N) and goes down
        until it subtracts the first coin seen (which would have to be 1).  It does this because, since it
        sorts the array with coins, by subtracting one by one of them from the current change to be verified in a
        backwards fashion, it could be seen as verifying if the current coin is greater tan the maximum "constructable
        change + 1", this is because at the end, if the result is greater than 0, it means the change was in deed
        bigger than "constructable change + 1"

        Attributes:
        coins: Array of integer values representing the value of a particular coin at hand. It can be empty.
    """

    if coins:
        # Sort in ascending order
        coins.sort()
        changes = []
        change_found = False
        change = 1
        while not change_found:

            if change <= len(coins):
                current_coin = change - 1

            if change == coins[current_coin] and change <= len(coins):
                changes.append(coins[current_coin])
            elif not verify_change(coins[current_coin], change, changes, coins):
                return change

            change += 1

    return 1


def verify_change(current_coin, change, change_list, coins):
    """ Helper function for non_constructable_change(), verifies if change is constructable

    Attributes:
        current_coin: Integer representing the value of the last coin received.
        change: Integer value representing the current change being verified
        change_list:
        coins:
    """
    if change <= len(coins):
        change_list.append(current_coin)

    for change_idx in range(len(change_list), 0, -1):

        if change - change_list[change_idx - 1] == 0:
            return True
        elif change - change_list[change_idx - 1] > 0:
            change -= change_list[change_idx - 1]

    return False
