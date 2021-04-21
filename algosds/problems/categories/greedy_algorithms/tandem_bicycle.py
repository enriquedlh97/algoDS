"""
Problem:

A tandem bicycle is a bicycle that's operated by two people: person A and person B. Both people pedal the bicycle, but
the person that pedals faster dictates the speed of the bicycle. So if person A pedals at a speed of 5, and person B
pedals at a speed of 4, the tandem bicycle moves at a speed of 5 (i.e., tandemSpeed = max(speedA, speedB) ).

You're given two lists of positive integers: one that contains the speeds of riders wearing red shirts and one that
contains the speeds of riders wearing blue shirts. Each rider is represented by a single positive integer, which is the
speed that they pedal a tandem bicycle at. Both lists have the same length, meaning that there are as many red-shirt
riders as there are blue-shirt riders. Your goal is to pair every rider wearing a red shirt with a rider wearing a blue
shirt to operate a tandem bicycle.

Write a function that returns the maximum possible total speed or the minimum possible total speed of all of the
tandem bicycles being ridden based on an input parameter, "fastest". If fastest=True, your function should return the
maximum possible total speed; otherwise it should return the minimum total speed.

"Total speed" is defined as the sum of the speeds of all the tandem bicycles being ridden. For example if there are 4
riders (2 red-shirt riders and 2 blue-shirt riders) who have speeds of 1, 3, 4, 5 , and if they're paired on tandem
bicycles as follows:
[1, 4], [5, 3] , then the total speed of these tandem bicycles is 4 + 5 = 9.

Input:
    red_shirt_speeds: [5, 5, 3, 9, 2]
    blue_shirt_speeds: [3, 6, 7, 2, 1]
    fastest: True

Output:
    return: 32
"""


# Time O( nlg(n) ), where n is the total number of elements in an array
# Space O(1)
def tandem_bicycle(red_shirt_speeds, blue_shirt_speeds, fastest):
    """ My solution

    This solution pairs the max value of one array with the min value of the other array when fastest=True and keeps
     going like this until all pairs are formed. When fastest=False it pairs the max value of one array with the max
     value of the other array.

    :param red_shirt_speeds: array containing integers representing the speeds of riders with red shirt
    :param blue_shirt_speeds: array containing integers representing the speeds of riders with blue shirt
    :param fastest: boolean value indicating whether the total fastest or total slowest speed is to be computed
    :return: total speed
    """
    red_shirt_speeds.sort(reverse=True)

    if fastest:
        blue_shirt_speeds.sort()
    else:
        blue_shirt_speeds.sort(reverse=True)

    total_speed = 0

    for idx in range(len(red_shirt_speeds)):
        total_speed += max(red_shirt_speeds[idx], blue_shirt_speeds[idx])

    return total_speed


def tandem_bicycle_original(red_shirt_speeds, blue_shirt_speeds, fastest):
    """ Original Solution

    This solution is essentially the same as the one above, the only difference is that botha arrays are sorted in
    ascending order and then, when checked if fastest=True, if it is in deed True, one of the arrays is reversed.

    :param red_shirt_speeds: array containing integers representing the speeds of riders with red shirt
    :param blue_shirt_speeds: array containing integers representing the speeds of riders with blue shirt
    :param fastest: boolean value indicating whether the total fastest or total slowest speed is to be computed
    :return: total speed
    """
    red_shirt_speeds.sort()
    blue_shirt_speeds.sort()

    if not fastest:
        reverse_array_in_place(red_shirt_speeds)

    total_speed = 0

    for idx in range(len(red_shirt_speeds)):
        rider_1 = red_shirt_speeds[idx]
        rider_2 = blue_shirt_speeds[len(blue_shirt_speeds) - idx - 1]
        total_speed += max(rider_1, rider_2)

    return total_speed


def reverse_array_in_place(array):
    """ Helper function for original solution. Reverses array in-place

    :param array: array to be reversed in-place
    :return: None
    """
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
