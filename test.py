#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-22 19:24:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# test
# f1 = 1
# f2 = 2
# for i in range(1, 21):
#     print '%12ld %12ld' % (f1, f2),
#     if (i % 3) == 0:
#         print ''
#     f1 = f1+f2
#     f2 = f1+f2

# h = 0
# leap = 1
# from math import sqrt
# from sys import stdout
# for m in range(101, 201):
#     k = int(sqrt(m+1))
#     for i in range(2, k+1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print '%-4d' % m
#         h += 1
#         if h % 10 == 0:
#             print ''
#     leap = 1
# print 'The total is %d' % h

# for n in range(100, 1000):
#     i = n/100
#     j = n/10 % 10
#     k = n % 10
#     if n == i**3+j**3+k**3:
#         print n


# def reduceNum(n):
#     print '{}='.format(n),
#     if not isinstance(n, int) or n <= 0:
#         print '请输入一个正确的数字！'
#         exit(0)
#     elif n in [1]:
#         print '{}'.format(n)
#     while n not in [1]:  # 循环保证递归
#         for index in xrange(2, n+1):
#             if n % index == 0:
#                 n /= index  # n 等于 n/index
#                 if n == 1:
#                     print index
#                 else:  # index 一定是素数
#                     print '{}*'.format(index),
#                 break
# reduceNum(99)
# reduceNum(100)

# while 1:
#     score = int(raw_input('input score:\n'))
#     if score != 0:
#         if score >= 90:
#             grade = 'A'
#         elif score >= 60:
#             grade = 'B'
#         else:
#             grade = 'C'
#         print '%d belongs to %s' % (score, grade)
#     else:
#         break

# import datetime
# if __name__ == '__main__':
#     # 输出今日日期，格式为 dd/mm/yyyy.
#     print(datetime.date.today().strftime('%d/%m/%Y'))
#     # 创建日期对象
#     miyazakiBirthDate = datetime.date(1941, 1, 5)
#     print(miyazakiBirthDate.strftime('%d/%m/%Y'))
#     # 日期算术运算
#     miyazakiBirthNextDay = miyazakiBirthDate+datetime.timedelta(days=1)
#     print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
#     # 日期替换
#     miyazakiFirstBirthday = miyazakiBirthDate.replace(
#         year=miyazakiBirthDate.year+1)
#     print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))

# import string
# s = raw_input('input a string:\n')
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print 'char=%d,space=%d,digit=%d,others=%d' % (letters, space, digit, others)

# Tn = 0
# Sn = []
# n = int(raw_input('n=:\n'))
# a = int(raw_input('a=:\n'))
# for count in range(n):
#     Tn = Tn+a
#     a = a*10
#     Sn.append(Tn)
#     print Tn
# Sn = reduce(lambda x, y: x+y, Sn)
# print Sn

# from sys import stdout
# for j in range(2, 1000):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#     if s == 0:
#         print j
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print k[n]

# tour = []
# height = []
# hei = 100.0  # 起始高度
# tim = 10  # 次数
# for i in range(1, tim+1):
#     tour.append(hei)
#     hei /= 2
#     height.append(hei)
# print('总高度:tour={0}'.format(sum(tour)))
# print('第10次反弹高度:height={0}'.format(height[-1]))
