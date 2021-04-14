"""
Problem:

The fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth
number is the sum of the (n -1)th and (n - 2)th numbers. Write a function that takes in an integer n and returns the nth
fibonacci number.

Input:
    1. n: 2

    2. n: 6

Output:
    1. 1  because 0, 1

    2. 5 because 0, 1, 1, 2, 3, 5
"""


# Time O(2^n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(n)
def get_nth_fib_recursive(n):
    """ Traditional recursive solution



    :param n: integer representing the nth fibonacci number to be calculated
    :return: integer representing the nth fibonacci number
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_nth_fib_recursive(n - 1) + get_nth_fib_recursive(n - 2)


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(1) if we assume that the compiler does tail call elimination, if not, then we have O(n) space
def get_nth_fib_tail_recursive(n, two_previous=1, amount=0):
    """ Tail recursive solution

    This solution, as it calls its recursive part, in only takes O(n) time because it only calls itself once, it does
    not split into two recursive calls. The recursive equation would be T(n) = T(n - 1) + 1. Also, since most modern
    compilers are able to do call tail elimination, the space complexity if O(1).

    More information on tail recursion adn tail call elimination is here:
    https://www.programmersought.com/article/71146901590/
    https://www.geeksforgeeks.org/tail-recursion/
    https://www.geeksforgeeks.org/tail-call-elimination/

    :param n: integer representing the nth fibonacci number to be calculated
    :param two_previous:
    :param amount:
    :return: integer representing the nth fibonacci number
    """
    if n == 1:
        return amount
    elif n == 2:
        amount += two_previous
        return amount
    else:
        return get_nth_fib_tail_recursive(n - 1, amount, amount + two_previous)


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(1)
def get_nth_fib_iterative_for_loop(n):
    """ Iterative solution with for loop

    Computes the nth fibonacci number only when the 3rd or higher nth fibonacci number is asked. It basically keeps
    track of the previous two fibonacci numbers and sums them up to compute the next one.

    :param n: integer representing the nth fibonacci number to be calculated
    :return: integer representing the nth fibonacci number
    """
    two_previous = 0
    one_previous = 1

    if n == 1:
        return two_previous
    elif n == 2:
        return one_previous
    else:

        n_th_number = 0

        for i in range(3, n + 1):
            n_th_number = one_previous + two_previous
            two_previous = one_previous
            one_previous = n_th_number

        return n_th_number


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(n), because of the hashmap
def get_nth_fib_memoization(n, memoize={1: 0, 2: 1}):
    """ Uses memoization/caching of previous fibonacci numbers

    This would be the next optimization after the traditional recursive solution. The traditional recursive solutions
    calls the recursive function twice for every fibonacci number, this means that it essentially computes most of the
    fibonacci numbers twice. For instance, if asked for fibonacci(n=8). It will call fibonacci(n=7) and fibonacci(n=6)
    and then fibonacci(n=7) itself calls fibonacci(n=6) and fibonacci(n=5). And the previous fibonacci(n=6) from the
    first call, calls fibonacci(n=5) and fibonacci(n=4). And the pattern continuous. This is very inefficient because
    the same numbers are computed multiple times.

    What this solution does is, for every fibonacci number that it computes, it keeps track of it in a hashtable. Every
    time it checks if it is already in a hashtable with previously computed fibonacci numbers, if it is not, then it
    calls itself again (recursive part) to get the previous two numbers (which are always already precomputed and is,
    therefore, only a O(1) time operation) and compute the new fibonacci number.

    For this reason, every fibonacci number is only computed once, making the algorithm a O(n) time and space because it
    stores every single fibonacci number.

    :param n: integer representing the nth fibonacci number to be calculated
    :param memoize:
    :return: integer representing the nth fibonacci number
    """
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_nth_fib_memoization(n - 1, memoize) + get_nth_fib_memoization(n - 2, memoize)
        return memoize[n]


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(1)
def get_nth_fib_iterative_while(n):
    """ Iterative solution with while loop

    It is the same as the iterative solution with for loop. It basically keeps track of the previous two fibonacci
    numbers and sums them up to compute the next one.

    :param n: integer representing the nth fibonacci number to be calculated
    :return: integer representing the nth fibonacci number
    """
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1

    return last_two[1] if n > 1 else last_two[0]
