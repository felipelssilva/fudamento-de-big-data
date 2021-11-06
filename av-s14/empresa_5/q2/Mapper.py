#!/usr/bin/env python
import sys
import re

COMPANY = "@Empresa5"
BADWORDS = ['worst', 'bad', 'never', 'horrible', 'terrible']

def findbadwords(tweet):
    for bad in BADWORDS:
        if len(re.findall(bad, tweet)) > 0:
            return True
        else:
            return False

def isquestion(tweet):
    if tweet.find("?") >= 0:
        return True
    else:
        return False

def isforcompany(tweet):
    if tweet.find(COMPANY) >= 0:
        return True
    else:
        return False

for line in sys.stdin:
    fields = line.split(';')

    id_tweet = fields[0]
    id_autor = fields[1]
    data_criacao = fields[2]
    tweet = fields[3]

    if isforcompany(tweet) and not(isquestion(tweet)) and not(findbadwords(tweet)):
        print '%s\t%s' % (id_autor, 1)

