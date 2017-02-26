#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-26 12:01:25
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os


def search(kw, dir=os.path.abspath('.')):
    for i in os.listdir(dir):
        path = os.path.join(dir, i)
        if os.path.isfile(path) and kw in i:
            print path
        if os.path.isdir(path):
            search(kw, path)

if __name__ == '__main__':
    search('test', '/home/zero/Code')
