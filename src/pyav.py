#! /usr/bin/python3
import argparse
import com
import crestron.crestron_autodiscovery

parser = argparse.ArgumentParser()
parser.add_argument('-Dc', action='store_true', help='crestron autodiscovery')
parser.add_argument('-o', action='store_true', help='output csv file for discovery output')
parser.add_argument('-c', help='input config file for configuration')
args = parser.parse_args()


if args.Dc:
    crestron.crestron_autodiscovery.autodiscovery()
    if args.o:
        pass
if args.c:
    file = args.c
    with open(file, 'r') as reader:
        lines = reader.readlines()
        for line in lines:
            print(line.strip())
