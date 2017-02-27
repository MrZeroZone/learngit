#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-26 21:35:23
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import json


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def sudent2dict(std):
        return{
            'name': std.name,
            'age': std.age,
            'score': std.score
        }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))
