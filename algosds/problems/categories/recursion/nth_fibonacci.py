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

    This solution check for the base cases, when n=1, it returns 0 and when n=2 it return 1, which are the first two
    Fibonacci numbers. If n is greater than two, then it calls the recursive part of the solution and starts computing
    the previous numbers in the sequence.

    This solution is very expensive regarding its time complexity since every fibonacci number is computed basically
    two times. For instance, when n=10 the recursive part is executed twice, first for computing the (n-1)th fibonacci
    number and then for computing the (n-2)th fibonacci number, which when summed, generate the actual nth fibonacci
    number requested. So in the case of n=10, it would call func(n=9) + func(n=8) and then each of them would call two
    more times the function. n=9 would call func(n=8) + func(n=7)  and n=8 would call func(n=7) + func(n=6). Already it
    can be seen how the work is duplicated.

    The recursive relation for this solution would then be:

    T(n) =        1                 when n = [1, 2]
           T(n-1) + T(n-2) + c      when n > 2

    In this case c=5 because we do 2 comparisons + 2 subtractions + 1 addition

    So to solve the recursion T(n) = T(n-1) + T(n-2) + c, since we have two calls, each of them for distinct values
    (n-1, n-2).

    Because of there are two recursive terms inside the recursive relation the number of nodes in the recursive tree
    grow as a power of 2 depending on the level k, so the nodes at level k are given by nodes = 2^K

    To get the time complexity we have to compute the total cost of leaf nodes (Lc) and the total cost of internal
    nodes (Ic).
    The time complexity would then  be T(n) = O(Lc + Ic)

    To compute Lc we just have to get the number of leaf nodes and then multiply it y the individual node cost, which in
    this case is c=5. so Lc = (total leaf nodes) * (individual node cost)

    Since we know we have 2^k nodes at level k, we have to find the nodes at the last k level. For that we have to
    follow the largest path of the recursion tree and extract the patterns from the recursive part. In this case we
    should start with T(n) -> T(n-1) -> and continue with the successive biggest terms. Since n-1 > n-2 it will take
    longer for T(n-1) and its successive terms to reach the base cases, T(2) or T(1). That is why we follow the path of
    the biggest term.

    The sequence of equations are as follows.

    1. T(n) = T(n-1) + T(n-2) + c  -> follow T(-1)
    2. T(n-1) = T(n-2) + T(n-3) + c  -> follow T(n-2)
    3. T(n-2) = T(n-3) + T(n-4) + c  -> follow T(n-3)
    4. T(n-3) = T(n-4) + T(n-5) + c  -> follow T(n-4)

    Already we can see that the pattern is n - x  where, when following the biggest recursive term, x will take the
    values of [0, 1, 2, 3, ..., n] as follows:
    1. n - 0
    2. n - 1
    3. n - 2
    4. n - 3

    The pattern here can be defined as (n - k) where k is the level (starting from level 0), as stated before.

    With this, we can now get the value for k by solving for T(1) as follows.

    T(n - k) = T(1)
    n - k = 1
    k = n - 1

    If we now plug in the value of k in our equation for nodes we get the following:

    nodes = 2^k
    nodes = 2^(n-1)

    So Lc = (cost of individual node) * (number of leaf nodes) = c * 2^(n-1) this can be further simplified as O(2^n)
    since c * 2^(-1) > 2^n

    Now, we still have to check the total cost of internal nodes Ic. Ic is defined as Ic = sum of costs at each level

    We know there are k = n-1 levels and we know that at each level there are 2^k = 2^n nodes and that each node has a
    cost of c. So the pattern for getting the total cost at level k is c * 2^k. All we have to do is sum c * 2^ from
    k = 0 to k = n-1  in this case we can use the formula ( x^(n+1) - 1 ) / (x - 1)  which works for when summing
    infinite sequences of the form x^0 + x^1 + x^2 + ... where |x| > 1. In this case n = n-1 and x = 2 so we get

    Ic = ( 2^(n-1+1) - 1 ) / (2 - 1)
    Ic = (2^n - 1) / (1)
    Ic = 2^n - 1

    This can be further simplified as Ic = O(2^n)

    So total cost is Cost = Lc + Ic = O(2^n) + O(2^n) = O(2^n)

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
