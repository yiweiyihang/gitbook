#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO:
f = StringIO('ˮ��ϸ������\n�����������\n��ͤ��С�У�\n�ƻ�ҹױ����')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())