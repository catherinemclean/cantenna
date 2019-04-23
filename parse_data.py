#!/usr/bin/env python
from os import listdir
from os.path import isfile, join, getsize
import ast
from statistics import median
import json

def stat_range(lst):
    return max(lst) - min(lst)

data_folder = '.'

parsed_data = []

data_files = [x for x in listdir(data_folder) if isfile(join(data_folder, x)) and x[-3:] == 'txt']

for fn in data_files:
    name = join(data_folder, fn)
    with open(name, errors='ignore') as f:
        ids = fn[:-4].split('_')
        dist = ids[0]
        local = ids[1]
        atype = ids[2]
        lines = f.readlines()
        if '30' in lines[1]:
            passes = 30
            atimel = 31
            atpl = 32
            sll = 34
            qll = 36
            asl = 37
            aql = 38
        else:
            passes = 10
            atimel = 11
            atpl = 12
            sll = 14
            qll = 16
            asl = 17
            aql = 18

        atime = lines[atimel].split()[-1]
        atp = lines[atpl].split()[-1]
        slevels = [int(x) for x in ast.literal_eval(lines[sll])]
        qlevels = [int(x) for x in ast.literal_eval(lines[qll])]
        avg_sig = int(lines[asl].split()[-1])
        avg_qal = int(lines[aql].split()[-1])

        parsed_data.append({'distance': dist,
                            'location': local,
                            'antenna': atype,
                            'passes': passes,
                            'time': atime,
                            'time/point': atp,
                            'signal_levels': slevels,
                            'signal_stats': {'mean': avg_sig,
                                             'median': int(median(slevels)),
                                             'range': stat_range(slevels)},
                            'quality_levels': qlevels,
                            'quality_stats': {'mean': avg_qal,
                                              'median': int(median(qlevels)),
                                              'range': stat_range(qlevels)}})

print(json.dumps(parsed_data, indent=4))