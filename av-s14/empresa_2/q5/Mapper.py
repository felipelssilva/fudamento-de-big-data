#!/usr/bin/env python
import sys
import re

COMPANY = "Empresa2"
WORDS = ['contact']


def findwords(tweet):
    for word in WORDS:
        if len(re.findall(word, tweet)) > 0:
            return True
        else:
            return False


def isforcompany(id_autor):
    if id_autor.find(COMPANY) >= 0:
        return True
    else:
        return False


for line in sys.stdin:
    fields = line.split(';')

    id_tweet = fields[0]
    id_autor = fields[1]
    data_criacao = fields[2]
    tweet = fields[3]

    if isforcompany(id_autor) and findwords(tweet):
        print('%s\t%s' % (id_autor, 1))
