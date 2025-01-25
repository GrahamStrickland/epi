#!/usr/bin/env


import bisect
import collections
from typing import Callable, List, Tuple

Student = collections.namedtuple("Student", ("name", "grade_point_average"))


def comp_gpa(student: Student) -> Tuple[float, str]:
    return (-student.grade_point_average, student.name)


def search_student(
    students: List[Student],
    target: Student,
    comp_gpa: Callable[[Student], Tuple[float, str]],
):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target
