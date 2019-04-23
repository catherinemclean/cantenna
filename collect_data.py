#!/usr/bin/env python

import iw_parse
import sys
from time import sleep
from time import time

TARGET = 'RogueOne'
DATA_PASSES = 30

def get_data():
    return iw_parse.get_interfaces(interface='wlan0')


def process_data(data):
    signal_levels = []
    quality_levels = []
    for data_pass in data:
        for entry in data_pass:
            if entry['Name'] == TARGET:
                signal_levels.append(entry['Signal Level'])
                quality_levels.append(entry['Quality'])

    return signal_levels, quality_levels

def collect():
    data = []
    i = 0
    start = time()
    while i < DATA_PASSES:
        sys.stdout.write('\rCollecting data: Pass {} out of {}'.format(i + 1, DATA_PASSES))
        sys.stdout.flush()
        data.append(get_data())
        sleep(.1)
        i += 1
    end = time()
    sys.stdout.write('\n')
    sys.stdout.write('Data collection took: {}\n'.format(end - start))
    sys.stdout.write('Average time/point: {}\n'.format((end-start)/DATA_PASSES))
    sys.stdout.flush()
    return data


def avg(data):
    return sum(map(int, data)) / len(data)


if __name__ == '__main__':
    sdata, qdata = process_data(collect())
    sys.stdout.write('Signal levels:\n{}\n'.format(sdata))
    sys.stdout.write('Quality levels:\n{}\n'.format(qdata))
    sys.stdout.write('Average signal level: {}\n'.format(avg(sdata)))
    sys.stdout.write('Average quality level: {}\n'.format(avg(qdata)))
    sys.stdout.flush()
