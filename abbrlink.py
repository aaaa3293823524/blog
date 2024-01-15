#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import time
import glob
import sys


def base36(num):
    seq = "0123456789abcdefghijklmnopqrstuvwxyz"
    res = ""
    while num > 0:
        res += seq[num % 36]
        num //= 36
    return res[::-1]


def abbrlink(s_date):
    _st = int(time.mktime(time.strptime("1996-03-28 00:00:00", "%Y-%m-%d %H:%M:%S")))
    _ed = int(time.mktime(time.strptime(s_date, "%Y-%m-%d %H:%M:%S")))
    return base36((_ed - _st) // 60).rjust(5, "0")


def process_post(post):
    with codecs.open(post, "r", encoding='utf-8') as f:
        data = f.read()
    front = re.findall(r"-{3,}.+?-{3,}", data, re.S)[0]
    s_date = re.findall(r"date: +(\d+-\d+-\d+ +\d+:\d+:\d+)", front)[0]
    abbr = abbrlink(s_date)
    if "abbrlink: " not in front:
        new_front = "{}\nabbrlink: {}\n---".format("\n".join(front.splitlines()[:-1]), abbr)
    else:
        new_front = re.sub("abbrlink: \S+", "abbrlink: " + abbr, front)
    if new_front != front:
        data = data.replace(front, new_front, 1)
        with codecs.open(post, "w", encoding='utf-8') as f:
            f.write(data)


def process():
    for post in glob.glob(os.path.join(os.path.dirname(__file__), "source", "_posts", "*", "*.md")):
        process_post(post)


def _main():
    '''
    处理所有文章
    $ python abbrlink.py
    转换日期为ID
    $ python abbrlink.py 2020-02-20 02:20:02
    '''
    if len(sys.argv) == 1:
        process()
    elif len(sys.argv) == 3 and re.match(r"\d+-\d+-\d+ +\d+:\d+:\d+", ' '.join(sys.argv[1:])):
        print(abbrlink(' '.join(sys.argv[1:])))
    elif len(sys.argv) == 2 and re.match(r"\d+-\d+-\d+ +\d+:\d+:\d+", sys.argv[1]):
        print(abbrlink(sys.argv[1]))
    else:
        print(_main.__doc__)
        


if __name__ == "__main__":
    _main()
