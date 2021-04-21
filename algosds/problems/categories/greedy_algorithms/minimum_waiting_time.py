"""
Problem:

Your are given a non-empty array of positive integers representing the amounts of time that specific queries take to \
execute. Only one query can be executed at a time, but the queries can be executed in any order.

A query's  waiting time is defined as the amount of time that it must wait before its execution starts. In other words,
if a query is executed second, then its waiting time is the duration of the first query; if a query is executed third,
then its waiting time is the sum of the durations of the first two queries.

Write a function that returns the minimum amount of total waiting time for all queries. For example, if you are given
the queries durations [1, 4, 5], then the total waiting time if the queries were executed in the order of [5, 1, 4]
would be (0) + (5) + (5 + 1) = 11. The first query duration 5 would be the seconds (duration of the first query) to be
executed, and te last query would have to wait the duration of the first two queries before being executed.

It is allowed to mutate the input array.

Input:
    queries: [3, 2, 1, 2, 6]

Output:
    minimum waiting time: 17
"""


# Time O( nlg(n) ), where n is the total number of elements in the array
# Space O(1)
def minimum_waiting_time(queries):
    """

    :param queries:
    :return:
    """
    queries.sort()
    wait = 0
    for idx in range(1, len(queries)):
        wait = wait + queries[idx - 1] * (len(queries) - idx)

    return wait


# Time O( nlg(n) ), where n is the total number of elements in the array
# Space O(1)
def minimum_waiting_time_original(queries):
    """

    :param queries:
    :return:
    """
    queries.sort()

    total_waiting_time = 0
    for idx, duration in enumerate(queries):
        queries_left = len(queries) - (idx + 1)
        total_waiting_time += duration * queries_left

    return total_waiting_time
