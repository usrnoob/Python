#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from lxml import etree
html = etree.HTML(html)
table = html.xpath("//tr[td]")
table1 = html.xpath('*/table/tbody/tr/td/text()')
print(table1)
print("---- 我是分割线 ---- ")
for row in table:
    table2= [i for i in row.itertext()]
    print(table2)
