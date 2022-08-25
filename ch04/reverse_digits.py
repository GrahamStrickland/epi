#! /usr/bin/env python3


def reverse_digits(x: int) -> int:
    forward_string = str(x)
    reverse_string = ""
    sign = -1 if forward_string[0] == '-' else 1
    for i in range(len(forward_string)-1, -1):
        if forward_string[i].isalnum():
            reverse_string += forward_string[i]
    return int(reverse_string) * sign