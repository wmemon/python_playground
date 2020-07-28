"""
A robot moves in a plane starting from the original point (0,0).
 The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
 The numbers after the direction are steps. Please write a program to compute
 the distance from current position after a sequence of movement and original point.
 If the distance is a float, then just print the nearest integer.

Input:- UP 5
        DOWN 3
        LEFT 3
        RIGHT 2

Output:- 2
"""

import math


def get_direction_and_movement(string):
    string = string.upper()
    if not isinstance(string, str):
        return "[!]Please enter String as an input."

    string_list = string.split(' ')
    if not (len(string_list) == 2):
        print("[!]The command was not recognised.")
        return None

    if not (string_list[0] == 'UP' or string_list[0] == 'DOWN' or string_list[0] == 'LEFT' or
            string_list[0] == 'RIGHT'):
        print("[!]The command was not recognised.")
        return None

    try:
        string_list[1] = int(string_list[1])
    except ValueError:
        print("[!]The command was not recognised.")
        return None

    return [string_list[0], string_list[1]]


def find_position(coordinates, list_position):

    if not isinstance(coordinates, str):
        return "[!]Please enter the coordinates separated by comma."

    coordinates_list = [int(i) for i in coordinates.split(',')]

    if not len(coordinates_list) == 2:
        return "[!] Input x and y coordinates respectively. eg:- x,y"

    if list_position[0] == 'UP':
        coordinates_list[0] += list_position[1]
        return ','.join([str(i) for i in coordinates_list])

    if list_position[0] == 'DOWN':
        coordinates_list[0] -= list_position[1]
        return ','.join([str(i) for i in coordinates_list])

    if list_position[0] == 'LEFT':
        coordinates_list[1] -= list_position[1]
        return ','.join([str(i) for i in coordinates_list])

    if list_position[0] == 'RIGHT':
        coordinates_list[1] += list_position[1]
        return ','.join([str(i) for i in coordinates_list])

    return None


def find_dist(coordinates):
    if not isinstance(coordinates, str):
        return "[!]Please enter the coordinates separated by comma."
    coordinates_list = [int(i) for i in coordinates.split(',')]
    if not len(coordinates_list) == 2:
        return "[!] Input x and y coordinates respectively. eg:- x,y"

    return math.sqrt(coordinates_list[0] ** 2 + coordinates_list[1] ** 2)


def main():
    coordinate = '0,0'
    print("Starting program.. enter stop to stop")

    while True:
        command = input("Enter command: ")
        if command.upper() == 'STOP':
            break
        if not get_direction_and_movement(command):
            continue

        coordinate = find_position((coordinate), get_direction_and_movement(command))

    print(f" The distance is :- {round(find_dist(coordinate))}")


if __name__ == '__main__':
    main()
