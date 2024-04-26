# -*- coding: utf-8 -*-
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt

file_name = 'GAMES 1995-2019 - 2019-1995.tsv'

# Function that creates a small pipeline of generators for reading single lines
# and turn them into a dictionary og columns and the lines.
def create_gens(file_name):

# Generator for running through the lines one by one
    lines = (line for line in open(file_name, encoding='utf8'))
# Generator for tab splitting the lines
    list_lines = (line.strip().split('\t') for line in lines)
# Gets the first line to use as dictionary keywords
    cols = next(list_lines)
# Generator that creates a dictionary of columns and the splittet data
    dicts = (dict(zip(cols, data)) for data in list_lines)
    return dicts

dicts = create_gens(file_name)

# Generator to search and return values fitting criterias
atelier_ps = (
    str (d["Title"])
    for d in dicts
    if  'Atelier' in d["Title"] and 'PS' in d['Platform(s)']
    )

# Generator filter that returns the title of all games released in 1999.
released_1999 = (
    str (d["Title"])
    for d in dicts
    if '1999' in d['Date']
    )


# Small function to get a list from generator above
dicts = create_gens(file_name)
def test(p):
    l = []
    for i in p:
        l.append(i)
    return l

windows_titles = test(atelier_ps)
print('amount of released Atelier titles from 1995 to 2019 on playstation is:')
print(len(windows_titles))
print('all game names of Atelier series')
print(windows_titles)

# Generator filter that only gives Platform(s) information
consoles = (
    str (d['Platform(s)'])
    for d in dicts
    )


# For every unique platform name found, it will add it to a dictionary and
# count occurrences. Also removes leading and trailing spaces, since these
# were frequent in the data.
def uniq_cons(d):
    l = {}
    for i in d:
        cons = i.split(',')
        cons = [s.strip() for s in cons]
        for c in cons:
            if c in l:
                l[c] += 1
            else:
                l[c] = 1
    return l


cons_rele_total = uniq_cons(consoles)

# As you cannot delete entries while looping through I create a copy and
# delete those instead.
filtered_dict = cons_rele_total.copy()
for key in cons_rele_total.keys():
    if cons_rele_total[key] < 500:
        del filtered_dict[key]

print('The filtered dictionary:')
print(filtered_dict)


plt.figure()
plt.title('Platform game releases above 500')
plt.bar(filtered_dict.keys(), filtered_dict.values())
plt.show()


