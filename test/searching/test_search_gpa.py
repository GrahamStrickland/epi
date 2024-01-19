#!/usr/bin/env python3


from nose.tools import assert_equal
from ..search_gpa import Student, comp_gpa, search_student


def test_search_student0():
    students = [('Zorina Abreu', 3.9), ('Zhen Abu-Zahra', 3.2),
            ('Zhanetta Adeyeye', 2.8), ('Yunzhe Alfonso', 3.8),
            ('Youngjin Ahn', 3.1), ('Yu Ahn', 3,5), ('Yoon Akin-Aderibigbe', 3.8),
            ('Yookyung Alexander', 3.7), ('Y-Shiuan Alsamdan', 2.9),
            ('Yingda Alter', 2.7), ('Ying Altmann', 3.9)]
    student = Student('Zhanetta Adeyeye', 2.8)
    obs = search_student(students, student, comp_gpa(student))
    exp = True
    assert_equal(obs, exp)
