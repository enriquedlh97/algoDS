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
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return get_nth_fib_recursive(n - 1) + get_nth_fib_recursive(n - 2)


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(1) if we assume that the compiler does tail call elimination, if not, then we have O(n) space
def get_nth_fib_tail_recursive(n, two_previous=1, amount=0):
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
    two_previous = 0
    one_previous = 1

    if n == 1:
        return two_previous
    elif n == 2:
        return one_previous
    else:

        for i in range(3, n + 1):
            n_th_number = one_previous + two_previous
            two_previous = one_previous
            one_previous = n_th_number

        return n_th_number


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(n), because of the hashmap
def get_nth_fib_memoization(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = get_nth_fib_memoization(n - 1, memoize) + get_nth_fib_memoization(n - 2, memoize)
        return memoize[n]


# Time O(n), where n is the nth fibonacci number (quantity of Fibonacci numbers that have to be computed)
# Space O(1)
def get_nth_fib_iterative_while(n):
    last_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = last_two[0] + last_two[1]
        last_two[0] = last_two[1]
        last_two[1] = next_fib
        counter += 1

    return last_two[1] if n > 1 else last_two[0]
