#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import pickle

import urllib.request
import lxml.html


URL = 'http://www.w3schools.com/cssref/css3_browsersupport.asp'

root = lxml.html.fromstring(urllib.request.urlopen(URL).read())


rows = root.xpath('//table/tr')

prefixable = set()
for line in rows:
    name, *browsers = line.getchildren()

    if any(b.values()[0].startswith('bsPre') for b in browsers):
        prefixable.add(name.text_content())


with open('pickled_tags', 'bw') as file:
    pickle.dump(prefixable, file)


