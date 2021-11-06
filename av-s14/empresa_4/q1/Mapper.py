#!/usr/bin/env python
import sys

for line in sys.stdin:
    fields = line.split(';')

    id_tweet = fields[0]
    id_autor = fields[1]
    data_criacao = fields[2]
    tweet = fields[3]

    if tweet.find("@Empresa4") >= 0:
        print '%s\t%s' % (id_autor, 1)

