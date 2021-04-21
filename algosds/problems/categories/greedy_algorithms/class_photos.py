"""
Problem:

You are tasked with taking photos of a class of students. The class always has an even number of students, and all
students are wearing blue shirts. Your are responsible for arranging the students in two rows before taking the photo.
Each row should contain the same number of students and should adhere to the following guidelines:

- All students wearing red shirts must be in the same row
- All students wearing blue shirts must be in the same row
- Each student in the back row must be strictly taller than the student directly in front of them in the front row

Your are given two input arrays: one containing the heights of all the students with red shirts and another one
containing the heights of all students with blue shirts. These arrays will always have the same length, and each height
will be a positive integer. Write a function that returns whether or not a class photo that follows the stated
guidelines can be taken.

Every class has at least 2 students.


Input:
    red_shirt_heights: [5, 8, 1, 3, 4]
    blue_shirt_heights: [6, 9, 2, 4, 5]

Output:
    return: True
    Blue students go in back row
"""


# Time O( nlg(n) ), where n is the total number of elements in an array
# Space O(1)
def class_photos_simultaneous_check(red_shirt_heights, blue_shirt_heights):
    """ Check simultaneously if photo can be taking for either shirt color on the back.

    :param red_shirt_heights: Non-empty array containing integers representing the heights of students with red shirts
    :param blue_shirt_heights: Non-empty array containing integers representing the heights of students with blue shirts
    :return: True if the photo can be taken following the specified guidelines
    """
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    red_back = True
    blue_back = True

    for idx in range(len(red_shirt_heights)):

        if red_shirt_heights[idx] >= blue_shirt_heights[idx]:
            blue_back = False

        if blue_shirt_heights[idx] >= red_shirt_heights[idx]:
            red_back = False

        if not (blue_back or red_back):
            return False

    return True


# Time O( nlg(n) ), where n is the total number of elements in an array
# Space O(1)
def class_photos_single_check(red_shirt_heights, blue_shirt_heights):
    """ First decides which shirt color should be in the back, then checks if the photo cna be taken.

    :param red_shirt_heights: Non-empty array containing integers representing the heights of students with red shirts
    :param blue_shirt_heights: Non-empty array containing integers representing the heights of students with blue shirts
    :return: True if the photo can be taken following the specified guidelines
    """
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    shirt_color_in_first_row = "RED" if red_shirt_heights[0] < blue_shirt_heights[0] else "BLUE"

    for idx in range(len(red_shirt_heights)):
        red_shirt_current_height = red_shirt_heights[idx]
        blue_shirt_current_height = blue_shirt_heights[idx]

        if red_shirt_current_height == "RED":
            if red_shirt_current_height >= blue_shirt_current_height:
                return False
        else:
            if blue_shirt_current_height >= red_shirt_current_height:
                return False

    return True
