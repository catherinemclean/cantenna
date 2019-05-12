#!/usr/bin/env python

import json

with open('results.json', 'r') as results:
    stats = []
    data = json.load(results)

    for entry in data:
        stats.append((entry['signal_stats']['mean'],
                      entry['signal_stats']['median'],
                      entry['distance'],
                      entry['antenna'],
                      entry['passes']))

    s = sorted(stats)
    s.reverse()
    for x in s:
        if not x[4] == 10:
            print('{} {} mean: {} meadian: {}'.format(x[2], x[3], x[0], x[1]))

