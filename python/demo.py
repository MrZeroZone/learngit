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

# 21：猴子吃桃问题
# x2 = 1
# for day in range(9, 0, -1):
#     x1 = (x2+1)*2
#     x2 = x1
# print x1

# 22：比赛名单
# for i in range(ord('x'), ord('z')+1):
#     for j in range(ord('x'), ord('z')+1):
#         if i != j:
#             for k in range(ord('x'), ord('z')+1):
#                 if(i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
# print 'order is a -- %s\t b -- %s\tc--%s' % (chr(i), chr(j), chr(k))

# 23：打印菱形
# from sys import stdout
# for i in range(4):
#     for j in range(2-i+1):
#         stdout.write(' ')
#     for k in range(2*i+1):
#         stdout.write('*')
#     print
# for i in range(3):
#     for j in range(i+1):
#         stdout.write(' ')
#     for k in range(4-2*i+1):
#         stdout.write('*')
#     print

# 24：分数序列
# a = 2.0
# b = 1.0
# s = 0
# for n in range(1, 21):
#     s += a/b
#     t = a
#     a = a+b
#     b = t
# print s

# 25：求1+2!+3!+...+20!的和
# n = 0
# s = 0
# t = 1
# for n in range(1, 21):
#     t *= n
#     s += t
# print '1!+2!+3!+...+20!=%d' % s

# 26：利用递归方法求5!
# def fact(j):
#     sum = 0
#     if j == 0:
#         sum = 1
#     else:
#         sum = j*fact(j-1)
#     return sum
# for i in range(6):
#     print '%d!=%d' % (i, fact(i))

# 27：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来
# def output(s, l):
#     if l == 0:
#         return
#     print(s[l-1])
#     output(s, l-1)

# s = raw_input('Input a string:')
# l = len(s)
# output(s, l)

# 28：递归
# def age(n):
#     if n == 1:
#         c = 10
#     else:
#         c = age(n-1)+2
#     return c

# print age(5)

# 29：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字
# x = int(raw_input("请输入一个数:\n"))
# a = x/10000
# b = x % 10000/1000
# c = x % 1000/100
# d = x % 100/10
# e = x % 10

# if a != 0:
#     print "5位数：", e, d, c, b, a
# elif b != 0:
#     print "4位数：", e, d, c, b,
# elif c != 0:
#     print "3位数：", e, d, c
# elif d != 0:
#     print "2位数：", e, d
# else:
#     print "1位数：", e

# 30：一个5位数，判断它是不是回文数，个位与万位相同，十位与千位相同
# a = int(raw_input("请输入一个数字:\n"))
# x = str(a)
# flag = True
# for i in range(len(x)/2):
#     if x[i] != x[-i-1]:
#         flag = False
#         break
# if flag:
#     print "%d 是一个回文数！" % a
# else:
#     print "%d 不是一个回文数！" % a
