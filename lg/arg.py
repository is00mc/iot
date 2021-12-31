import argparse
import LG


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', action='store_true', help='lists possible commands')

args = parser.parse_args()

for obj in LG.Command.commands:
    for i in dir(obj):
        print(obj.i)